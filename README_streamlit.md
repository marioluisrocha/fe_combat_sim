# Fire Emblem Combat Simulator - Streamlit Demo

This repository contains a Python package for simulating Fire Emblem-style turn-based tactical RPG combat, along with a Streamlit web app for interactive testing.

## Requirements

- Python 3.7+
- Streamlit
- Pandas

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/marioluisrocha/fe-combat-sim.git
   cd fe-combat-sim
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package and dependencies:
   ```
   pip install -e .
   ```

## Running the Streamlit App

To run the interactive Streamlit demo:

```
streamlit run streamlit_app.py
```

The web app will open in your default browser at `http://localhost:8501`.

## Features

The combat simulator implements key Fire Emblem mechanics:

- Character classes with different types (Infantry, Armored, Flying, etc.)
- Weapon triangle mechanics (Sword > Axe > Lance > Sword)
- Effective weapons against specific unit types
- Combat flow with attack, counter-attack, and follow-up attacks
- Critical hits and hit rate calculations based on stats
- Random number factors affecting combat outcomes

## Package Structure

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
├── utils/
│   ├── __init__.py
│   ├── stats.py
│   └── weapon_triangle.py
└── data/
    └── __init__.py  # Contains predefined weapons and character templates
```

## Usage Example

```python
from fe_combat_sim.entities import Character, Weapon, CharacterClass
from fe_combat_sim.entities import KNIGHT, PEGASUS_KNIGHT
from fe_combat_sim.combat import Battle

# Create weapons with effectiveness against specific class types
iron_sword = Weapon("Iron Sword", "Sword", might=5, hit=90, crit=0, range=(1, 1), uses=46)
longbow = Weapon("Longbow", "Bow", might=5, hit=70, crit=0, range=(2, 3), 
                 uses=20, effective_against=["Flying"])

# Create characters
marth = Character(
    name="Marth", 
    character_class=CharacterClass("Lord", 5, ["Infantry", "Royal"]),
    stats={"hp": 42, "str": 12, "skl": 13, "spd": 16, "lck": 12, "def": 11, "res": 4},
    weapon=iron_sword
)

caeda = Character(
    name="Caeda", 
    character_class=PEGASUS_KNIGHT,  # Predefined class with ["Flying", "Mounted"] types
    stats={"hp": 36, "str": 8, "skl": 10, "spd": 18, "lck": 15, "def": 6, "res": 9},
    weapon=iron_sword
)

# Simulate a battle
battle = Battle(marth, caeda)
result = battle.simulate_round()

# Process results
for entry in battle.log:
    print(entry["message"])
```

## License

This project is available under the MIT License.
