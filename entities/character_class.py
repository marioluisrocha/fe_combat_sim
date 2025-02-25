"""
Character class definitions for Fire Emblem Combat Simulator.
Includes all classes from Fire Emblem 6 (Binding Blade), 7 (Blazing Blade), and 8 (Sacred Stones).
"""

class CharacterClass:
    """Class representing a character's class/job in the game."""
    
    def __init__(self, name, movement=5, class_types=None, promoted=False, weapons=None, description=None):
        """
        Initialize a character class.
        
        Args:
            name (str): Name of the class (e.g., "Knight", "Pegasus Knight")
            movement (int): Base movement range
            class_types (list): List of class types for weakness/resistance calculation
            promoted (bool): Whether this is a promoted class
            weapons (list): Weapon types this class can use
            description (str): Brief description of the class
        """
        self.name = name
        self.movement = movement
        self.class_types = class_types or []
        self.promoted = promoted
        self.weapons = weapons or []
        self.description = description
        
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
        weapons_str = ", ".join(self.weapons) if self.weapons else "None"
        return (f"CharacterClass(name='{self.name}', movement={self.movement}, "
                f"class_types=[{types_str}], promoted={self.promoted}, weapons=[{weapons_str}])")


# --- UNPROMOTED CLASSES ---

# Lords
LORD_ELIWOOD = CharacterClass(
    name="Lord (Eliwood)", 
    movement=5, 
    class_types=["Infantry", "Royal"],
    promoted=False,
    weapons=["Sword"],
    description="Noble protagonist from Pherae (FE7)"
)

LORD_HECTOR = CharacterClass(
    name="Lord (Hector)", 
    movement=5, 
    class_types=["Infantry", "Royal"],
    promoted=False,
    weapons=["Axe"],
    description="Brash lord from Ostia (FE7)"
)

LORD_LYN = CharacterClass(
    name="Lord (Lyn)", 
    movement=6, 
    class_types=["Infantry", "Royal"],
    promoted=False,
    weapons=["Sword"],
    description="Swift nomad of Sacae (FE7)"
)

LORD_ROY = CharacterClass(
    name="Lord (Roy)", 
    movement=5, 
    class_types=["Infantry", "Royal"],
    promoted=False,
    weapons=["Sword"],
    description="Young lord of Pherae (FE6)"
)

LORD_EIRIKA = CharacterClass(
    name="Lord (Eirika)", 
    movement=5, 
    class_types=["Infantry", "Royal"],
    promoted=False,
    weapons=["Sword"],
    description="Princess of Renais (FE8)"
)

LORD_EPHRAIM = CharacterClass(
    name="Lord (Ephraim)", 
    movement=5, 
    class_types=["Infantry", "Royal"],
    promoted=False,
    weapons=["Lance"],
    description="Prince of Renais (FE8)"
)

# Cavaliers
CAVALIER = CharacterClass(
    name="Cavalier", 
    movement=7, 
    class_types=["Horseback", "Mounted"],
    promoted=False,
    weapons=["Sword", "Lance"],
    description="Mounted knights with balanced stats"
)

NOMAD = CharacterClass(
    name="Nomad", 
    movement=7, 
    class_types=["Horseback", "Mounted"],
    promoted=False,
    weapons=["Bow"],
    description="Mounted archers from the plains of Sacae"
)

TROUBADOUR = CharacterClass(
    name="Troubadour", 
    movement=7, 
    class_types=["Horseback", "Mounted"],
    promoted=False,
    weapons=["Staff"],
    description="Mounted healers"
)

# Knights and Fighters
KNIGHT = CharacterClass(
    name="Knight", 
    movement=4, 
    class_types=["Armored", "Infantry"],
    promoted=False,
    weapons=["Lance"],
    description="Heavily armored, slow-moving defensive units"
)

FIGHTER = CharacterClass(
    name="Fighter", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Axe"],
    description="Offensive axe users with high strength"
)

MERCENARY = CharacterClass(
    name="Mercenary", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Sword"],
    description="Balanced sword-wielding soldiers for hire"
)

MYRMIDON = CharacterClass(
    name="Myrmidon", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Sword"],
    description="Fast sword users with high skill and critical hit rate"
)

SOLDIER = CharacterClass(
    name="Soldier", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Lance"],
    description="Basic lance-wielding infantry units"
)

ARCHER = CharacterClass(
    name="Archer", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Bow"],
    description="Infantry bow users that attack from a distance"
)

PIRATE = CharacterClass(
    name="Pirate", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Axe"],
    description="Seafaring axe users who can cross water terrain"
)

