"""
Battle system for Fire Emblem Combat Simulator.
"""
import random
from fe_combat_sim.utils.weapon_triangle import WeaponTriangle

class Battle:
    """Handles combat encounters between characters."""
    
    def __init__(self, attacker, defender, terrain=None):
        """
        Initialize a battle between two characters.
        
        Args:
            attacker (Character): Attacking character
            defender (Character): Defending character
            terrain (dict, optional): Terrain effects
        """
        self.attacker = attacker
        self.defender = defender
        self.terrain = terrain or {}
        self.log = []
    
    def simulate_round(self):
        """
        Simulate a full round of combat.
        
        Returns:
            dict: Results of the combat round
        """
        # Attacker attacks first
        attacker_result = self._perform_attack(self.attacker, self.defender)
        self.log.append(attacker_result)
        
        # Check if defender is defeated
        if self.defender.current_hp <= 0:
            return {"victory": True, "victor": self.attacker.name, "log": self.log}
        
        # Determine if defender can counter-attack
        can_counter = self._can_counter_attack()
        
        if can_counter:
            defender_result = self._perform_attack(self.defender, self.attacker)
            self.log.append(defender_result)
            
            # Check if attacker is defeated
            if self.attacker.current_hp <= 0:
                return {"victory": True, "victor": self.defender.name, "log": self.log}
        
        # Handle follow-up attacks based on speed
        if self._can_perform_follow_up(self.attacker, self.defender) and self.defender.current_hp > 0:
            follow_up_result = self._perform_attack(self.attacker, self.defender)
            self.log.append(follow_up_result)
            
            if self.defender.current_hp <= 0:
                return {"victory": True, "victor": self.attacker.name, "log": self.log}
                
        elif self._can_perform_follow_up(self.defender, self.attacker) and can_counter and self.attacker.current_hp > 0:
            follow_up_result = self._perform_attack(self.defender, self.attacker)
            self.log.append(follow_up_result)
            
            if self.attacker.current_hp <= 0:
                return {"victory": True, "victor": self.defender.name, "log": self.log}
        
        return {"victory": False, "log": self.log}
    
    def _perform_attack(self, attacker, defender):
        """
        Perform a single attack.
        
        Args:
            attacker (Character): Attacking character
            defender (Character): Defending character
            
        Returns:
            dict: Result of the attack
        """
        # Calculate hit chance
        hit_rate = self._calculate_hit_rate(attacker, defender)
        hit_roll = random.randint(1, 100)
        
        if hit_roll > hit_rate:
            return {
                "attacker": attacker.name,
                "defender": defender.name,
                "hit": False,
                "message": f"{attacker.name}'s attack missed!"
            }
        
        # Calculate if attack is a critical hit
        crit_rate = self._calculate_crit_rate(attacker, defender)
        crit_roll = random.randint(1, 100)
        is_crit = crit_roll <= crit_rate
        
        # Calculate damage
        base_damage = attacker._calculate_damage(defender)
        damage = base_damage * (3 if is_crit else 1)
        
        # Check for effectiveness
        effectiveness = attacker.weapon.is_effective_against(defender)
        
        # Apply damage
        defender.current_hp = max(0, defender.current_hp - damage)
        
        return {
            "attacker": attacker.name,
            "defender": defender.name,
            "hit": True,
            "critical": is_crit,
            "effective": effectiveness,
            "damage": damage,
            "defender_hp_remaining": defender.current_hp,
            "message": self._generate_attack_message(attacker, defender, damage, is_crit, effectiveness)
        }
    
    def _generate_attack_message(self, attacker, defender, damage, is_crit, is_effective):
        """
        Generate a message describing the attack result.
        
        Args:
            attacker (Character): Attacking character
            defender (Character): Defending character
            damage (int): Damage dealt
            is_crit (bool): Whether the attack was a critical hit
            is_effective (bool): Whether the attack was effective against the target
            
        Returns:
            str: Message describing the attack
        """
        message = f"{attacker.name}"
        
        if is_effective:
            message += " attacks with effectiveness!"
        
        if is_crit:
            message += " lands a critical hit!"
        else:
            message += " attacks!"
            
        message += f" Deals {damage} damage to {defender.name}!"
        
        return message
    
    def _calculate_hit_rate(self, attacker, defender):
        """
        Calculate hit rate.
        
        Args:
            attacker (Character): Attacking character
            defender (Character): Defending character
            
        Returns:
            int: Hit rate percentage
        """
        weapon_hit = attacker.weapon.hit if attacker.weapon else 0
        skill = attacker.stats.get("skl", 0)
        luck = attacker.stats.get("lck", 0) // 2
        
        hit = weapon_hit + skill * 2 + luck
        
        avoid = defender.stats.get("spd", 0) * 2 + defender.stats.get("lck", 0)
        
        # Apply terrain effects if any
        terrain_avoid = 0
        if self.terrain:
            terrain_avoid = self.terrain.get("avoid", 0)
        
        # Apply weapon triangle effects
        if attacker.weapon and defender.weapon:
            hit_mod = WeaponTriangle.apply_advantage(
                attacker.weapon, defender.weapon, 0, hit
            )[1]
            hit = hit_mod
        
        final_hit_rate = min(100, max(0, hit - avoid - terrain_avoid))
        return final_hit_rate
    
    def _calculate_crit_rate(self, attacker, defender):
        """
        Calculate critical hit rate.
        
        Args:
            attacker (Character): Attacking character
            defender (Character): Defending character
            
        Returns:
            int: Critical hit rate percentage
        """
        weapon_crit = attacker.weapon.crit if attacker.weapon else 0
        skill = attacker.stats.get("skl", 0)
        
        crit = weapon_crit + skill // 2
        
        crit_avoid = defender.stats.get("lck", 0)
        
        final_crit_rate = max(0, crit - crit_avoid)
        return final_crit_rate
    
    def _can_counter_attack(self):
        """
        Determine if defender can counter-attack.
        
        Returns:
            bool: True if defender can counter-attack
        """
        if not self.defender.weapon:
            return False
        
        attacker_range = self.attacker.weapon.range if self.attacker.weapon else (1, 1)
        defender_range = self.defender.weapon.range if self.defender.weapon else (1, 1)
        
        # Assume 1 tile distance for simplicity
        combat_range = 1
        
        return (defender_range[0] <= combat_range <= defender_range[1])
    
    def _can_perform_follow_up(self, character, opponent):
        """
        Determine if character can perform a follow-up attack.
        
        Args:
            character (Character): Character to check
            opponent (Character): Opponent character
            
        Returns:
            bool: True if character can perform a follow-up attack
        """
        char_spd = character.stats.get("spd", 0)
        opp_spd = opponent.stats.get("spd", 0)
        
        # Character needs 5 or more speed than opponent
        return char_spd >= opp_spd + 5
