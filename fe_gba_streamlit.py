"""
Streamlit app for running the Fire Emblem Combat Simulator with GBA-era weapons.
This version includes all weapons from Fire Emblem 6, 7, and 8.
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

# Set page config with GBA Fire Emblem theme
st.set_page_config(
    page_title="GBA Fire Emblem Combat Simulator",
    page_icon="⚔️",
    layout="wide"
)

# Custom CSS for GBA Fire Emblem theming
st.markdown("""
<style>
    .main {
        background-color: #f5f5dc;
    }
    h1, h2, h3 {
        color: #8b0000;
    }
    .stButton>button {
        background-color: #8b0000;
        color: white;
    }
    .stButton>button:hover {
        background-color: #b22222;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("⚔️ GBA Fire Emblem Combat Simulator")
st.markdown("""
This app simulates battles from the Game Boy Advance Fire Emblem games: 
- Fire Emblem: The Binding Blade (FE6)
- Fire Emblem: The Blazing Blade (FE7)
- Fire Emblem: The Sacred Stones (FE8)

Choose your characters, equip legendary weapons, and unleash tactical combat!
""")

# Initialize session state for combat log
if 'combat_log' not in st.session_state:
    st.session_state.combat_log = []

# Group weapons by type for easier selection
def group_weapons_by_type():
    grouped = {}
    for name, weapon in WEAPONS.items():
        if weapon.weapon_type not in grouped:
            grouped[weapon.weapon_type] = []
        grouped[weapon.weapon_type].append((name, weapon))
    
    # Sort weapons within each type by might
    for weapon_type in grouped:
        grouped[weapon_type] = sorted(grouped[weapon_type], key=lambda x: x[1].might)
    
    return grouped

# Group legendary weapons separately
def get_legendary_weapons():
    legendary_names = [
        "Binding Blade", "Durandal", "Sol Katti", "Maltet", "Armads", 
        "Mulagir", "Aureola", "Apocalypse", "Siegmund", "Sieglinde", 
        "Vidofnir", "Nidhogg", "Garm", "Gleipnir", "Ivaldi",
        "Excalibur", "Audhulma"
    ]
    return {name: WEAPONS[name] for name in legendary_names if name in WEAPONS}

# Load weapon groups
weapon_groups = group_weapons_by_type()
legendary_weapons = get_legendary_weapons()

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
        
        # Weapon selection interface with tabs for different weapon types
        st.write("**Select Weapon:**")
        
        # Show a special "Legendary Weapons" section
        use_legendary = st.checkbox("Use Legendary Weapon", key=f"legendary_{character_key}")
        
        if use_legendary:
            weapon_name = st.selectbox(
                "Legendary Weapon",
                sorted(legendary_weapons.keys()),
                key=f"legendary_weapon_{character_key}"
            )
        else:
            # Regular weapon selection with tabs for each type
            weapon_tabs = st.tabs([wt.capitalize() for wt in weapon_groups.keys()])
            
            # Store the selected weapon name in a variable
            weapon_name = None
            
            for i, weapon_type in enumerate(weapon_groups.keys()):
                with weapon_tabs[i]:
                    weapons_of_type = weapon_groups[weapon_type]
                    
                    # Only show selection if there are weapons of this type
                    if weapons_of_type:
                        weapon_options = [name for name, _ in weapons_of_type]
                        selected_weapon = st.selectbox(
                            f"Select {weapon_type}",
                            weapon_options,
                            key=f"weapon_{character_key}_{weapon_type}"
                        )
                        
                        # If this tab's weapon is selected, update the weapon_name
                        if st.checkbox(f"Equip this {weapon_type}", 
                                     key=f"equip_{character_key}_{weapon_type}"):
                            weapon_name = selected_weapon
        
        # Create character
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
        
        # Display weapon info if a weapon is equipped
        if character.weapon:
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
            }
            
            if weapon.effective_against:
                weapon_data["Effective Against"] = ", ".join(weapon.effective_against)
            
            weapon_df = pd.DataFrame(list(weapon_data.items()))
            weapon_df.columns = ["Stat", "Value"]
            st.table(weapon_df)
        else:
            st.warning("No weapon equipped! Please select a weapon.")
        
        return character