BRIGAND = CharacterClass(
    name="Brigand", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Axe"],
    description="Mountain-dwelling bandits who can traverse peaks"
)

# Flying Units
PEGASUS_KNIGHT = CharacterClass(
    name="Pegasus Knight", 
    movement=7, 
    class_types=["Flying", "Mounted"],
    promoted=False,
    weapons=["Lance"],
    description="Flying lance users with high speed but vulnerable to arrows"
)

WYVERN_RIDER = CharacterClass(
    name="Wyvern Rider", 
    movement=7, 
    class_types=["Flying", "Mounted", "Dragon"],
    promoted=False,
    weapons=["Lance"],
    description="Flying dragon riders with high defense but weak to arrows and dragon-slaying weapons"
)

# Magic Users
MAGE = CharacterClass(
    name="Mage", 
    movement=5, 
    class_types=["Infantry", "Magic"],
    promoted=False,
    weapons=["Tome"],
    description="Practitioners of anima magic (fire, thunder, wind)"
)

MONK = CharacterClass(
    name="Monk", 
    movement=5, 
    class_types=["Infantry", "Magic"],
    promoted=False,
    weapons=["Tome"],
    description="Male light magic users"
)

CLERIC = CharacterClass(
    name="Cleric", 
    movement=5, 
    class_types=["Infantry", "Magic"],
    promoted=False,
    weapons=["Staff"],
    description="Female staff users focused on healing"
)

PRIEST = CharacterClass(
    name="Priest", 
    movement=5, 
    class_types=["Infantry", "Magic"],
    promoted=False,
    weapons=["Staff"],
    description="Male staff users focused on healing"
)

SHAMAN = CharacterClass(
    name="Shaman", 
    movement=5, 
    class_types=["Infantry", "Magic"],
    promoted=False,
    weapons=["Tome"],
    description="Dark magic practitioners"
)

# Thieves and Dancers
THIEF = CharacterClass(
    name="Thief", 
    movement=6, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Sword"],
    description="Fast units that can pick locks and steal items"
)

DANCER = CharacterClass(
    name="Dancer", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=[],
    description="Support units that allow allies to take another action"
)

BARD = CharacterClass(
    name="Bard", 
    movement=5, 
    class_types=["Infantry"],
    promoted=False,
    weapons=[],
    description="Male support units that allow allies to take another action"
)

# Special Classes
MANAKETE = CharacterClass(
    name="Manakete", 
    movement=5, 
    class_types=["Infantry", "Dragon"],
    promoted=False,
    weapons=["Dragonstone"],
    description="Human-dragon shapeshifters that use dragonstones to transform"
)

JOURNEYMAN = CharacterClass(
    name="Journeyman", 
    movement=4, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Axe"],
    description="Trainee class that can promote to Fighter, Pirate, or Warrior (FE8)"
)

RECRUIT = CharacterClass(
    name="Recruit", 
    movement=4, 
    class_types=["Infantry"],
    promoted=False,
    weapons=["Lance"],
    description="Trainee class that can promote to Cavalier, Knight, or Soldier (FE8)"
)

PUPIL = CharacterClass(
    name="Pupil", 
    movement=4, 
    class_types=["Infantry", "Magic"],
    promoted=False,
    weapons=["Tome"],
    description="Trainee class that can promote to Mage, Shaman, or Monk (FE8)"
)

# --- PROMOTED CLASSES ---

# Lord Promotions
KNIGHT_LORD = CharacterClass(
    name="Knight Lord", 
    movement=7, 
    class_types=["Horseback", "Mounted", "Royal"],
    promoted=True,
    weapons=["Sword", "Lance"],
    description="Eliwood's promoted class (FE7)"
)

GREAT_LORD_HECTOR = CharacterClass(
    name="Great Lord (Hector)", 
    movement=5, 
    class_types=["Infantry", "Royal"],
    promoted=True,
    weapons=["Sword", "Axe"],
    description="Hector's promoted class (FE7)"
)

BLADE_LORD = CharacterClass(
    name="Blade Lord", 
    movement=6, 
    class_types=["Infantry", "Royal"],
    promoted=True,
    weapons=["Sword", "Bow"],
    description="Lyn's promoted class (FE7)"
)

MASTER_LORD = CharacterClass(
    name="Master Lord", 
    movement=6, 
    class_types=["Infantry", "Royal"],
    promoted=True,
    weapons=["Sword"],
    description="Roy's promoted class (FE6)"
)

GREAT_LORD_EIRIKA = CharacterClass(
    name="Great Lord (Eirika)", 
    movement=7, 
    class_types=["Infantry", "Royal"],
    promoted=True,
    weapons=["Sword"],
    description="Eirika's promoted class (FE8)"
)

