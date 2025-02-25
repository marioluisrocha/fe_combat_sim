"""
Entity modules for Fire Emblem Combat Simulator.
Includes character classes, weapons, and items.
"""

# Import all entity classes for easier access
from fe_combat_sim.entities.character import Character
from fe_combat_sim.entities.weapon import Weapon
from fe_combat_sim.entities.character_class import CharacterClass
from fe_combat_sim.entities.character_class import (
    INFANTRY, KNIGHT, CAVALIER, PEGASUS_KNIGHT,
    WYVERN_RIDER, MAGE, LORD, PREDEFINED_CLASSES,
    get_class
)
