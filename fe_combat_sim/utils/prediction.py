"""
Prediction utility functions for Fire Emblem Combat Simulator.
These functions help analyze possible combat outcomes without actually performing the combat.
"""
import random
from fe_combat_sim.combat.battle import Battle

def predict_damage(attacker, defender):
    """
    Predict the damage that an attacker would deal to a defender.
    
    Args:
        attacker: The attacking character
        defender: The defending character
        
    Returns:
        dict: Damage prediction information
    """
    # Check if the attacker has a weapon
    if not attacker.weapon:
        return {
            "min_damage": 0,
            "max_damage": 0,
            "crit_damage": 0,
            "hit_rate": 0,
            "crit_rate": 0,
            "effectiveness": False
        }
    
    # Create a temporary battle to use its calculation methods
    temp_battle = Battle(attacker, defender)
    
    # Calculate hit rate
    hit_rate = temp_battle._calculate_hit_rate(attacker, defender)
    
    # Calculate crit rate
    crit_rate = temp_battle._calculate_crit_rate(attacker, defender)
    
    # Calculate base damage
    base_damage = attacker._calculate_damage(defender)
    
    # Calculate critical damage
    crit_damage = base_damage * 3
    
    # Check for effectiveness
    effectiveness = attacker.weapon.is_effective_against(defender)
    
    return {
        "min_damage": base_damage,  # Minimum damage (no critical)
        "max_damage": base_damage,  # Maximum damage (no critical)
        "crit_damage": crit_damage,  # Critical hit damage
        "hit_rate": hit_rate,       # Hit rate percentage
        "crit_rate": crit_rate,     # Critical hit rate percentage
        "effectiveness": effectiveness  # Whether weapon is effective against defender
    }

def predict_battle_outcome(attacker, defender, iterations=100):
    """
    Predict the outcome of a battle through Monte Carlo simulation.
    
    Args:
        attacker: The attacking character
        defender: The defending character
        iterations: Number of simulations to run
        
    Returns:
        dict: Battle outcome prediction statistics
    """
    # Store original HP values to reset after each simulation
    attacker_hp = attacker.current_hp
    defender_hp = defender.current_hp
    
    results = {
        "attacker_victories": 0,
        "defender_victories": 0,
        "no_victory": 0,
        "average_attacker_remaining_hp": 0,
        "average_defender_remaining_hp": 0,
        "average_rounds": 0
    }
    
    for _ in range(iterations):
        # Reset HP
        attacker.current_hp = attacker_hp
        defender.current_hp = defender_hp
        
        # Create a new battle
        battle = Battle(attacker, defender)
        
        # Simulate combat for up to 10 rounds (to avoid potential infinite loops)
        round_count = 0
        max_rounds = 10
        
        while round_count < max_rounds:
            round_count += 1
            
            # Simulate a round
            result = battle.simulate_round()
            
            # Check if battle is over
            if result.get("victory", False):
                if result["victor"] == attacker.name:
                    results["attacker_victories"] += 1
                else:
                    results["defender_victories"] += 1
                break
            
            # If we reach max rounds without victory, count as no victory
            if round_count == max_rounds:
                results["no_victory"] += 1
        
        # Track remaining HP and rounds
        results["average_attacker_remaining_hp"] += attacker.current_hp
        results["average_defender_remaining_hp"] += defender.current_hp
        results["average_rounds"] += round_count
    
    # Calculate averages
    results["average_attacker_remaining_hp"] /= iterations
    results["average_defender_remaining_hp"] /= iterations
    results["average_rounds"] /= iterations
    
    # Calculate victory percentages
    results["attacker_victory_percentage"] = (results["attacker_victories"] / iterations) * 100
    results["defender_victory_percentage"] = (results["defender_victories"] / iterations) * 100
    results["no_victory_percentage"] = (results["no_victory"] / iterations) * 100
    
    # Reset HP to original values
    attacker.current_hp = attacker_hp
    defender.current_hp = defender_hp
    
    return results