GREAT_LORD_EPHRAIM = CharacterClass(
    name="Great Lord (Ephraim)", 
    movement=7, 
    class_types=["Infantry", "Royal"],
    promoted=True,
    weapons=["Lance"],
    description="Ephraim's promoted class (FE8)"
)

# Cavalier Promotions
PALADIN = CharacterClass(
    name="Paladin", 
    movement=8, 
    class_types=["Horseback", "Mounted"],
    promoted=True,
    weapons=["Sword", "Lance", "Axe"],
    description="Promoted cavaliers with balanced stats and weaponry"
)

NOMAD_TROOPER = CharacterClass(
    name="Nomad Trooper", 
    movement=7, 
    class_types=["Horseback", "Mounted"],
    promoted=True,
    weapons=["Sword", "Bow"],
    description="Promoted nomads who can use swords"
)

VALKYRIE = CharacterClass(
    name="Valkyrie", 
    movement=8, 
    class_types=["Horseback", "Mounted", "Magic"],
    promoted=True,
    weapons=["Tome", "Staff"],
    description="Promoted troubadours who can use magic and staves"
)

# Knight and Fighter Promotions
GENERAL = CharacterClass(
    name="General", 
    movement=5, 
    class_types=["Armored", "Infantry"],
    promoted=True,
    weapons=["Sword", "Lance", "Axe"],
    description="Promoted knights with high defense and varied weapon options"
)

WARRIOR = CharacterClass(
    name="Warrior", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Axe", "Bow"],
    description="Promoted fighters who can use axes and bows"
)

HERO = CharacterClass(
    name="Hero", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Sword", "Axe"],
    description="Promoted mercenaries with balanced stats and weapon options"
)

SWORDMASTER = CharacterClass(
    name="Swordmaster", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Sword"],
    description="Promoted myrmidons with high speed and critical hit rates"
)

HALBERDIER = CharacterClass(
    name="Halberdier", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Lance"],
    description="Promoted soldiers with enhanced lance skills"
)

SNIPER = CharacterClass(
    name="Sniper", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Bow"],
    description="Promoted archers with increased range and accuracy"
)

BERSERKER = CharacterClass(
    name="Berserker", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Axe"],
    description="Promoted pirates with extremely high critical hit rates"
)

# Flying Unit Promotions
FALCON_KNIGHT = CharacterClass(
    name="Falcon Knight", 
    movement=8, 
    class_types=["Flying", "Mounted"],
    promoted=True,
    weapons=["Sword", "Lance"],
    description="Promoted pegasus knights with access to swords"
)

WYVERN_LORD = CharacterClass(
    name="Wyvern Lord", 
    movement=8, 
    class_types=["Flying", "Mounted", "Dragon"],
    promoted=True,
    weapons=["Lance", "Sword"],
    description="Promoted wyvern riders with improved stats and sword access"
)

WYVERN_KNIGHT = CharacterClass(
    name="Wyvern Knight", 
    movement=8, 
    class_types=["Flying", "Mounted", "Dragon"],
    promoted=True,
    weapons=["Lance"],
    description="Alternative promotion for wyvern riders with Pierce skill (FE8)"
)

# Magic User Promotions
SAGE = CharacterClass(
    name="Sage", 
    movement=6, 
    class_types=["Infantry", "Magic"],
    promoted=True,
    weapons=["Tome", "Staff"],
    description="Promoted mages who can use staves and all anima magic"
)

BISHOP = CharacterClass(
    name="Bishop", 
    movement=6, 
    class_types=["Infantry", "Magic"],
    promoted=True,
    weapons=["Tome", "Staff"],
    description="Promoted monks/clerics with enhanced light magic and healing"
)

DRUID = CharacterClass(
    name="Druid", 
    movement=6, 
    class_types=["Infantry", "Magic"],
    promoted=True,
    weapons=["Tome", "Staff"],
    description="Promoted shamans with enhanced dark magic and staff access"
)

# Thief Promotions
ASSASSIN = CharacterClass(
    name="Assassin", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Sword"],
    description="Promoted thieves with the Silencer skill for instant kills"
)

ROGUE = CharacterClass(
    name="Rogue", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Sword"],
    description="Promoted thieves with enhanced stealing and lock-picking abilities (FE8)"
)

# Special Promotions
SUMMONER = CharacterClass(
    name="Summoner", 
    movement=6, 
    class_types=["Infantry", "Magic"],
    promoted=True,
    weapons=["Tome", "Staff"],
    description="Alternative promotion for shamans who can summon phantoms (FE8)"
)

