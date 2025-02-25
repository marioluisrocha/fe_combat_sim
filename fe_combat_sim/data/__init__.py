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

# Predefined weapons from Fire Emblem 6 (Binding Blade), 7 (Blazing Blade), and 8 (Sacred Stones)
WEAPONS = {
    # Basic Swords
    "Iron Sword": Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46),
    "Slim Sword": Weapon("Slim Sword", "Sword", might=3, hit=100, crit=5, range=(1, 1), uses=30),
    "Steel Sword": Weapon("Steel Sword", "Sword", might=8, hit=75, crit=0, range=(1, 1), uses=30),
    "Silver Sword": Weapon("Silver Sword", "Sword", might=13, hit=80, crit=0, range=(1, 1), uses=20),
    "Poison Sword": Weapon("Poison Sword", "Sword", might=3, hit=70, crit=0, range=(1, 1), uses=40),
    "Brave Sword": Weapon("Brave Sword", "Sword", might=9, hit=75, crit=0, range=(1, 1), uses=30),
    "Killing Edge": Weapon("Killing Edge", "Sword", might=9, hit=85, crit=30, range=(1, 1), uses=20),
    "Wo Dao": Weapon("Wo Dao", "Sword", might=8, hit=85, crit=35, range=(1, 1), uses=20),
    "Armorslayer": Weapon("Armorslayer", "Sword", might=8, hit=80, crit=0, range=(1, 1), 
                         uses=18, effective_against=["Armored"]),
    "Wyrmslayer": Weapon("Wyrmslayer", "Sword", might=8, hit=75, crit=0, range=(1, 1), 
                         uses=20, effective_against=["Dragon"]),
    "Light Brand": Weapon("Light Brand", "Sword", might=9, hit=70, crit=0, range=(1, 2), uses=25),
    "Wind Sword": Weapon("Wind Sword", "Sword", might=9, hit=70, crit=0, range=(1, 2), uses=40),
    "Lancereaver": Weapon("Lancereaver", "Sword", might=9, hit=75, crit=5, range=(1, 1), uses=15),
    "Runesword": Weapon("Runesword", "Sword", might=12, hit=65, crit=0, range=(1, 2), uses=15),

    # Special Swords (Legendary/Character-specific)
    "Binding Blade": Weapon("Binding Blade", "Sword", might=17, hit=95, crit=0, range=(1, 2), uses=20, 
                           effective_against=["Dragon"]),
    "Durandal": Weapon("Durandal", "Sword", might=17, hit=90, crit=0, range=(1, 1), uses=20),
    "Sol Katti": Weapon("Sol Katti", "Sword", might=13, hit=95, crit=25, range=(1, 1), uses=25),
    "Mani Katti": Weapon("Mani Katti", "Sword", might=8, hit=80, crit=20, range=(1, 1), uses=45),
    "Rapier": Weapon("Rapier", "Sword", might=7, hit=95, crit=10, range=(1, 1), uses=40, 
                    effective_against=["Armored", "Horseback"]),
    "Audhulma": Weapon("Audhulma", "Sword", might=13, hit=85, crit=0, range=(1, 1), uses=25),
    "Sieglinde": Weapon("Sieglinde", "Sword", might=16, hit=90, crit=0, range=(1, 1), uses=25),

    # Basic Lances
    "Iron Lance": Weapon("Iron Lance", "Lance", might=7, hit=80, crit=0, range=(1, 1), uses=45),
    "Slim Lance": Weapon("Slim Lance", "Lance", might=4, hit=85, crit=5, range=(1, 1), uses=30),
    "Steel Lance": Weapon("Steel Lance", "Lance", might=10, hit=70, crit=0, range=(1, 1), uses=30),
    "Silver Lance": Weapon("Silver Lance", "Lance", might=14, hit=75, crit=0, range=(1, 1), uses=20),
    "Poison Lance": Weapon("Poison Lance", "Lance", might=4, hit=65, crit=0, range=(1, 1), uses=40),
    "Brave Lance": Weapon("Brave Lance", "Lance", might=10, hit=70, crit=0, range=(1, 1), uses=30),
    "Killer Lance": Weapon("Killer Lance", "Lance", might=10, hit=75, crit=30, range=(1, 1), uses=20),
    "Horseslayer": Weapon("Horseslayer", "Lance", might=7, hit=70, crit=0, range=(1, 1), 
                         uses=16, effective_against=["Horseback", "Mounted"]),
    "Javelin": Weapon("Javelin", "Lance", might=6, hit=65, crit=0, range=(1, 2), uses=20),
    "Spear": Weapon("Spear", "Lance", might=12, hit=70, crit=5, range=(1, 2), uses=15),
    "Axereaver": Weapon("Axereaver", "Lance", might=10, hit=75, crit=5, range=(1, 1), uses=15),
    "Short Spear": Weapon("Short Spear", "Lance", might=9, hit=60, crit=0, range=(1, 2), uses=18),
    "Knight Killer": Weapon("Knight Killer", "Lance", might=7, hit=70, crit=0, range=(1, 1), 
                           uses=16, effective_against=["Armored"]),

    # Special Lances (Legendary/Character-specific)
    "Maltet": Weapon("Maltet", "Lance", might=16, hit=90, crit=0, range=(1, 1), uses=20, 
                    effective_against=["Dragon"]),
    "Rex Hasta": Weapon("Rex Hasta", "Lance", might=15, hit=85, crit=10, range=(1, 1), uses=25),
    "Reginleif": Weapon("Reginleif", "Lance", might=8, hit=80, crit=0, range=(1, 1), uses=45, 
                       effective_against=["Armored", "Horseback"]),
    "Vidofnir": Weapon("Vidofnir", "Lance", might=15, hit=85, crit=0, range=(1, 1), uses=25),
    "Siegmund": Weapon("Siegmund", "Lance", might=17, hit=80, crit=0, range=(1, 1), uses=25),
    "Gradivus": Weapon("Gradivus", "Lance", might=14, hit=85, crit=0, range=(1, 2), uses=20),

    # Basic Axes
    "Iron Axe": Weapon("Iron Axe", "Axe", might=8, hit=75, crit=0, range=(1, 1), uses=45),
    "Slim Axe": Weapon("Slim Axe", "Axe", might=5, hit=85, crit=5, range=(1, 1), uses=30),
    "Steel Axe": Weapon("Steel Axe", "Axe", might=11, hit=65, crit=0, range=(1, 1), uses=30),
    "Silver Axe": Weapon("Silver Axe", "Axe", might=15, hit=70, crit=0, range=(1, 1), uses=20),
    "Poison Axe": Weapon("Poison Axe", "Axe", might=4, hit=60, crit=0, range=(1, 1), uses=40),
    "Brave Axe": Weapon("Brave Axe", "Axe", might=10, hit=65, crit=0, range=(1, 1), uses=30),
    "Killer Axe": Weapon("Killer Axe", "Axe", might=11, hit=65, crit=30, range=(1, 1), uses=20),
    "Hammer": Weapon("Hammer", "Axe", might=10, hit=55, crit=0, range=(1, 1), 
                    uses=20, effective_against=["Armored"]),
    "Halberd": Weapon("Halberd", "Axe", might=10, hit=60, crit=0, range=(1, 1), 
                     uses=20, effective_against=["Horseback", "Mounted"]),
    "Hand Axe": Weapon("Hand Axe", "Axe", might=7, hit=60, crit=0, range=(1, 2), uses=20),
    "Short Axe": Weapon("Short Axe", "Axe", might=9, hit=55, crit=0, range=(1, 2), uses=15),
    "Tomahawk": Weapon("Tomahawk", "Axe", might=13, hit=65, crit=0, range=(1, 2), uses=15),
    "Swordreaver": Weapon("Swordreaver", "Axe", might=11, hit=65, crit=5, range=(1, 1), uses=15),
    "Devil Axe": Weapon("Devil Axe", "Axe", might=18, hit=55, crit=0, range=(1, 1), uses=20),
    "Swordslayer": Weapon("Swordslayer", "Axe", might=13, hit=80, crit=5, range=(1, 1), uses=20),

    # Special Axes (Legendary/Character-specific)
    "Armads": Weapon("Armads", "Axe", might=18, hit=85, crit=0, range=(1, 1), uses=25),
    "Wolf Beil": Weapon("Wolf Beil", "Axe", might=10, hit=75, crit=5, range=(1, 1), uses=30, 
                       effective_against=["Armored", "Horseback"]),
    "Basilikos": Weapon("Basilikos", "Axe", might=16, hit=75, crit=15, range=(1, 1), uses=25),
    "Garm": Weapon("Garm", "Axe", might=16, hit=75, crit=0, range=(1, 1), uses=25),

    # Basic Bows
    "Iron Bow": Weapon("Iron Bow", "Bow", might=6, hit=85, crit=0, range=(2, 2), 
                      uses=45, effective_against=["Flying"]),
    "Steel Bow": Weapon("Steel Bow", "Bow", might=9, hit=70, crit=0, range=(2, 2), 
                       uses=30, effective_against=["Flying"]),
    "Silver Bow": Weapon("Silver Bow", "Bow", might=13, hit=75, crit=0, range=(2, 2), 
                        uses=20, effective_against=["Flying"]),
    "Poison Bow": Weapon("Poison Bow", "Bow", might=4, hit=65, crit=0, range=(2, 2), 
                        uses=40, effective_against=["Flying"]),
    "Killer Bow": Weapon("Killer Bow", "Bow", might=9, hit=75, crit=30, range=(2, 2), 
                        uses=20, effective_against=["Flying"]),
    "Brave Bow": Weapon("Brave Bow", "Bow", might=10, hit=70, crit=0, range=(2, 2), 
                       uses=30, effective_against=["Flying"]),
    "Short Bow": Weapon("Short Bow", "Bow", might=5, hit=85, crit=10, range=(2, 2), 
                       uses=22, effective_against=["Flying"]),
    "Longbow": Weapon("Longbow", "Bow", might=5, hit=65, crit=0, range=(2, 3), 
                     uses=20, effective_against=["Flying"]),

    # Special Bows (Legendary/Character-specific)
    "Mulagir": Weapon("Mulagir", "Bow", might=14, hit=85, crit=0, range=(2, 2), 
                     uses=20, effective_against=["Flying"]),
    "Rienfleche": Weapon("Rienfleche", "Bow", might=15, hit=80, crit=10, range=(2, 2), 
                        uses=25, effective_against=["Flying"]),
    "Nidhogg": Weapon("Nidhogg", "Bow", might=14, hit=80, crit=0, range=(2, 2), 
                     uses=30, effective_against=["Flying"]),

    # Anima Magic (Tomes)
    "Fire": Weapon("Fire", "Tome", might=5, hit=90, crit=0, range=(1, 2), uses=40),
    "Thunder": Weapon("Thunder", "Tome", might=8, hit=80, crit=5, range=(1, 2), uses=35),
    "Elfire": Weapon("Elfire", "Tome", might=10, hit=85, crit=0, range=(1, 2), uses=30),
    "Wind": Weapon("Wind", "Tome", might=3, hit=100, crit=0, range=(1, 2), 
                  uses=40, effective_against=["Flying"]),
    "Aircalibur": Weapon("Aircalibur", "Tome", might=8, hit=85, crit=5, range=(1, 2), 
                        uses=25, effective_against=["Flying"]),
    "Excalibur": Weapon("Excalibur", "Tome", might=12, hit=90, crit=10, range=(1, 2), 
                       uses=25, effective_against=["Flying"]),
    "Bolting": Weapon("Bolting", "Tome", might=12, hit=60, crit=0, range=(3, 10), uses=5),
    "Fimbulvetr": Weapon("Fimbulvetr", "Tome", might=13, hit=80, crit=0, range=(1, 2), uses=20),
    "Elthunder": Weapon("Elthunder", "Tome", might=10, hit=80, crit=5, range=(1, 2), uses=20),
    "Bolganone": Weapon("Bolganone", "Tome", might=15, hit=75, crit=0, range=(1, 2), uses=15),
    "Tornado": Weapon("Tornado", "Tome", might=12, hit=90, crit=5, range=(1, 2), uses=20),
    
    # Light Magic (Tomes)
    "Lightning": Weapon("Lightning", "Tome", might=4, hit=95, crit=5, range=(1, 2), uses=35),
    "Shine": Weapon("Shine", "Tome", might=6, hit=90, crit=8, range=(1, 2), uses=30),
    "Divine": Weapon("Divine", "Tome", might=8, hit=85, crit=10, range=(1, 2), uses=25),
    "Purge": Weapon("Purge", "Tome", might=10, hit=70, crit=5, range=(3, 10), uses=5),
    "Aura": Weapon("Aura", "Tome", might=12, hit=85, crit=15, range=(1, 2), uses=20),
    "Aureola": Weapon("Aureola", "Tome", might=15, hit=85, crit=5, range=(1, 2), uses=20, 
                      effective_against=["Dragon"]),
    "Ivaldi": Weapon("Ivaldi", "Tome", might=17, hit=90, crit=5, range=(1, 2), uses=25),
    
    # Dark Magic (Tomes)
    "Flux": Weapon("Flux", "Tome", might=7, hit=80, crit=0, range=(1, 2), uses=45),
    "Luna": Weapon("Luna", "Tome", might=0, hit=95, crit=20, range=(1, 2), uses=30),
    "Nosferatu": Weapon("Nosferatu", "Tome", might=10, hit=70, crit=0, range=(1, 2), uses=20),
    "Eclipse": Weapon("Eclipse", "Tome", might=0, hit=60, crit=0, range=(3, 10), uses=5),
    "Fenrir": Weapon("Fenrir", "Tome", might=15, hit=70, crit=0, range=(1, 2), uses=20),
    "Gespenst": Weapon("Gespenst", "Tome", might=18, hit=80, crit=0, range=(1, 2), uses=20),
    "Gleipnir": Weapon("Gleipnir", "Tome", might=15, hit=80, crit=0, range=(1, 2), uses=25),
    "Apocalypse": Weapon("Apocalypse", "Tome", might=20, hit=75, crit=5, range=(1, 2), uses=20),
    
    # Staves (for healing and utility)
    "Heal": Weapon("Heal", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=30),
    "Mend": Weapon("Mend", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=20),
    "Recover": Weapon("Recover", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=15),
    "Physic": Weapon("Physic", "Staff", might=0, hit=100, crit=0, range=(1, 10), uses=15),
    "Fortify": Weapon("Fortify", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=8),
    "Restore": Weapon("Restore", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=10),
    "Silence": Weapon("Silence", "Staff", might=0, hit=70, crit=0, range=(1, 10), uses=3),
    "Sleep": Weapon("Sleep", "Staff", might=0, hit=65, crit=0, range=(1, 10), uses=2),
    "Berserk": Weapon("Berserk", "Staff", might=0, hit=60, crit=0, range=(1, 10), uses=2),
    "Warp": Weapon("Warp", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=5),
    "Rescue": Weapon("Rescue", "Staff", might=0, hit=100, crit=0, range=(1, 10), uses=3),
    "Barrier": Weapon("Barrier", "Staff", might=0, hit=100, crit=0, range=(1, 1), uses=15),
    
    # Other special weapons
    "Dragonstone": Weapon("Dragonstone", "Other", might=12, hit=95, crit=0, range=(1, 1), uses=50),
    "Runesword": Weapon("Runesword", "Sword", might=12, hit=65, crit=0, range=(1, 2), uses=15),
    "Spear": Weapon("Spear", "Lance", might=12, hit=70, crit=5, range=(1, 2), uses=15),
    "Shamshir": Weapon("Shamshir", "Sword", might=8, hit=80, crit=35, range=(1, 1), uses=20),
    "Naglfar": Weapon("Naglfar", "Tome", might=18, hit=85, crit=0, range=(1, 2), uses=25),
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
