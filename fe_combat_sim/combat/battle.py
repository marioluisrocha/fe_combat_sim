"""
Battle system for Fire Emblem Combat Simulator.
"""

# Import from old location and fix imports for the package structure
from combat.battle import Battle
# Update imports to use package structure
Battle.__module__ = 'fe_combat_sim.combat.battle'
