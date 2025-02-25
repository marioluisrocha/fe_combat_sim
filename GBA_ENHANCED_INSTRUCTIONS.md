"""
Updated instructions for running the enhanced Fire Emblem GBA Combat Simulator
"""

# Enhanced GBA Fire Emblem Combat Simulator

## Overview

The enhanced Fire Emblem Combat Simulator now features:

- **Complete GBA Class System**: All 60+ classes from Fire Emblem 6, 7, and 8
- **Comprehensive Weapon Collection**: 100+ weapons with authentic stats and effects
- **Interactive UI**: Class selection organized by categories with detailed information
- **Battle Prediction**: Monte Carlo simulation to predict outcomes
- **GBA-Style Visuals**: Themed interface inspired by the GBA Fire Emblem games

## Running the Enhanced Simulator

```bash
# Set up the environment as described in previous instructions
cd path/to/project
pyenv local fe-combat-env

# Install requirements
pip install -r requirements.txt

# Run the enhanced GBA simulator
streamlit run fe_gba_complete.py
```

## Features and Usage

### Character Creation

1. **Class Selection**: Classes are organized by categories:
   - Lord Classes
   - Knight/Armor Classes
   - Cavalry Classes
   - Flying Classes
   - Infantry Classes
   - Magic Classes
   - Support Classes
   - Special Classes
   - Monster Classes (from FE8)

2. **Weapon Selection**: Weapons are filtered based on what the selected class can use:
   - Standard weapons organized by type (Sword, Lance, Axe, Bow, Tome, Staff)
   - Legendary weapons option for equipping iconic weapons
   - Visual indicators for weapon effectiveness and stats

3. **Level Adjustment**: Set level between 1-20 (or 1-20 for promoted classes)

### Combat Prediction

The simulator provides detailed combat predictions:

- **Hit Rates**: Shows chance to hit based on skill, weapon, and advantages
- **Damage Calculation**: Shows expected damage considering all factors
- **Critical Rate**: Shows chance for triple damage
- **Weapon Triangle**: Highlights advantages or disadvantages 
- **Effectiveness**: Shows bonus damage against specific class types
- **Monte Carlo Simulation**: Run 100 simulated battles to predict outcomes

### Battle Simulation

Simulates a complete round of combat with:

- Attacker's initial strike
- Defender's counter-attack (if in range)
- Follow-up attacks (if one unit is 5+ speed faster)
- Critical hits
- Weapon triangle effects
- Weapon effectiveness
- Animated battle log

## Class and Weapon Notes

### Promotion Status

- **Unpromoted Classes**: Base classes (like Cavalier, Mage, Fighter)
- **Promoted Classes**: Advanced classes (like Paladin, Sage, Warrior)

### Class Types

Classes have types that determine weapon effectiveness:

- **Armored**: Weak to Armorslayer, Hammer, etc.
- **Horseback/Mounted**: Weak to Horseslayer, Halberd, etc.
- **Flying**: Weak to bows, wind magic
- **Dragon**: Weak to wyrmslayers, dragon-effective weapons
- **Infantry**: Standard movement, no special weaknesses
- **Magic**: Users of tomes and staves
- **Monster**: Special enemy classes from FE8

### Weapon Properties

Weapons have special properties:

- **Might**: Base damage
- **Hit**: Accuracy bonus
- **Crit**: Critical hit chance
- **Range**: Attack distance (1=melee, 2=ranged, etc.)
- **Effectiveness**: Bonus damage against specific class types
- **Brave Weapons**: Strike twice on attack (Brave Sword, etc.)
- **Legendary Weapons**: High-power weapons unique to each game

## Example Simulation

1. Pick a Lord class for one character (e.g., "Lord (Roy)") and equip the Binding Blade
2. Pick an Armored class for the other (e.g., "General") and equip a Silver Lance
3. Run the battle prediction to see effectiveness bonuses
4. Simulate the battle to see the combat flow

## Future Development Plans

- Support abilities/skills from the GBA games
- Unit promotion system
- Inventory management
- Support conversations and bonuses
- Map with terrain effects
- Multi-unit battles

Enjoy your tactical battles with the authentic GBA Fire Emblem experience!
