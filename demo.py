"""
Simple demo script for using the Fire Emblem Combat Simulator package.
"""
from fe_combat_sim.entities import Character, Weapon, CharacterClass
from fe_combat_sim.entities import KNIGHT, PEGASUS_KNIGHT, WYVERN_RIDER, CAVALIER
from fe_combat_sim.combat import Battle
from fe_combat_sim.data import get_weapon, create_character_from_template

def create_demo_weapons():
    """Create some demo weapons."""
    iron_sword = Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46)
    armor_slayer = Weapon("Armor Slayer", "Sword", might=8, hit=80, crit=0, range=(1, 1), 
                         uses=30, effective_against=["Armored"])
    killer_bow = Weapon("Killer Bow", "Bow", might=7, hit=85, crit=30, range=(2, 2), 
                        uses=20, effective_against=["Flying"])
    silver_lance = Weapon("Silver Lance", "Lance", might=14, hit=75, crit=0, range=(1, 1), uses=20)
    
    return {
        "iron_sword": iron_sword,
        "armor_slayer": armor_slayer,
        "killer_bow": killer_bow,
        "silver_lance": silver_lance
    }

def create_demo_characters(weapons):
    """Create some demo characters."""
    marth = Character(
        name="Marth", 
        character_class=CharacterClass("Lord", 5, ["Infantry", "Royal"]),
        stats={"hp": 42, "str": 12, "mag": 2, "skl": 13, "spd": 16, "lck": 12, "def": 11, "res": 4},
        weapon=weapons["iron_sword"]
    )
    
    draug = Character(
        name="Draug", 
        character_class=KNIGHT,
        stats={"hp": 48, "str": 11, "mag": 1, "skl": 8, "spd": 6, "lck": 7, "def": 17, "res": 3},
        weapon=weapons["iron_sword"]
    )
    
    caeda = Character(
        name="Caeda", 
        character_class=PEGASUS_KNIGHT,
        stats={"hp": 36, "str": 9, "mag": 5, "skl": 12, "spd": 17, "lck": 14, "def": 7, "res": 9},
        weapon=weapons["silver_lance"]
    )
    
    jagen = Character(
        name="Jagen", 
        character_class=CAVALIER,
        stats={"hp": 40, "str": 9, "mag": 3, "skl": 8, "spd": 11, "lck": 8, "def": 13, "res": 7},
        weapon=weapons["silver_lance"]
    )
    
    return {
        "marth": marth,
        "draug": draug,
        "caeda": caeda,
        "jagen": jagen
    }

def simulate_battles(characters):
    """Simulate some battles between characters."""
    battles = [
        # Standard battle between Marth and Jagen
        ("Standard Battle", characters["marth"], characters["jagen"]),
        
        # Battle with effective weapon against armor
        ("Armor Effective", characters["marth"], characters["draug"])
    ]
    
    # Set Marth's weapon to armor slayer for the second battle
    characters["marth"].weapon = get_weapon("Armorslayer")
    
    for battle_name, attacker, defender in battles:
        print(f"\n=== {battle_name} ===")
        print(f"Attacker: {attacker.name} ({attacker.character_class}) - HP: {attacker.current_hp}/{attacker.stats['hp']}")
        print(f"Weapon: {attacker.weapon.name}")
        print(f"Defender: {defender.name} ({defender.character_class}) - HP: {defender.current_hp}/{defender.stats['hp']}")
        print(f"Weapon: {defender.weapon.name}")
        print("\n" + "-" * 40 + "\n")
        
        # Create battle
        battle = Battle(attacker, defender)
        
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
        print(f"{attacker.name} - HP: {attacker.current_hp}/{attacker.stats['hp']}")
        print(f"{defender.name} - HP: {defender.current_hp}/{defender.stats['hp']}")
        
        # Reset HP for next battle
        attacker.current_hp = attacker.stats["hp"]
        defender.current_hp = defender.stats["hp"]

def using_character_templates():
    """Demonstrate using character templates from the data module."""
    print("\n=== Using Character Templates ===")
    
    # Create characters from templates
    lord = create_character_from_template("Marth", "Lord", 10, "Silver Sword")
    knight = create_character_from_template("Draug", "Knight", 10, "Silver Lance")
    
    print(f"Created {lord.name} ({lord.character_class})")
    print(f"Stats: {', '.join(f'{k}={v}' for k, v in lord.stats.items())}")
    print(f"Weapon: {lord.weapon.name}")
    
    print(f"\nCreated {knight.name} ({knight.character_class})")
    print(f"Stats: {', '.join(f'{k}={v}' for k, v in knight.stats.items())}")
    print(f"Weapon: {knight.weapon.name}")
    
    # Simulate battle between templated characters
    battle = Battle(lord, knight)
    result = battle.simulate_round()
    
    print("\nBattle Log:")
    for entry in battle.log:
        if "message" in entry:
            print(f"- {entry['message']}")
    
    if result.get("victory", False):
        print(f"\n{result['victor']} wins the battle!")
    else:
        print("\nBattle continues...")

def main():
    """Main demo function."""
    print("=== Fire Emblem Combat Simulator Demo ===")
    
    # Create demo items
    weapons = create_demo_weapons()
    characters = create_demo_characters(weapons)
    
    # Simulate battles
    simulate_battles(characters)
    
    # Demonstrate using character templates
    using_character_templates()

if __name__ == "__main__":
    main()
