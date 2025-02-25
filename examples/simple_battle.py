"""
Simple battle example for Fire Emblem Combat Simulator.
"""
import sys
import os

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fe_combat_sim.entities.character import Character
from fe_combat_sim.entities.weapon import Weapon
from fe_combat_sim.entities.character_class import CharacterClass, KNIGHT, CAVALIER, PEGASUS_KNIGHT
from fe_combat_sim.combat.battle import Battle

def main():
    """Run a simple battle example."""
    
    # Create weapons with effectiveness
    iron_sword = Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46)
    
    # A lance effective against armored units
    armor_lance = Weapon("Armor Lance", "Lance", might=8, hit=80, crit=0, range=(1, 1), 
                        uses=30, effective_against=["Armored"])
    
    # A bow effective against flying units
    killer_bow = Weapon("Killer Bow", "Bow", might=7, hit=85, crit=30, range=(2, 2), 
                        uses=20, effective_against=["Flying"])
    
    # Create characters with specific classes
    marth = Character(
        name="Marth", 
        character_class=CharacterClass("Lord", 5, ["Infantry", "Royal"]),
        stats={"hp": 42, "str": 12, "mag": 2, "skl": 13, "spd": 16, "lck": 12, "def": 11, "res": 4},
        weapon=iron_sword
    )
    
    knight = Character(
        name="Draug", 
        character_class=KNIGHT,
        stats={"hp": 48, "str": 11, "mag": 1, "skl": 8, "spd": 6, "lck": 7, "def": 17, "res": 3},
        weapon=iron_sword
    )
    
    pegasus = Character(
        name="Caeda", 
        character_class=PEGASUS_KNIGHT,
        stats={"hp": 36, "str": 9, "mag": 5, "skl": 12, "spd": 17, "lck": 14, "def": 7, "res": 9},
        weapon=iron_sword
    )
    
    # Create battles to test effectiveness
    print("=== Battle 1: Normal Weapons ===")
    battle1 = Battle(marth, knight)
    simulate_and_print_battle(battle1)
    
    print("\n=== Battle 2: Weapon Effective Against Armor ===")
    marth.weapon = armor_lance
    battle2 = Battle(marth, knight)
    simulate_and_print_battle(battle2)
    
    print("\n=== Battle 3: Weapon Effective Against Flying ===")
    marth.weapon = killer_bow
    battle3 = Battle(marth, pegasus)
    simulate_and_print_battle(battle3)

def simulate_and_print_battle(battle):
    """Simulate a battle and print the results."""
    
    # Print initial state
    print(f"{battle.attacker.name} ({battle.attacker.character_class}) - HP: {battle.attacker.current_hp}/{battle.attacker.stats['hp']}")
    print(f"Weapon: {battle.attacker.weapon.name}")
    print(f"Class types: {battle.attacker.character_class.class_types}")
    print()
    print(f"{battle.defender.name} ({battle.defender.character_class}) - HP: {battle.defender.current_hp}/{battle.defender.stats['hp']}")
    print(f"Weapon: {battle.defender.weapon.name}")
    print(f"Class types: {battle.defender.character_class.class_types}")
    print("\n" + "-" * 40 + "\n")
    
    # Simulate combat
    result = battle.simulate_round()
    
    # Print battle log
    for entry in battle.log:
        if not entry.get("hit", True):
            print(f"{entry['attacker']} missed!")
        else:
            print(entry["message"])
            print(f"{entry['defender']} HP: {entry['defender_hp_remaining']}")
        print()
    
    # Print result
    if result.get("victory", False):
        print(f"{result['victor']} wins the battle!")
    else:
        print("Battle continues...")
    
    # Print final state
    print("\n" + "-" * 40 + "\n")
    print(f"{battle.attacker.name} - HP: {battle.attacker.current_hp}/{battle.attacker.stats['hp']}")
    print(f"{battle.defender.name} - HP: {battle.defender.current_hp}/{battle.defender.stats['hp']}")
    
    # Reset HP for next battle
    battle.attacker.current_hp = battle.attacker.stats["hp"]
    battle.defender.current_hp = battle.defender.stats["hp"]

if __name__ == "__main__":
    main()
