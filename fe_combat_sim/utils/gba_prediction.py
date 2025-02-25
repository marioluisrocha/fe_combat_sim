"""
Updated prediction utility functions for Fire Emblem Combat Simulator with GBA weapons.
"""
import random
from fe_combat_sim.combat.battle import Battle

def predict_damage(attacker, defender):
    """
    Predict the damage that an attacker would deal to a defender.
    
    Args:
        attacker: The attacking character
        defender: The defending character
        
    Returns:
        dict: Damage prediction information
    """
    # Check if the attacker has a weapon
    if not attacker.weapon:
        return {
            "min_damage": 0,
            "max_damage": 0,
            "crit_damage": 0,
            "hit_rate": 0,
            "crit_rate": 0,
            "effectiveness": False
        }
    
    # Create a temporary battle to use its calculation methods
    temp_battle = Battle(attacker, defender)
    
    # Calculate hit rate
    hit_rate = temp_battle._calculate_hit_rate(attacker, defender)
    
    # Calculate crit rate
    crit_rate = temp_battle._calculate_crit_rate(attacker, defender)
    
    # Calculate base damage
    base_damage = attacker._calculate_damage(defender)
    
    # Calculate critical damage
    crit_damage = base_damage * 3
    
    # Check for effectiveness
    effectiveness = attacker.weapon.is_effective_against(defender)
    
    # Check if weapon has brave effect (strikes twice)
    is_brave = "Brave" in attacker.weapon.name
    
    # Apply weapon triangle effects
    weapon_triangle_advantage = 0
    if attacker.weapon and defender.weapon:
        from fe_combat_sim.utils.weapon_triangle import WeaponTriangle
        weapon_triangle_advantage = WeaponTriangle.get_advantage(
            attacker.weapon.weapon_type, defender.weapon.weapon_type
        )
    
    return {
        "min_damage": base_damage,  # Minimum damage (no critical)
        "max_damage": base_damage,  # Maximum damage (no critical)
        "crit_damage": crit_damage,  # Critical hit damage
        "hit_rate": hit_rate,       # Hit rate percentage
        "crit_rate": crit_rate,     # Critical hit rate percentage
        "effectiveness": effectiveness,  # Whether weapon is effective against defender
        "brave": is_brave,          # Whether weapon strikes twice
        "weapon_triangle": weapon_triangle_advantage  # Weapon triangle advantage
    }

def predict_battle_outcome(attacker, defender, iterations=100):
    """
    Predict the outcome of a battle through Monte Carlo simulation.
    
    Args:
        attacker: The attacking character
        defender: The defending character
        iterations: Number of simulations to run
        
    Returns:
        dict: Battle outcome prediction statistics
    """
    # Store original HP values to reset after each simulation
    attacker_hp = attacker.current_hp
    defender_hp = defender.current_hp
    
    results = {
        "attacker_victories": 0,
        "defender_victories": 0,
        "no_victory": 0,
        "average_attacker_remaining_hp": 0,
        "average_defender_remaining_hp": 0,
        "average_rounds": 0,
        "average_attacks": 0,
        "critical_hits": 0,
        "misses": 0
    }
    
    for _ in range(iterations):
        # Reset HP
        attacker.current_hp = attacker_hp
        defender.current_hp = defender_hp
        
        # Create a new battle
        battle = Battle(attacker, defender)
        
        # Simulate combat for up to 10 rounds (to avoid potential infinite loops)
        round_count = 0
        attack_count = 0
        max_rounds = 10
        
        while round_count < max_rounds:
            round_count += 1
            
            # Simulate a round
            result = battle.simulate_round()
            
            # Count attacks and track hits/misses/crits
            for entry in battle.log:
                attack_count += 1
                if not entry.get("hit", False):
                    results["misses"] += 1
                elif entry.get("critical", False):
                    results["critical_hits"] += 1
            
            # Check if battle is over
            if result.get("victory", False):
                if result["victor"] == attacker.name:
                    results["attacker_victories"] += 1
                else:
                    results["defender_victories"] += 1
                break
            
            # If we reach max rounds without victory, count as no victory
            if round_count == max_rounds:
                results["no_victory"] += 1
        
        # Track remaining HP and rounds
        results["average_attacker_remaining_hp"] += attacker.current_hp
        results["average_defender_remaining_hp"] += defender.current_hp
        results["average_rounds"] += round_count
        results["average_attacks"] += attack_count
    
    # Calculate averages
    results["average_attacker_remaining_hp"] /= iterations
    results["average_defender_remaining_hp"] /= iterations
    results["average_rounds"] /= iterations
    results["average_attacks"] /= iterations
    
    # Calculate victory percentages
    results["attacker_victory_percentage"] = (results["attacker_victories"] / iterations) * 100
    results["defender_victory_percentage"] = (results["defender_victories"] / iterations) * 100
    results["no_victory_percentage"] = (results["no_victory"] / iterations) * 100
    
    # Calculate hit/miss/crit percentages
    total_attacks = results["average_attacks"] * iterations
    if total_attacks > 0:
        results["miss_percentage"] = (results["misses"] / total_attacks) * 100
        results["crit_percentage"] = (results["critical_hits"] / total_attacks) * 100
    else:
        results["miss_percentage"] = 0
        results["crit_percentage"] = 0
    
    # Reset HP to original values
    attacker.current_hp = attacker_hp
    defender.current_hp = defender_hp
    
    return results
