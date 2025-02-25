"""
Entity modules for Fire Emblem Combat Simulator.
Includes character classes, weapons, and items.
"""

# Import all entity classes for easier access
from fe_combat_sim.entities.character import Character
from fe_combat_sim.entities.weapon import Weapon
from fe_combat_sim.entities.character_class import (
    CharacterClass,
    GBA_CLASSES,
    get_class, 
    PREDEFINED_CLASSES
)

# Import basic classes from separate module to avoid circular imports
from fe_combat_sim.entities.basic_classes import (
    INFANTRY, KNIGHT, CAVALIER, PEGASUS_KNIGHT,
    WYVERN_RIDER, MAGE, LORD
)
