"""
Fire Emblem Combat Simulator
A Python package for simulating turn-based tactical RPG combat in the style of Fire Emblem.
"""

__version__ = "0.1.0"

# Import key components for easy access
from fe_combat_sim.entities.character import Character
from fe_combat_sim.entities.weapon import Weapon
from fe_combat_sim.entities.character_class import CharacterClass
from fe_combat_sim.combat.battle import Battle
