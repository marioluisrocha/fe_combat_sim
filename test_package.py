"""
Simple script to test that the package structure works correctly.
"""
from fe_combat_sim.entities import Character, Weapon, CharacterClass
from fe_combat_sim.entities import KNIGHT, PEGASUS_KNIGHT
from fe_combat_sim.combat import Battle
from fe_combat_sim.data import get_weapon, create_character_from_template

def test_imports():
    """Test that all imports work correctly."""
    print("Testing imports... ", end="")
    
    # Create a weapon
    iron_sword = Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46)
    
    # Create a character class
    lord = CharacterClass("Lord", 5, ["Infantry", "Royal"])
    
    # Create a character
    marth = Character("Marth", lord, {"hp": 20, "str": 6, "skl": 7, "spd": 8, "lck": 5, "def": 5, "res": 1}, iron_sword)
    
    # Create a battle
    battle = Battle(marth, marth)
    
    print("Success!")

def test_data_module():
    """Test that the data module works correctly."""
    print("Testing data module... ", end="")
    
    # Get a predefined weapon
    weapon = get_weapon("Silver Sword")
    assert weapon.name == "Silver Sword"
    assert weapon.might == 13
    
    # Create a character from template
    character = create_character_from_template("Test", "Lord", 1, "Iron Sword")
    assert character.name == "Test"
    assert character.character_class.name == "Lord"
    assert character.weapon.name == "Iron Sword"
    
    print("Success!")

def test_battle_simulation():
    """Test that the battle simulation works correctly."""
    print("Testing battle simulation... ", end="")
    
    # Create two characters
    marth = create_character_from_template("Marth", "Lord", 10, "Silver Sword")
    minerva = create_character_from_template("Minerva", "Wyvern Rider", 10, "Silver Lance")
    
    # Create battle
    battle = Battle(marth, minerva)
    
    # Simulate combat
    result = battle.simulate_round()
    
    # Check that the battle log contains entries
    assert len(battle.log) > 0
    
    # Check that HP has been reduced
    assert marth.current_hp < marth.stats["hp"] or minerva.current_hp < minerva.stats["hp"]
    
    print("Success!")

if __name__ == "__main__":
    print("Testing fe_combat_sim package...")
    test_imports()
    test_data_module()
    test_battle_simulation()
    print("All tests passed!")
