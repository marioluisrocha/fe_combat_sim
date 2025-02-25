"""
Streamlit app for running the Fire Emblem Combat Simulator with comprehensive GBA class system.
This version includes all classes and weapons from Fire Emblem 6, 7, and 8.
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
from fe_combat_sim.utils.gba_prediction import predict_damage, predict_battle_outcome

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
    .highlight {
        background-color: #ffd700;
        padding: 2px 5px;
        border-radius: 3px;
        font-weight: bold;
    }
    .promoted {
        color: #8b0000;
        font-weight: bold;
    }
    .unpromoted {
        color: #0000cd;
        font-weight: bold;
    }
    .monster {
        color: #800080;
        font-weight: bold;
    }
    .legendary {
        color: #daa520;
        font-weight: bold;
        text-shadow: 0px 0px 2px #ffd700;
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

Choose characters from **over 60 different classes** and equip them with **more than 100 weapons** from the GBA games!
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
        "Excalibur", "Audhulma", "Naglfar", "Reginleif", "Wolf Beil",
        "Mani Katti", "Rapier"
    ]
    return {name: WEAPONS[name] for name in legendary_names if name in WEAPONS}

# Group classes by category
def group_classes_by_category():
    grouped = {
        "Lord Classes": [],
        "Knight/Armor Classes": [],
        "Cavalry Classes": [],
        "Flying Classes": [],
        "Infantry Classes": [],
        "Magic Classes": [],
        "Support Classes": [],
        "Special Classes": [],
        "Monster Classes": []
    }
    
    for name, char_class in CHARACTER_TEMPLATES.items():
        class_obj = char_class["class"]
        
        # Determine the group
        if "Royal" in class_obj.class_types:
            grouped["Lord Classes"].append((name, class_obj))
        elif "Armored" in class_obj.class_types:
            grouped["Knight/Armor Classes"].append((name, class_obj))
        elif "Horseback" in class_obj.class_types and "Magic" not in class_obj.class_types:
            grouped["Cavalry Classes"].append((name, class_obj))
        elif "Flying" in class_obj.class_types:
            grouped["Flying Classes"].append((name, class_obj))
        elif "Magic" in class_obj.class_types:
            grouped["Magic Classes"].append((name, class_obj))
        elif name in ["Dancer", "Bard", "Thief", "Assassin", "Rogue"]:
            grouped["Support Classes"].append((name, class_obj))
        elif "Monster" in class_obj.class_types:
            grouped["Monster Classes"].append((name, class_obj))
        elif name in ["Manakete", "Journeyman", "Recruit", "Pupil", "Super Trainee"]:
            grouped["Special Classes"].append((name, class_obj))
        else:
            grouped["Infantry Classes"].append((name, class_obj))
    
    # Sort classes within each category
    for category in grouped:
        # Sort by promotion status (unpromoted first) then by name
        grouped[category] = sorted(grouped[category], key=lambda x: (x[1].promoted, x[0]))
    
    return grouped

# Helper to format class name with styling
def format_class_name(name, is_promoted=False, is_monster=False):
    if is_monster:
        return f'<span class="monster">{name}</span>'
    elif is_promoted:
        return f'<span class="promoted">{name}</span>'
    else:
        return f'<span class="unpromoted">{name}</span>'

# Helper to format weapon name with styling
def format_weapon_name(name, is_legendary=False):
    if is_legendary:
        return f'<span class="legendary">{name}</span>'
    else:
        return name

# Load weapon and class groups
weapon_groups = group_weapons_by_type()
legendary_weapons = get_legendary_weapons()
class_groups = group_classes_by_category()

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
        
        # Create tabs for class categories
        class_category_tabs = st.tabs(list(class_groups.keys()))
        
        # Variable to store the selected class
        selected_class = None
        selected_class_name = None
        
        # Display classes by category
        for i, (category, classes) in enumerate(class_groups.items()):
            with class_category_tabs[i]:
                if classes:  # Only show if category has classes
                    classes_dict = {name: obj for name, obj in classes}
                    
                    # Create a radio selection with formatted class names
                    class_options = []
                    for class_name, class_obj in classes:
                        is_promoted = class_obj.promoted
                        is_monster = "Monster" in class_obj.class_types
                        formatted_name = f"{class_name} ({'Promoted' if is_promoted else 'Base'}) - {', '.join(class_obj.weapons)}"
                        class_options.append((class_name, formatted_name, is_promoted, is_monster))
                    
                    # Create columns for class selection to make the UI more compact
                    cols = st.columns(2)
                    for j, (class_name, formatted_name, is_promoted, is_monster) in enumerate(class_options):
                        col_idx = j % 2
                        with cols[col_idx]:
                            if st.checkbox(
                                formatted_name,
                                key=f"{character_key}_{category}_{class_name}",
                                help=f"Class types: {', '.join(classes_dict[class_name].class_types)}"
                            ):
                                selected_class = classes_dict[class_name]
                                selected_class_name = class_name
                                
                                # Uncheck other class options
                                for k, (other_name, _, _, _) in enumerate(class_options):
                                    if other_name != class_name:
                                        st.session_state[f"{character_key}_{category}_{other_name}"] = False
                                
                                # Uncheck classes in other categories
                                for other_category, other_classes in class_groups.items():
                                    if other_category != category:
                                        for other_name, _ in other_classes:
                                            st.session_state[f"{character_key}_{other_category}_{other_name}"] = False
        
        # If no class is selected, use a default
        if not selected_class:
            selected_class_name = "Lord (Roy)"  # Default class
            selected_class = CHARACTER_TEMPLATES[selected_class_name]["class"]
        
        # Level selection
        level = st.slider(
            "Level",
            min_value=1,
            max_value=20 if not selected_class.promoted else 20,
            value=10,
            key=f"level_{character_key}"
        )
        
        # Weapon selection with game-appropriate filtering
        st.write("**Select Weapon:**")
        
        # Get class's usable weapon types
        usable_weapon_types = selected_class.weapons
        
        if not usable_weapon_types:
            st.warning(f"This class ({selected_class_name}) cannot use weapons.")
            weapon_name = None
        else:
            # Filter weapon groups to only show usable types
            usable_groups = {
                wt: weapons for wt, weapons in weapon_groups.items() 
                if wt in usable_weapon_types or wt == "Other"
            }
            
            # Legendary weapon option
            use_legendary = st.checkbox("Use Legendary Weapon", key=f"legendary_{character_key}")
            
            if use_legendary:
                # Filter legendary weapons to those the class can use
                usable_legendary = {
                    name: weapon for name, weapon in legendary_weapons.items()
                    if weapon.weapon_type in usable_weapon_types
                }
                
                if not usable_legendary:
                    st.warning(f"No legendary weapons available for this class's weapon types: {', '.join(usable_weapon_types)}")
                    weapon_name = None
                else:
                    weapon_name = st.selectbox(
                        "Legendary Weapon",
                        sorted(usable_legendary.keys()),
                        key=f"legendary_weapon_{character_key}",
                        format_func=lambda x: f"⚔️ {x} (Might: {usable_legendary[x].might})"
                    )
            else:
                # Regular weapon selection with tabs for each usable type
                if not usable_groups:
                    st.warning(f"No weapons available for this class's weapon types: {', '.join(usable_weapon_types)}")
                    weapon_name = None
                else:
                    weapon_tabs = st.tabs([wt.capitalize() for wt in usable_groups.keys()])
                    
                    # Store the selected weapon name
                    weapon_name = None
                    
                    for i, weapon_type in enumerate(usable_groups.keys()):
                        with weapon_tabs[i]:
                            weapons_of_type = usable_groups[weapon_type]
                            
                            # Only show selection if there are weapons of this type
                            if weapons_of_type:
                                weapon_options = [name for name, _ in weapons_of_type]
                                selected_weapon = st.selectbox(
                                    f"Select {weapon_type}",
                                    weapon_options,
                                    key=f"weapon_{character_key}_{weapon_type}",
                                    format_func=lambda x: f"{x} (Might: {dict(weapons_of_type)[x].might})"
                                )
                                
                                # If this tab's weapon is selected, update the weapon_name
                                if st.checkbox(f"Equip this {weapon_type}", 
                                             key=f"equip_{character_key}_{weapon_type}"):
                                    weapon_name = selected_weapon
                                    
                                    # Uncheck other weapon types
                                    for other_type in usable_groups.keys():
                                        if other_type != weapon_type:
                                            key = f"equip_{character_key}_{other_type}"
                                            if key in st.session_state:
                                                st.session_state[key] = False
        
        # Create character
        character = create_character_from_template(
            name,
            selected_class_name,
            level,
            weapon_name
        )
        
        # Display character stats
        st.write("---")
        st.write(f"**Character Stats ({selected_class_name}):**")
        
        # Format stats as a table
        stats_df = pd.DataFrame([character.stats]).T.reset_index()
        stats_df.columns = ["Stat", "Value"]
        
        # Add stat abbreviation explanations
        stat_explanations = {
            "hp": "HP (Hit Points)",
            "str": "Str (Strength)",
            "mag": "Mag (Magic)",
            "skl": "Skl (Skill)",
            "spd": "Spd (Speed)",
            "lck": "Lck (Luck)",
            "def": "Def (Defense)",
            "res": "Res (Resistance)"
        }
        stats_df["Stat"] = stats_df["Stat"].map(lambda x: stat_explanations.get(x, x))
        
        st.table(stats_df)
        
        # Display class info
        st.write("**Class Information:**")
        class_data = {
            "Name": selected_class_name,
            "Movement": selected_class.movement,
            "Class Types": ", ".join(selected_class.class_types),
            "Weapon Types": ", ".join(selected_class.weapons) if selected_class.weapons else "None",
            "Promotion Status": "Promoted" if selected_class.promoted else "Unpromoted"
        }
        class_df = pd.DataFrame(list(class_data.items()))
        class_df.columns = ["Property", "Value"]
        st.table(class_df)
        
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
            st.warning("No weapon equipped! Please select a weapon if this class can use weapons.")
        
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
            atk_data["Effectiveness"] = "✓ Effective! (3x damage)"
        
        if atk_damage_pred.get('brave', False):
            atk_data["Brave Effect"] = "✓ Strikes twice!"
        
        # Add weapon triangle information
        wt_advantage = atk_damage_pred.get('weapon_triangle', 0)
        if wt_advantage == 1:
            atk_data["Weapon Triangle"] = "✓ Advantage! (+1 damage, +15 hit)"
        elif wt_advantage == -1:
            atk_data["Weapon Triangle"] = "✗ Disadvantage! (-1 damage, -15 hit)"
        
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
            def_data["Effectiveness"] = "✓ Effective! (3x damage)"
        
        if def_damage_pred.get('brave', False):
            def_data["Brave Effect"] = "✓ Strikes twice!"
        
        # Add weapon triangle information
        wt_advantage = def_damage_pred.get('weapon_triangle', 0)
        if wt_advantage == 1:
            def_data["Weapon Triangle"] = "✓ Advantage! (+1 damage, +15 hit)"
        elif wt_advantage == -1:
            def_data["Weapon Triangle"] = "✗ Disadvantage! (-1 damage, -15 hit)"
        
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
        
        # Show average rounds and battle statistics
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        
        col_stats1.metric(
            "Average Combat Rounds",
            f"{outcome['average_rounds']:.1f}"
        )
        
        col_stats2.metric(
            "Miss Rate",
            f"{outcome.get('miss_percentage', 0):.1f}%"
        )
        
        col_stats3.metric(
            "Critical Hit Rate",
            f"{outcome.get('crit_percentage', 0):.1f}%"
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
    if not attacker.weapon and not defender.weapon:
        st.warning("Both characters need weapons equipped to show combat predictions.")
    elif not attacker.weapon:
        st.warning(f"{attacker.name} needs a weapon equipped to show combat predictions.")
    else:
        st.warning(f"{defender.name} needs a weapon equipped to show combat predictions.")

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
    if not attacker.weapon and not defender.weapon:
        st.warning("Both characters need weapons equipped to simulate a battle.")
    elif not attacker.weapon:
        st.warning(f"{attacker.name} needs a weapon equipped to simulate a battle.")
    else:
        st.warning(f"{defender.name} needs a weapon equipped to simulate a battle.")

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
    
    ### Class System
    
    The GBA Fire Emblem games feature a diverse class system with promotion paths:
    
    - **Lord Classes**: Main characters with unique promotion paths
    - **Knights/Armors**: Heavily armored units with high defense
    - **Cavalry**: Mobile mounted units
    - **Flying Units**: Pegasus Knights and Wyvern Riders with high mobility
    - **Infantry**: Foot soldiers including Fighters, Mercenaries, Myrmidons
    - **Magic Users**: Mages, Monks, Shamans, and their promoted variants
    - **Support Units**: Thieves, Dancers, Bards
    - **Trainee Classes**: Unique to FE8, these units start weak but have multiple promotion options
    - **Monster Classes**: Unique to FE8, enemy-only classes in the main game
    """)

# ---- About ----
with st.expander("About This Simulator"):
    st.markdown("""
    ### Fire Emblem Combat Simulator
    
    This simulator implements the core combat mechanics found in the GBA Fire Emblem games, including:
    
    - **Complete Class System**: All 60+ classes from the GBA Fire Emblem games
    - **Comprehensive Weapons**: All weapons from Fire Emblem 6, 7, and 8
    - **Weapon Triangle**: Sword > Axe > Lance > Sword advantage system
    - **Effective Weapons**: Special effectiveness against armor, cavalry, fliers, etc.
    - **Combat Flow**: Attack, counter-attack, and follow-up attacks based on speed
    - **Critical Hits**: Based on skill and weapon critical rates
    - **Battle Prediction**: Monte Carlo simulation to predict battle outcomes
    
    This is an open-source project created for educational purposes.
    
    *Note: This project is not affiliated with Nintendo or Intelligent Systems,
    the creators of the Fire Emblem series.*
    """)
