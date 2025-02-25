"""
Import fix for INFANTRY class reference.
This is a temporary solution to fix import errors.
"""

# Define the INFANTRY class directly in this module
# This ensures it's available when imported from fe_combat_sim.entities
from fe_combat_sim.entities.character_class import CharacterClass

INFANTRY = CharacterClass("Infantry", 5, ["Infantry"])
KNIGHT = CharacterClass("Knight", 4, ["Armored", "Infantry"])  
CAVALIER = CharacterClass("Cavalier", 7, ["Horseback", "Mounted"])
PEGASUS_KNIGHT = CharacterClass("Pegasus Knight", 7, ["Flying", "Mounted"])
WYVERN_RIDER = CharacterClass("Wyvern Rider", 7, ["Flying", "Mounted", "Dragon"])
MAGE = CharacterClass("Mage", 5, ["Infantry", "Magic"])
LORD = CharacterClass("Lord", 5, ["Infantry", "Royal"])
