"""
Instructions for running the Fire Emblem GBA Combat Simulator
"""

# 1. Setting Up Your Environment

To run the GBA Fire Emblem Combat Simulator, follow these steps:

## Using pyenv to create a virtual environment:

```bash
# Install pyenv (if not already installed)
# On macOS (using Homebrew)
brew install pyenv

# On Linux
curl https://pyenv.run | bash

# Install a Python version (if needed)
pyenv install 3.10.0  # Or another version

# Create a virtual environment
pyenv virtualenv 3.10.0 fe-combat-env

# Set the directory to automatically use this environment
cd path/to/project
pyenv local fe-combat-env
```

## Installing dependencies:

```bash
# Install requirements
pip install -r requirements.txt
# OR
pip install -e .
```

## Running the Streamlit app:

```bash
# Run the standard Streamlit app
streamlit run streamlit_app.py

# OR run the enhanced GBA-themed version
streamlit run fe_gba_streamlit.py
```

# 2. Features of the GBA Combat Simulator

The GBA-themed simulator includes:

- All weapons from Fire Emblem 6 (Binding Blade), 7 (Blazing Blade), and 8 (Sacred Stones)
- Legendary weapons with their authentic stats
- Weapon effectiveness against different class types
- Combat mechanics matching the GBA games
- Battle prediction based on Monte Carlo simulation
- Animated combat log
- Visual styling inspired by the GBA Fire Emblem games

# 3. Project Structure

```
fe_combat_sim/                  # Main package directory
├── __init__.py
├── entities/                   # Character and item classes
├── combat/                     # Battle mechanics
├── utils/                      # Utility functions and predictions
│   └── gba_prediction.py       # GBA-specific prediction utilities
└── data/                       # Game data with all GBA weapons
streamlit_app.py                # Standard Streamlit app
fe_gba_streamlit.py             # GBA-themed Streamlit app
```

# 4. Feedback and Contributions

This is an early version of the simulator. Future improvements may include:

- Support for skills (like Luna, Sol, Astra)
- Full inventory management
- Class promotions and stat growths
- Terrain effects and defensive tiles
- Support conversations and bonuses
- Battle animations

Enjoy your tactical battles!
