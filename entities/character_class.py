"""
Character class definitions for Fire Emblem Combat Simulator.
"""

class CharacterClass:
    """Class representing a character's class/job in the game."""
    
    def __init__(self, name, movement=5, class_types=None):
        """
        Initialize a character class.
        
        Args:
            name (str): Name of the class (e.g., "Knight", "Pegasus Knight")
            movement (int): Base movement range
            class_types (list): List of class types for weakness/resistance calculation
        """
        self.name = name
        self.movement = movement
        self.class_types = class_types or []
        
    def is_type(self, class_type):
        """
        Check if the class has a specific type.
        
        Args:
            class_type (str): Class type to check for
            
        Returns:
            bool: True if the class has the specified type
        """
        return class_type in self.class_types
        
    def __str__(self):
        """String representation of the class."""
        return self.name
        
    def __repr__(self):
        """Detailed representation of the class."""
        types_str = ", ".join(self.class_types) if self.class_types else "None"
        return f"CharacterClass(name='{self.name}', movement={self.movement}, class_types=[{types_str}])"


# Define common character classes
INFANTRY = CharacterClass("Infantry", 5, ["Infantry"])
KNIGHT = CharacterClass("Knight", 4, ["Armored", "Infantry"])
CAVALIER = CharacterClass("Cavalier", 7, ["Horseback", "Mounted"])
PEGASUS_KNIGHT = CharacterClass("Pegasus Knight", 7, ["Flying", "Mounted"])
WYVERN_RIDER = CharacterClass("Wyvern Rider", 7, ["Flying", "Mounted", "Dragon"])
MAGE = CharacterClass("Mage", 5, ["Infantry", "Magic"])
LORD = CharacterClass("Lord", 5, ["Infantry", "Royal"])

# Define a dictionary of predefined classes for easy access
PREDEFINED_CLASSES = {
    "Infantry": INFANTRY,
    "Knight": KNIGHT,
    "Cavalier": CAVALIER,
    "Pegasus Knight": PEGASUS_KNIGHT,
    "Wyvern Rider": WYVERN_RIDER,
    "Mage": MAGE,
    "Lord": LORD
}

def get_class(class_name):
    """
    Get a predefined class by name.
    
    Args:
        class_name (str): Name of the class to get
        
    Returns:
        CharacterClass: The requested class or None if not found
    """
    return PREDEFINED_CLASSES.get(class_name)
