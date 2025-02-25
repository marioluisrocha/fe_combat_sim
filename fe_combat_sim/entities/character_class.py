"""
Character class module for Fire Emblem Combat Simulator.
"""

# Import from old location with the updated GBA classes
from entities.character_class import (
    CharacterClass, 
    GBA_CLASSES,
    get_class,
    PREDEFINED_CLASSES,
    INFANTRY  # Make sure INFANTRY is exported
)

# Re-export all the imported names
__all__ = ['CharacterClass', 'GBA_CLASSES', 'get_class', 'PREDEFINED_CLASSES', 'INFANTRY']
