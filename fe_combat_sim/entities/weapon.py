"""
Weapon class for Fire Emblem Combat Simulator.
"""

class Weapon:
    """Base class for all weapons in the game."""
    
    WEAPON_TYPES = ["Sword", "Lance", "Axe", "Bow", "Tome", "Staff", "Other"]
    
    def __init__(self, name, weapon_type, might, hit, crit=0, range=(1, 1), uses=None, 
                 effective_against=None):
        """
        Initialize a weapon.
        
        Args:
            name (str): Weapon name
            weapon_type (str): Type of weapon
            might (int): Base damage
            hit (int): Hit rate modifier
            crit (int, optional): Critical hit rate modifier
            range (tuple, optional): Range of weapon (min, max)
            uses (int, optional): Number of uses before breaking
            effective_against (list, optional): List of class types the weapon is effective against
        """
        if weapon_type not in self.WEAPON_TYPES:
            raise ValueError(f"Invalid weapon type. Must be one of {self.WEAPON_TYPES}")
        
        self.name = name
        self.weapon_type = weapon_type
        self.might = might
        self.hit = hit
        self.crit = crit
        self.range = range
        self.uses = uses
        self.current_uses = uses
        self.effective_against = effective_against or []
    
    def is_physical(self):
        """
        Check if the weapon is physical or magical.
        
        Returns:
            bool: True if physical, False if magical
        """
        return self.weapon_type not in ["Tome", "Staff"]
    
    def is_effective_against(self, character):
        """
        Check if the weapon is effective against a character's class.
        
        Args:
            character: Character to check effectiveness against
            
        Returns:
            bool: True if the weapon is effective against the character's class
        """
        if not self.effective_against or not character.character_class:
            return False
            
        for class_type in self.effective_against:
            if character.character_class.is_type(class_type):
                return True
                
        return False
    
    def get_effectiveness_multiplier(self, character):
        """
        Get the damage multiplier based on effectiveness.
        
        Args:
            character: Character to check effectiveness against
            
        Returns:
            float: Damage multiplier (typically 2.0 or 3.0 for effectiveness)
        """
        return 3.0 if self.is_effective_against(character) else 1.0
    
    def use(self):
        """
        Use the weapon once.
        
        Returns:
            bool: True if weapon can still be used, False if broken
        """
        if self.uses is None:
            return True
        
        if self.current_uses > 0:
            self.current_uses -= 1
            
        return self.current_uses > 0
        
    def __str__(self):
        """String representation of the weapon."""
        return self.name
        
    def __repr__(self):
        """Detailed representation of the weapon."""
        effective_str = ", ".join(self.effective_against) if self.effective_against else "None"
        return (f"Weapon(name='{self.name}', type='{self.weapon_type}', might={self.might}, "
                f"hit={self.hit}, crit={self.crit}, range={self.range}, uses={self.uses}, "
                f"effective_against=[{effective_str}])")


# Define some common weapon effectiveness combinations
ARMOR_EFFECTIVE = ["Armored"]
CAVALRY_EFFECTIVE = ["Horseback", "Mounted"]
FLIER_EFFECTIVE = ["Flying"]
DRAGON_EFFECTIVE = ["Dragon"]
