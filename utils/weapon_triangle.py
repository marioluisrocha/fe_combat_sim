"""
Weapon triangle utilities for Fire Emblem Combat Simulator.
"""

class WeaponTriangle:
    """Class for handling weapon triangle advantages and disadvantages."""
    
    # Standard Fire Emblem weapon triangle: Sword > Axe > Lance > Sword
    WEAPON_ADVANTAGES = {
        "Sword": ["Axe"],
        "Lance": ["Sword"],
        "Axe": ["Lance"],
        "Bow": [],
        "Tome": [],
        "Staff": []
    }
    
    # Modern Fire Emblem games added magic triangle
    MAGIC_TRIANGLE = {
        "Fire": ["Wind"],
        "Wind": ["Thunder"],
        "Thunder": ["Fire"]
    }
    
    @classmethod
    def get_advantage(cls, attacker_weapon_type, defender_weapon_type):
        """
        Calculate weapon triangle advantage.
        
        Args:
            attacker_weapon_type (str): Attacker's weapon type
            defender_weapon_type (str): Defender's weapon type
            
        Returns:
            int: 1 for advantage, -1 for disadvantage, 0 for neutral
        """
        # Check if attacker has advantage
        if (attacker_weapon_type in cls.WEAPON_ADVANTAGES and 
            defender_weapon_type in cls.WEAPON_ADVANTAGES[attacker_weapon_type]):
            return 1
            
        # Check if defender has advantage
        if (defender_weapon_type in cls.WEAPON_ADVANTAGES and 
            attacker_weapon_type in cls.WEAPON_ADVANTAGES[defender_weapon_type]):
            return -1
            
        return 0
    
    @classmethod
    def apply_advantage(cls, attacker_weapon, defender_weapon, damage, hit):
        """
        Apply weapon triangle effects to damage and hit.
        
        Args:
            attacker_weapon (Weapon): Attacker's weapon
            defender_weapon (Weapon): Defender's weapon
            damage (int): Base damage
            hit (int): Base hit rate
            
        Returns:
            tuple: Modified (damage, hit)
        """
        if not attacker_weapon or not defender_weapon:
            return damage, hit
            
        advantage = cls.get_advantage(attacker_weapon.weapon_type, defender_weapon.weapon_type)
        
        if advantage == 1:
            # Advantage: +1 damage, +15 hit
            return damage + 1, hit + 15
        elif advantage == -1:
            # Disadvantage: -1 damage, -15 hit
            return max(0, damage - 1), max(0, hit - 15)
        else:
            # Neutral: no change
            return damage, hit
