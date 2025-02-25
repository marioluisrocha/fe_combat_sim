"""
Data module for Fire Emblem Combat Simulator.
Includes predefined weapons, character templates, etc.
"""

from fe_combat_sim.entities.weapon import Weapon
from fe_combat_sim.entities.character import Character
from fe_combat_sim.entities.character_class import (
    CharacterClass, INFANTRY, KNIGHT, CAVALIER, 
    PEGASUS_KNIGHT, WYVERN_RIDER, MAGE, LORD
)

# Predefined weapons
WEAPONS = {
    # Swords
    "Iron Sword": Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46),
    "Steel Sword": Weapon("Steel Sword", "Sword", might=8, hit=75, crit=0, range=(1, 1), uses=30),
    "Silver Sword": Weapon("Silver Sword", "Sword", might=13, hit=80, crit=0, range=(1, 1), uses=20),
    "Killing Edge": Weapon("Killing Edge", "Sword", might=9, hit=85, crit=30, range=(1, 1), uses=20),
    "Armorslayer": Weapon("Armorslayer", "Sword", might=8, hit=80, crit=0, range=(1, 1), 
                          uses=18, effective_against=["Armored"]),
    "Wyrmslayer": Weapon("Wyrmslayer", "Sword", might=8, hit=75, crit=0, range=(1, 1), 
                          uses=20, effective_against=["Dragon"]),
    
    # Lances
    "Iron Lance": Weapon("Iron Lance", "Lance", might=7, hit=80, crit=0, range=(1, 1), uses=45),
    "Steel Lance": Weapon("Steel Lance", "Lance", might=10, hit=70, crit=0, range=(1, 1), uses=30),
    "Silver Lance": Weapon("Silver Lance", "Lance", might=14, hit=75, crit=0, range=(1, 1), uses=20),
    "Killer Lance": Weapon("Killer Lance", "Lance", might=10, hit=75, crit=30, range=(1, 1), uses=20),
    "Horseslayer": Weapon("Horseslayer", "Lance", might=7, hit=70, crit=0, range=(1, 1), 
                          uses=16, effective_against=["Horseback", "Mounted"]),
    "Javelin": Weapon("Javelin", "Lance", might=6, hit=65, crit=0, range=(1, 2), uses=20),
    
    # Axes
    "Iron Axe": Weapon("Iron Axe", "Axe", might=8, hit=75, crit=0, range=(1, 1), uses=45),
    "Steel Axe": Weapon("Steel Axe", "Axe", might=11, hit=65, crit=0, range=(1, 1), uses=30),
    "Silver Axe": Weapon("Silver Axe", "Axe", might=15, hit=70, crit=0, range=(1, 1), uses=20),
    "Killer Axe": Weapon("Killer Axe", "Axe", might=11, hit=65, crit=30, range=(1, 1), uses=20),
    "Hammer": Weapon("Hammer", "Axe", might=10, hit=55, crit=0, range=(1, 1), 
                     uses=16, effective_against=["Armored"]),
    "Hand Axe": Weapon("Hand Axe", "Axe", might=7, hit=60, crit=0, range=(1, 2), uses=20),
    
    # Bows
    "Iron Bow": Weapon("Iron Bow", "Bow", might=6, hit=85, crit=0, range=(2, 2), 
                       uses=45, effective_against=["Flying"]),
    "Steel Bow": Weapon("Steel Bow", "Bow", might=9, hit=70, crit=0, range=(2, 2), 
                        uses=30, effective_against=["Flying"]),
    "Silver Bow": Weapon("Silver Bow", "Bow", might=13, hit=75, crit=0, range=(2, 2), 
                         uses=20, effective_against=["Flying"]),
    "Killer Bow": Weapon("Killer Bow", "Bow", might=7, hit=85, crit=30, range=(2, 2), 
                         uses=20, effective_against=["Flying"]),
    "Longbow": Weapon("Longbow", "Bow", might=5, hit=65, crit=0, range=(2, 3), 
                      uses=20, effective_against=["Flying"]),
    
    # Tomes
    "Fire": Weapon("Fire", "Tome", might=5, hit=90, crit=0, range=(1, 2), uses=40),
    "Thunder": Weapon("Thunder", "Tome", might=8, hit=80, crit=5, range=(1, 2), uses=35),
    "Wind": Weapon("Wind", "Tome", might=3, hit=100, crit=0, range=(1, 2), 
                   uses=40, effective_against=["Flying"]),
    "Flux": Weapon("Flux", "Tome", might=7, hit=80, crit=0, range=(1, 2), uses=45),
    
    # Staves
    "Heal": Weapon("Heal", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=30),
    "Mend": Weapon("Mend", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=20),
    "Physic": Weapon("Physic", "Staff", might=0, hit=100, crit=0, range=(1, 10), uses=15),
}

