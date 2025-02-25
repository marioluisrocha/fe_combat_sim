"""
Example demonstrating weapon effectiveness against different character classes.
"""
import sys
import os

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fe_combat_sim.entities.character import Character
from fe_combat_sim.entities.weapon import Weapon
from fe_combat_sim.entities.character_class import CharacterClass
from fe_combat_sim.entities.character_class import KNIGHT, CAVALIER, PEGASUS_KNIGHT, WYVERN_RIDER
from fe_combat_sim.utils.stats import generate_random_stats

def main():
    """Run a weapon effectiveness demonstration."""
    
    # Create a collection of weapons with various effectiveness
    weapons = [
        Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46),
        Weapon("Armorslayer", "Sword", might=8, hit=80, crit=0, range=(1, 1), 
              uses=30, effective_against=["Armored"]),
        Weapon("Horseslayer", "Lance", might=7, hit=70, crit=0, range=(1, 1), 
              uses=16, effective_against=["Horseback", "Mounted"]),
        Weapon("Wing Spear", "Lance", might=7, hit=85, crit=5, range=(1, 1), 
              uses=25, effective_against=["Armored", "Horseback"]),
        Weapon("Killer Bow", "Bow", might=6, hit=85, crit=30, range=(2, 2), 
              uses=20, effective_against=[]),
        Weapon("Longbow", "Bow", might=5, hit=70, crit=0, range=(2, 3), 
              uses=30, effective_against=["Flying"]),
        Weapon("Wyrmslayer", "Sword", might=8, hit=75, crit=0, range=(1, 1), 
              uses=20, effective_against=["Dragon"]),
    ]
    
    # Create characters with different class types
    characters = [
        Character("Infantry Soldier", CharacterClass("Fighter", 5, ["Infantry"]), 
                 {"hp": 40, "str": 10, "def": 8, "spd": 10}, weapons[0]),
        Character("Armored Knight", KNIGHT, 
                 {"hp": 45, "str": 9, "def": 15, "spd": 5}, weapons[0]),
        Character("Cavalry", CAVALIER, 
                 {"hp": 38, "str": 11, "def": 10, "spd": 12}, weapons[0]),
        Character("Pegasus Rider", PEGASUS_KNIGHT, 
                 {"hp": 35, "str": 8, "def": 7, "spd": 15}, weapons[0]),
        Character("Wyvern Rider", WYVERN_RIDER, 
                 {"hp": 42, "str": 12, "def": 12, "spd": 9}, weapons[0]),
    ]
    
    # Print header
    print("=== Weapon Effectiveness Demonstration ===\n")
    
    # For each weapon and character combination, show effectiveness
    for weapon in weapons:
        print(f"Weapon: {weapon.name} ({weapon.weapon_type})")
        print(f"Might: {weapon.might}, Hit: {weapon.hit}, Crit: {weapon.crit}")
        print(f"Effective against: {', '.join(weapon.effective_against) if weapon.effective_against else 'None'}")
        print("\nEffectiveness against characters:")
        
        for character in characters:
            effective = weapon.is_effective_against(character)
            multiplier = weapon.get_effectiveness_multiplier(character)
            
            effectiveness_text = "EFFECTIVE! (x3 damage)" if effective else "Normal damage"
            
            print(f"  {character.name} ({character.character_class}): {effectiveness_text}")
            print(f"    Class types: {', '.join(character.character_class.class_types)}")
        
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()