RANGER = CharacterClass(
    name="Ranger", 
    movement=7, 
    class_types=["Horseback", "Mounted"],
    promoted=True,
    weapons=["Sword", "Bow"],
    description="Alternative promotion for cavaliers with bow access (FE8)"
)

SUPER_TRAINEE = CharacterClass(
    name="Super Trainee", 
    movement=6, 
    class_types=["Infantry"],
    promoted=True,
    weapons=["Sword", "Lance", "Axe"],
    description="Special third-tier promotion for trainees (FE8)"
)

GREAT_KNIGHT = CharacterClass(
    name="Great Knight", 
    movement=6, 
    class_types=["Horseback", "Mounted", "Armored"],
    promoted=True,
    weapons=["Sword", "Lance", "Axe"],
    description="Heavily armored mounted knights (FE8)"
)

MAGIC_KNIGHT = CharacterClass(
    name="Magic Knight", 
    movement=7, 
    class_types=["Horseback", "Mounted", "Magic"],
    promoted=True,
    weapons=["Sword", "Tome"],
    description="Mounted units that use swords and magic (FE8)"
)

# FE8 Sacred Stones Unique Classes
NECROMANCER = CharacterClass(
    name="Necromancer", 
    movement=6, 
    class_types=["Infantry", "Magic"],
    promoted=True,
    weapons=["Tome", "Staff"],
    description="Unique class used by Lyon in FE8, powerful dark magic user"
)

DEMON_KING = CharacterClass(
    name="Demon King", 
    movement=6, 
    class_types=["Armored", "Magic", "Monster"],
    promoted=True,
    weapons=["Tome"],
    description="Final boss class in FE8 with extremely high stats"
)

# Monster Classes from FE8
REVENANT = CharacterClass(
    name="Revenant", 
    movement=4, 
    class_types=["Monster"],
    promoted=False,
    weapons=["Monster"],
    description="Basic zombie monsters with low stats"
)

ENTOMBED = CharacterClass(
    name="Entombed", 
    movement=5, 
    class_types=["Monster"],
    promoted=True,
    weapons=["Monster"],
    description="Promoted zombies with improved stats"
)

BONEWALKER = CharacterClass(
    name="Bonewalker", 
    movement=5, 
    class_types=["Monster"],
    promoted=False,
    weapons=["Sword", "Lance", "Bow"],
    description="Skeletal monsters that use conventional weapons"
)

WIGHT = CharacterClass(
    name="Wight", 
    movement=6, 
    class_types=["Monster"],
    promoted=True,
    weapons=["Sword", "Lance", "Bow"],
    description="Promoted bonewalkers with higher stats"
)

MOGALL = CharacterClass(
    name="Mogall", 
    movement=5, 
    class_types=["Monster", "Flying", "Magic"],
    promoted=False,
    weapons=["Monster"],
    description="Flying eye monsters that use dark magic"
)

ARCH_MOGALL = CharacterClass(
    name="Arch Mogall", 
    movement=6, 
    class_types=["Monster", "Flying", "Magic"],
    promoted=True,
    weapons=["Monster"],
    description="Promoted mogalls with stronger magic"
)

GORGON = CharacterClass(
    name="Gorgon", 
    movement=5, 
    class_types=["Monster", "Magic"],
    promoted=False,
    weapons=["Monster"],
    description="Snake-woman monsters with stone gaze ability"
)

# Special NPC Classes
BAEL = CharacterClass(
    name="Bael", 
    movement=6, 
    class_types=["Monster"],
    promoted=False,
    weapons=["Monster"],
    description="Giant spider monsters"
)

ELDER_BAEL = CharacterClass(
    name="Elder Bael", 
    movement=6, 
    class_types=["Monster"],
    promoted=True,
    weapons=["Monster"],
    description="Promoted giant spiders"
)

MAUTHE_DOOG = CharacterClass(
    name="Mauthe Doog", 
    movement=7, 
    class_types=["Monster"],
    promoted=False,
    weapons=["Monster"],
    description="Demonic dog monsters"
)

GWYLLGI = CharacterClass(
    name="Gwyllgi", 
    movement=7, 
    class_types=["Monster"],
    promoted=True,
    weapons=["Monster"],
    description="Promoted demonic dogs with fire breath"
)

TARVOS = CharacterClass(
    name="Tarvos", 
    movement=6, 
    class_types=["Monster"],
    promoted=False,
    weapons=["Monster"],
    description="Minotaur-like axe-wielding monsters"
)

