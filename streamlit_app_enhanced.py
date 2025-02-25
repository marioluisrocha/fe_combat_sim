"""
Enhanced Streamlit app for testing the Fire Emblem Combat Simulator with battle predictions.
"""
import streamlit as st
import pandas as pd
import time
import random
import matplotlib.pyplot as plt
from fe_combat_sim.entities import Character, Weapon
from fe_combat_sim.combat import Battle
from fe_combat_sim.data import (
    WEAPONS, CHARACTER_TEMPLATES, 
    get_weapon, create_character_from_template
)
from fe_combat_sim.utils.prediction import predict_damage, predict_battle_outcome

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

# Initialize session state for combat log
if 'combat_log' not in st.session_state:
    st.session_state.combat_log = []

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

# ---- Combat Prediction ----
st.header("Combat Prediction")

# Display combat prediction
colA, colB = st.columns(2)

with colA:
    st.subheader(f"{attacker.name} → {defender.name}")
    
    # Predict damage
    atk_damage_pred = predict_damage(attacker, defender)
    
    # Format as a table
    atk_data = {
        "Hit Rate": f"{atk_damage_pred['hit_rate']:.1f}%",
        "Damage": f"{atk_damage_pred['min_damage']}",
        "Critical Rate": f"{atk_damage_pred['crit_rate']:.1f}%",
        "Critical Damage": f"{atk_damage_pred['crit_damage']}",
    }
    
    if atk_damage_pred['effectiveness']:
        atk_data["Effectiveness"] = "✓ Effective!"
    
    atk_df = pd.DataFrame(list(atk_data.items()))
    atk_df.columns = ["Stat", "Value"]
    st.table(atk_df)

with colB:
    st.subheader(f"{defender.name} → {attacker.name}")
    
    # Predict damage
    def_damage_pred = predict_damage(defender, attacker)
    
    # Format as a table
    def_data = {
        "Hit Rate": f"{def_damage_pred['hit_rate']:.1f}%",
        "Damage": f"{def_damage_pred['min_damage']}",
        "Critical Rate": f"{def_damage_pred['crit_rate']:.1f}%",
        "Critical Damage": f"{def_damage_pred['crit_damage']}",
    }
    
    if def_damage_pred['effectiveness']:
        def_data["Effectiveness"] = "✓ Effective!"
    
    def_df = pd.DataFrame(list(def_data.items()))
    def_df.columns = ["Stat", "Value"]
    st.table(def_df)

# ---- Battle Outcome Prediction ----
if st.button("Predict Battle Outcome (100 Simulations)", type="secondary"):
    # Show spinner during calculation
    with st.spinner("Running simulations..."):
        outcome = predict_battle_outcome(attacker, defender, iterations=100)
    
    st.subheader("Battle Outcome Prediction")
    
    # Show victory percentages
    col_outcome1, col_outcome2, col_outcome3 = st.columns(3)
    
    col_outcome1.metric(
        f"{attacker.name} Victory",
        f"{outcome['attacker_victory_percentage']:.1f}%"
    )
    
    col_outcome2.metric(
        f"{defender.name} Victory",
        f"{outcome['defender_victory_percentage']:.1f}%"
    )
    
    col_outcome3.metric(
        f"Draw/Inconclusive",
        f"{outcome['no_victory_percentage']:.1f}%"
    )
    
    # Show average remaining HP
    st.write("**Average Remaining HP:**")
    
    col_hp1, col_hp2 = st.columns(2)
    
    col_hp1.metric(
        attacker.name,
        f"{outcome['average_attacker_remaining_hp']:.1f}/{attacker.stats['hp']}"
    )
    
    col_hp2.metric(
        defender.name,
        f"{outcome['average_defender_remaining_hp']:.1f}/{defender.stats['hp']}"
    )
    
    # Show average rounds
    st.metric(
        "Average Combat Rounds",
        f"{outcome['average_rounds']:.1f}"
    )
    
    # Create a bar chart for victory percentages
    fig, ax = plt.subplots(figsize=(10, 5))
    
    labels = [f"{attacker.name} Victory", f"{defender.name} Victory", "Draw/Inconclusive"]
    values = [
        outcome['attacker_victory_percentage'],
        outcome['defender_victory_percentage'],
        outcome['no_victory_percentage']
    ]
    
    bars = ax.bar(labels, values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    ax.set_ylabel('Percentage')
    ax.set_title('Battle Outcome Prediction (100 Simulations)')
    
    # Display the chart using st.pyplot
    st.pyplot(fig)

# ---- Battle Simulation ----
st.header("Battle Simulation")

# Create simulate button
if st.button("Simulate Battle", type="primary"):
    # Clear previous combat log
    st.session_state.combat_log = []
    
    # Create battle
    battle = Battle(attacker, defender)
    
    # Simulate combat
    result = battle.simulate_round()
    
    # Update combat log
    st.session_state.combat_log = battle.log.copy()
    
    # Display battle log
    st.subheader("Battle Log")
    
    combat_log_container = st.container()
    
    with combat_log_container:
        # Display battle log entries with animation
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
            
            # Add slight delay for animation effect
            time.sleep(0.5)
    
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

# Display existing combat log if available
elif st.session_state.combat_log:
    st.subheader("Previous Battle Log")
    
    for i, entry in enumerate(st.session_state.combat_log):
        if not entry.get("hit", True):
            st.write(f"🎯 {entry['attacker']} missed!")
        else:
            # Format message with emoji
            emoji = "💥" if entry.get("critical", False) else "⚔️"
            emoji = "🔥" if entry.get("effective", False) else emoji
            
            st.write(f"{emoji} {entry['message']}")
            st.write(f"  {entry['defender']} HP: {entry['defender_hp_remaining']}")
        
        # Add separator between attacks
        if i < len(st.session_state.combat_log) - 1:
            st.write("---")
    
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
