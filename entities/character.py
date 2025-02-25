"""
Character class for Fire Emblem Combat Simulator.
"""

from fe_combat_sim.entities.character_class import CharacterClass, get_class

class Character:
    """Base class for all characters in the game."""
    
    def __init__(self, name, character_class, stats, weapon=None):
        """
        Initialize a character.
        
        Args:
            name (str): Character name
            character_class (str or CharacterClass): Character class
            stats (dict): Character statistics
            weapon (Weapon, optional): Equipped weapon
        """
        self.name = name
        
        # Process character_class - accept either a string or a CharacterClass object
        if isinstance(character_class, str):
            self.character_class = get_class(character_class)
            if not self.character_class:
                # If not found in predefined classes, create a basic one
                self.character_class = CharacterClass(character_class)
        else:
            self.character_class = character_class
            
        self.stats = stats
        self.weapon = weapon
        self.current_hp = stats.get("hp", 0)
    
    def attack(self, target):
        """
        Attack another character.
        
        Args:
            target (Character): Target character
            
        Returns:
            dict: Results of the attack
        """
        if not self.weapon:
            return {"success": False, "message": "No weapon equipped"}
        
        damage = self._calculate_damage(target)
        target.current_hp = max(0, target.current_hp - damage)
        
        return {
            "success": True,
            "attacker": self.name,
            "defender": target.name,
            "damage": damage,
            "defender_hp_remaining": target.current_hp
        }
    
    def _calculate_damage(self, target):
        """
        Calculate damage against target.
        
        Args:
            target (Character): Target character
            
        Returns:
            int: Calculated damage
        """
        # Basic damage calculation
        if self.weapon.is_physical():
            atk = self.stats.get("str", 0) + self.weapon.might
            defense = target.stats.get("def", 0)
        else:
            atk = self.stats.get("mag", 0) + self.weapon.might
            defense = target.stats.get("res", 0)
        
        # Calculate base damage
        damage = max(0, atk - defense)
        
        # Apply effectiveness multiplier
        effectiveness_multiplier = self.weapon.get_effectiveness_multiplier(target)
        damage = int(damage * effectiveness_multiplier)
        
        return damage
        
    def __str__(self):
        """String representation of the character."""
        return f"{self.name} ({self.character_class})"
        
    def __repr__(self):
        """Detailed representation of the character."""
        return f"Character(name='{self.name}', class='{self.character_class}', HP={self.current_hp}/{self.stats.get('hp', 0)})"
