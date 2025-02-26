# Fire Emblem Combat Simulator

A Python package for simulating turn-based tactical RPG combat in the style of Fire Emblem. 


## Overview

This package provides a framework for creating and simulating Fire Emblem-style combat encounters. It features:

- Character creation with stats, classes, and weapons
- Class type system (Infantry, Armored, Flying, etc.)
- Weapon triangle mechanics
- Weapon effectiveness against specific class types
- Combat system with attack, counter-attack, and follow-up attack logic
- Critical hits and hit rate calculations
- Stat growth utilities

## Project Structure

```
fe_combat_sim/
├── __init__.py
├── entities/
│   ├── __init__.py
│   ├── character.py
│   ├── character_class.py
│   └── weapon.py
├── combat/
│   ├── __init__.py
│   └── battle.py
└── utils/
    ├── __init__.py
    ├── stats.py
    └── weapon_triangle.py
examples/
├── simple_battle.py
└── weapon_effectiveness.py
```

## Usage Example

```python
from fe_combat_sim.entities.character import Character
from fe_combat_sim.entities.weapon import Weapon
from fe_combat_sim.entities.character_class import KNIGHT, PEGASUS_KNIGHT
from fe_combat_sim.combat.battle import Battle

# Create weapons with effectiveness against specific class types
iron_sword = Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46)
armor_lance = Weapon("Armor Lance", "Lance", might=8, hit=80, crit=0, range=(1, 1), 
                     uses=30, effective_against=["Armored"])

# Create characters with specific class types
marth = Character(
    name="Marth", 
    character_class=CharacterClass("Lord", 5, ["Infantry", "Royal"]),
    stats={"hp": 42, "str": 12, "skl": 13, "spd": 16, "lck": 12, "def": 11, "res": 4},
    weapon=iron_sword
)

draug = Character(
    name="Draug", 
    character_class=KNIGHT,  # Predefined class with ["Armored", "Infantry"] types
    stats={"hp": 48, "str": 11, "skl": 8, "spd": 6, "lck": 7, "def": 17, "res": 3},
    weapon=iron_sword
)

# Simulate a battle
battle = Battle(marth, draug)
result = battle.simulate_round()

# Process results
for entry in battle.log:
    print(entry["message"])
```

## Character Classes and Weapon Effectiveness

The package implements a robust system for character classes and weapon effectiveness:

### Character Classes

Each character belongs to a specific class which defines its movement range and class types:

```python
# Create a custom character class
myrmidon = CharacterClass("Myrmidon", movement=6, class_types=["Infantry", "Sword-wielder"])

# Use predefined classes
from fe_combat_sim.entities.character_class import KNIGHT, CAVALIER, PEGASUS_KNIGHT, WYVERN_RIDER

# Character classes have types that determine weapon effectiveness
knight = Character("Armor Knight", KNIGHT, {...})  # Has "Armored" type
pegasus = Character("Pegasus Knight", PEGASUS_KNIGHT, {...})  # Has "Flying" type
wyvern = Character("Wyvern Rider", WYVERN_RIDER, {...})  # Has "Flying" and "Dragon" types
```

### Weapon Effectiveness

Weapons can be effective against specific class types, dealing increased damage:

```python
# Create weapons with effectiveness
armorslayer = Weapon("Armorslayer", "Sword", might=8, hit=80, crit=0, 
                    effective_against=["Armored"])

wing_spear = Weapon("Wing Spear", "Lance", might=7, hit=85, crit=5, 
                   effective_against=["Armored", "Horseback"])

longbow = Weapon("Longbow", "Bow", might=5, hit=70, crit=0, range=(2, 3),
                effective_against=["Flying"])

# Effectiveness is automatically applied in combat
battle = Battle(character_with_longbow, pegasus_knight)
```

When a weapon is effective against an enemy's class type, it deals 3x damage (by default).

## Combat Mechanics

The battle system implements several key Fire Emblem mechanics:

- **Attack Sequence**: Attack, counter-attack, and potential follow-up attacks
- **Weapon Triangle**: Swords > Axes > Lances > Swords
- **Hit Calculation**: Based on skill, luck, and weapon hit rates
- **Critical Hits**: Based on skill and weapon critical rates
- **Follow-up Attacks**: When one character has 5+ more speed than their opponent
- **Effectiveness**: Weapons can deal bonus damage against specific class types

## Future Development

This project is still in early development. Future additions may include:

- Support for different Fire Emblem game mechanics (GBA, Tellius, 3DS, etc.)
- Map and terrain effects
- Class skills and weapon skills
- Support relationships
- More advanced AI for computer-controlled characters

## License

This project is available under the MIT License.