# Create characters
attacker = character_creator(col1, "attacker", "Roy")
defender = character_creator(col2, "defender", "Zephiel")

# ---- Combat Prediction ----
st.header("Combat Prediction")

# Only show prediction if both characters have weapons
if attacker.weapon and defender.weapon:
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
    
    # Battle outcome prediction
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
        
        # Use GBA Fire Emblem inspired colors
        colors = ['#c22e2e', '#2e54c2', '#707070']
        bars = ax.bar(labels, values, color=colors)
        
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
else:
    st.warning("Both characters need weapons equipped to show combat predictions.")

# ---- Battle Simulation ----
st.header("Battle Simulation")

# Only allow battle if both characters have weapons
if attacker.weapon and defender.weapon:
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
                    st.markdown(f"🎯 **{entry['attacker']} missed!**")
                else:
                    # Format message with emoji and styling
                    emoji = "💥" if entry.get("critical", False) else "⚔️"
                    emoji = "🔥" if entry.get("effective", False) else emoji
                    
                    message_parts = entry["message"].split("!")
                    styled_message = f"{message_parts[0]}!"
                    if len(message_parts) > 1:
                        styled_message += message_parts[1]
                    
                    st.markdown(f"{emoji} **{styled_message}**")
                    st.markdown(f"  *{entry['defender']} HP: {entry['defender_hp_remaining']}*")
                
                # Add separator between attacks
                if i < len(battle.log) - 1:
                    st.markdown("---")
                
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
                st.markdown(f"🎯 **{entry['attacker']} missed!**")
            else:
                # Format message with emoji
                emoji = "💥" if entry.get("critical", False) else "⚔️"
                emoji = "🔥" if entry.get("effective", False) else emoji
                
                st.markdown(f"{emoji} **{entry['message']}**")
                st.markdown(f"  *{entry['defender']} HP: {entry['defender_hp_remaining']}*")
            
            # Add separator between attacks
            if i < len(st.session_state.combat_log) - 1:
                st.markdown("---")
else:
    st.warning("Both characters need weapons equipped to simulate a battle.")

# ---- GBA Game-Specific Information ----
with st.expander("About GBA Fire Emblem Games"):
    st.markdown("""
    ### The GBA Fire Emblem Trilogy
    
    **Fire Emblem: The Binding Blade (FE6)**
    - Released in 2002 for Game Boy Advance (Japan only)
    - Main character: Roy
    - Notable weapons: Binding Blade, Durandal, Maltet, Armads, Mulagir, Forblaze, Apocalypse
    
    **Fire Emblem: The Blazing Blade (FE7)**
    - Released in 2003 for Game Boy Advance (First FE game released internationally)
    - Main characters: Eliwood, Hector, Lyn
    - Prequel to The Binding Blade
    - Notable weapons: Durandal, Sol Katti, Armads, Mani Katti
    
    **Fire Emblem: The Sacred Stones (FE8)**
    - Released in 2004 for Game Boy Advance
    - Main characters: Eirika and Ephraim
    - Standalone story
    - Notable weapons: Sieglinde, Siegmund, Audhulma, Garm, Gleipnir, Ivaldi, Nidhogg, Vidofnir, Excalibur
    """)

# ---- About ----
with st.expander("About This Simulator"):
    st.markdown("""
    ### Fire Emblem Combat Simulator
    
    This simulator implements the core combat mechanics found in the GBA Fire Emblem games, including:
    
    - Character classes with different types (Infantry, Armored, Flying, etc.)
    - Weapon triangle mechanics (Sword > Axe > Lance > Sword)
    - Effective weapons against specific unit types
    - Combat flow with attack, counter-attack, and follow-up attacks
    - Critical hits and hit rate calculations based on stats
    - All weapons from Fire Emblem 6, 7, and 8
    
    This is an open-source project created for educational purposes.
    
    *Note: This project is not affiliated with Nintendo or Intelligent Systems,
    the creators of the Fire Emblem series.*
    """)
