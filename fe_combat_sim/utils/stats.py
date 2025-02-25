"""
Stats utilities for Fire Emblem Combat Simulator.
"""

# Import from old location and fix imports for the package structure
from utils.stats import calculate_growth, generate_random_stats
# Update imports to use package structure
calculate_growth.__module__ = 'fe_combat_sim.utils.stats'
generate_random_stats.__module__ = 'fe_combat_sim.utils.stats'
