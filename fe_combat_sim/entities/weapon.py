"""
Weapon class for Fire Emblem Combat Simulator.
"""

# Import from old location and fix imports for the package structure
from entities.weapon import (
    Weapon, ARMOR_EFFECTIVE, CAVALRY_EFFECTIVE, 
    FLIER_EFFECTIVE, DRAGON_EFFECTIVE
)
# Update imports to use package structure
Weapon.__module__ = 'fe_combat_sim.entities.weapon'