# Character templates with reasonable stat distributions
CHARACTER_TEMPLATES = {
    "Lord": {
        "class": LORD,
        "stats": {"hp": 20, "str": 5, "mag": 1, "skl": 7, "spd": 7, "lck": 7, "def": 5, "res": 1},
        "growth_rates": {"hp": 0.7, "str": 0.45, "mag": 0.15, "skl": 0.5, "spd": 0.5, "lck": 0.5, "def": 0.3, "res": 0.25}
    },
    "Cavalier": {
        "class": CAVALIER,
        "stats": {"hp": 20, "str": 6, "mag": 0, "skl": 5, "spd": 5, "lck": 3, "def": 7, "res": 0},
        "growth_rates": {"hp": 0.8, "str": 0.5, "mag": 0.0, "skl": 0.4, "spd": 0.35, "lck": 0.25, "def": 0.45, "res": 0.2}
    },
    "Knight": {
        "class": KNIGHT,
        "stats": {"hp": 23, "str": 8, "mag": 0, "skl": 4, "spd": 1, "lck": 2, "def": 11, "res": 0},
        "growth_rates": {"hp": 0.9, "str": 0.5, "mag": 0.0, "skl": 0.35, "spd": 0.2, "lck": 0.2, "def": 0.6, "res": 0.15}
    },
    "Pegasus Knight": {
        "class": PEGASUS_KNIGHT,
        "stats": {"hp": 17, "str": 4, "mag": 2, "skl": 6, "spd": 9, "lck": 6, "def": 4, "res": 5},
        "growth_rates": {"hp": 0.6, "str": 0.35, "mag": 0.2, "skl": 0.5, "spd": 0.6, "lck": 0.5, "def": 0.2, "res": 0.5}
    },
    "Wyvern Rider": {
        "class": WYVERN_RIDER,
        "stats": {"hp": 22, "str": 7, "mag": 0, "skl": 5, "spd": 6, "lck": 2, "def": 9, "res": 0},
        "growth_rates": {"hp": 0.8, "str": 0.55, "mag": 0.0, "skl": 0.4, "spd": 0.4, "lck": 0.2, "def": 0.5, "res": 0.1}
    },
    "Mage": {
        "class": MAGE,
        "stats": {"hp": 16, "str": 1, "mag": 5, "skl": 4, "spd": 5, "lck": 4, "def": 2, "res": 5},
        "growth_rates": {"hp": 0.55, "str": 0.1, "mag": 0.6, "skl": 0.4, "spd": 0.45, "lck": 0.4, "def": 0.15, "res": 0.5}
    },
}

def get_weapon(name):
    """Get a predefined weapon by name."""
    return WEAPONS.get(name)

def create_character_from_template(name, template_name, level=1, weapon_name=None):
    """
    Create a character from a template.
    
    Args:
        name (str): Character name
        template_name (str): Template name
        level (int): Character level
        weapon_name (str, optional): Name of the weapon to equip
        
    Returns:
        Character: Created character
    """
    from fe_combat_sim.utils.stats import generate_random_stats
    
    template = CHARACTER_TEMPLATES.get(template_name)
    if not template:
        raise ValueError(f"Template '{template_name}' not found")
    
    # Calculate stats for the character's level
    if level > 1:
        stats = generate_random_stats(
            template["stats"],
            template["growth_rates"],
            level - 1
        )
    else:
        stats = template["stats"].copy()
    
    # Get weapon if specified
    weapon = get_weapon(weapon_name) if weapon_name else None
    
    # Create character
    return Character(name, template["class"], stats, weapon)