MAELDUIN = CharacterClass(
    name="Maelduin", 
    movement=6, 
    class_types=["Monster"],
    promoted=True,
    weapons=["Monster"],
    description="Promoted minotaurs with higher stats"
)

GARGOYLE = CharacterClass(
    name="Gargoyle", 
    movement=7, 
    class_types=["Monster", "Flying"],
    promoted=False,
    weapons=["Monster"],
    description="Flying stone monsters"
)

DEATHGOYLE = CharacterClass(
    name="Deathgoyle", 
    movement=7, 
    class_types=["Monster", "Flying"],
    promoted=True,
    weapons=["Monster"],
    description="Promoted gargoyles with poisoned weapons"
)

# Create dictionary of all classes
GBA_CLASSES = {
    # Unpromoted
    "Lord (Eliwood)": LORD_ELIWOOD,
    "Lord (Hector)": LORD_HECTOR,
    "Lord (Lyn)": LORD_LYN,
    "Lord (Roy)": LORD_ROY,
    "Lord (Eirika)": LORD_EIRIKA,
    "Lord (Ephraim)": LORD_EPHRAIM,
    "Cavalier": CAVALIER,
    "Knight": KNIGHT,
    "Fighter": FIGHTER,
    "Mercenary": MERCENARY,
    "Myrmidon": MYRMIDON,
    "Soldier": SOLDIER,
    "Archer": ARCHER,
    "Nomad": NOMAD,
    "Troubadour": TROUBADOUR,
    "Pegasus Knight": PEGASUS_KNIGHT,
    "Wyvern Rider": WYVERN_RIDER,
    "Mage": MAGE,
    "Monk": MONK,
    "Cleric": CLERIC,
    "Priest": PRIEST,
    "Shaman": SHAMAN,
    "Thief": THIEF,
    "Pirate": PIRATE,
    "Brigand": BRIGAND,
    "Dancer": DANCER,
    "Bard": BARD,
    "Manakete": MANAKETE,
    "Journeyman": JOURNEYMAN,
    "Recruit": RECRUIT,
    "Pupil": PUPIL,
    
    # Promoted
    "Knight Lord": KNIGHT_LORD,
    "Great Lord (Hector)": GREAT_LORD_HECTOR,
    "Blade Lord": BLADE_LORD,
    "Master Lord": MASTER_LORD,
    "Great Lord (Eirika)": GREAT_LORD_EIRIKA,
    "Great Lord (Ephraim)": GREAT_LORD_EPHRAIM,
    "Paladin": PALADIN,
    "General": GENERAL,
    "Warrior": WARRIOR,
    "Hero": HERO,
    "Swordmaster": SWORDMASTER,
    "Halberdier": HALBERDIER,
    "Sniper": SNIPER,
    "Nomad Trooper": NOMAD_TROOPER,
    "Valkyrie": VALKYRIE,
    "Falcon Knight": FALCON_KNIGHT,
    "Wyvern Lord": WYVERN_LORD,
    "Wyvern Knight": WYVERN_KNIGHT,
    "Sage": SAGE,
    "Bishop": BISHOP,
    "Druid": DRUID,
    "Assassin": ASSASSIN,
    "Rogue": ROGUE,
    "Berserker": BERSERKER,
    "Summoner": SUMMONER,
    "Ranger": RANGER,
    "Great Knight": GREAT_KNIGHT,
    "Magic Knight": MAGIC_KNIGHT,
    "Necromancer": NECROMANCER,
    
    # Monster Classes (FE8)
    "Revenant": REVENANT,
    "Entombed": ENTOMBED,
    "Bonewalker": BONEWALKER,
    "Wight": WIGHT,
    "Mogall": MOGALL,
    "Arch Mogall": ARCH_MOGALL,
    "Gorgon": GORGON,
    "Bael": BAEL,
    "Elder Bael": ELDER_BAEL,
    "Mauthe Doog": MAUTHE_DOOG,
    "Gwyllgi": GWYLLGI,
    "Tarvos": TARVOS,
    "Maelduin": MAELDUIN,
    "Gargoyle": GARGOYLE,
    "Deathgoyle": DEATHGOYLE,
    "Demon King": DEMON_KING,
}

def get_class(class_name):
    """
    Get a predefined class by name.
    
    Args:
        class_name (str): Name of the class to get
        
    Returns:
        CharacterClass: The requested class or None if not found
    """
    return GBA_CLASSES.get(class_name)

# For backward compatibility
PREDEFINED_CLASSES = GBA_CLASSES.copy()
INFANTRY = CharacterClass("Infantry", 5, ["Infantry"])
