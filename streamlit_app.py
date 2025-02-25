"""
Streamlit app for testing the Fire Emblem Combat Simulator.
"""
import streamlit as st
import pandas as pd
import random
from fe_combat_sim.entities import Character, Weapon
from fe_combat_sim.combat import Battle
from fe_combat_sim.data import (
    WEAPONS, CHARACTER_TEMPLATES, 
    get_weapon, create_character_from_template
)

# Set page config
st.set_page_config(
    page_title="Fire Emblem Combat Simulator",
    page_icon="⚔️",
    layout="wide"
)

# Page title
st.title("⚔️ Fire Emblem Combat Simulator")
st.write("""
This app lets you simulate battles between characters from a Fire Emblem-style
tactical RPG. Create characters, equip weapons, and simulate combat!
""")

# ---- Character Creation ----
st.header("Character Creation")

# Create columns for character creation
col1, col2 = st.columns(2)

# Function to create character selection UI
def character_creator(column, character_key, default_name):
    with column:
        st.subheader(f"{character_key.title()}")
        
        # Basic character info
        name = st.text_input(
            "Character Name", 
            value=default_name,
            key=f"name_{character_key}"
        )
        
        template = st.selectbox(
            "Character Class",
            list(CHARACTER_TEMPLATES.keys()),
            key=f"template_{character_key}"
        )
        
        level = st.slider(
            "Level",
            min_value=1,
            max_value=20,
            value=10,
            key=f"level_{character_key}"
        )
        
        # Weapon selection
        weapon_types = {w.weapon_type for w in WEAPONS.values()}
        weapon_type = st.selectbox(
            "Weapon Type",
            sorted(weapon_types),
            key=f"weapon_type_{character_key}"
        )
        
        # Filter weapons by type
        weapons_of_type = {
            name: weapon for name, weapon in WEAPONS.items() 
            if weapon.weapon_type == weapon_type
        }
        
        weapon_name = st.selectbox(
            "Weapon",
            sorted(weapons_of_type.keys()),
            key=f"weapon_{character_key}"
        )
        
        # Create and return character
        character = create_character_from_template(
            name,
            template,
            level,
            weapon_name
        )
        
        # Display character stats
        st.write("---")
        st.write("**Character Stats:**")
        
        # Format stats as a table
        stats_df = pd.DataFrame([character.stats]).T.reset_index()
        stats_df.columns = ["Stat", "Value"]
        st.table(stats_df)
        
        # Display weapon info
        st.write("**Weapon Stats:**")
        
        weapon = character.weapon
        weapon_data = {
            "Name": weapon.name,
            "Type": weapon.weapon_type,
            "Might": weapon.might,
            "Hit": weapon.hit,
            "Crit": weapon.crit,
            "Range": f"{weapon.range[0]}-{weapon.range[1]}",
            "Uses": f"{weapon.current_uses}/{weapon.uses}" if weapon.uses else "∞",
            "Effective Against": ", ".join(weapon.effective_against) if weapon.effective_against else "None"
        }
        
        weapon_df = pd.DataFrame(list(weapon_data.items()))
        weapon_df.columns = ["Stat", "Value"]
        st.table(weapon_df)
        
        return character

# Create characters
attacker = character_creator(col1, "attacker", "Marth")
defender = character_creator(col2, "defender", "Minerva")

# ---- Battle Simulation ----
st.header("Battle Simulation")

# Create simulate button
if st.button("Simulate Battle", type="primary"):
    # Create battle
    battle = Battle(attacker, defender)
    
    # Simulate combat
    result = battle.simulate_round()
    
    # Display battle log
    st.subheader("Battle Log")
    
    for i, entry in enumerate(battle.log):
        if not entry.get("hit", True):
            st.write(f"🎯 {entry['attacker']} missed!")
        else:
            # Format message with emoji
            emoji = "💥" if entry.get("critical", False) else "⚔️"
            emoji = "🔥" if entry.get("effective", False) else emoji
            
            st.write(f"{emoji} {entry['message']}")
            st.write(f"  {entry['defender']} HP: {entry['defender_hp_remaining']}")
        
        # Add separator between attacks
        if i < len(battle.log) - 1:
            st.write("---")
    
    # Show result
    st.subheader("Result")
    
    if result.get("victory", False):
        st.success(f"**{result['victor']} wins the battle!**")
    else:
        st.info("**Battle continues...**")
    
    # Final state
    col3, col4 = st.columns(2)
    
    col3.metric(
        f"{attacker.name}'s HP",
        f"{attacker.current_hp}/{attacker.stats['hp']}"
    )
    
    col4.metric(
        f"{defender.name}'s HP",
        f"{defender.current_hp}/{defender.stats['hp']}"
    )
    
    # Reset HP for next simulation
    attacker.current_hp = attacker.stats["hp"]
    defender.current_hp = defender.stats["hp"]
    
# ---- Terrain Effects (Section for future development) ----
with st.expander("Terrain Settings (Coming Soon)"):
    st.write("""
    In future versions, you'll be able to set terrain effects that modify
    combat outcomes. Terrain can provide defensive bonuses, movement penalties,
    or other strategic effects.
    """)
    
    # Placeholder terrain selector
    terrain_type = st.selectbox(
        "Terrain Type (Preview)",
        ["Plains", "Forest", "Mountain", "Fort", "River", "Desert"],
        disabled=True
    )

# ---- About ----
with st.expander("About This Simulator"):
    st.write("""
    ### Fire Emblem Combat Simulator
    
    This simulator implements the core combat mechanics found in the Fire Emblem series
    of tactical RPGs. The current version includes:
    
    - Character classes with different types (Infantry, Armored, Flying, etc.)
    - Weapon triangle mechanics (Sword > Axe > Lance > Sword)
    - Effective weapons against specific unit types
    - Combat flow with attack, counter-attack, and follow-up attacks
    - Critical hits and hit rate calculations based on stats
    - Random number factors affecting combat outcomes
    
    This is an open-source project created for educational purposes.
    """)
    
    st.info("""
    Note: This project is not affiliated with Nintendo or Intelligent Systems,
    the creators of the Fire Emblem series.
    """)
