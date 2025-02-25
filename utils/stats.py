"""
Stats utilities for Fire Emblem Combat Simulator.
"""

def calculate_growth(base, growth_rate, levels):
    """
    Calculate a stat based on growth rate and levels.
    
    Args:
        base (int): Base stat value
        growth_rate (float): Growth rate as a decimal (e.g., 0.7 for 70%)
        levels (int): Number of level-ups
        
    Returns:
        int: New stat value
    """
    import random
    
    stat = base
    
    for _ in range(levels):
        if random.random() < growth_rate:
            stat += 1
    
    return stat

def generate_random_stats(base_stats, growth_rates, levels, max_stats=None):
    """
    Generate random stats based on growth rates.
    
    Args:
        base_stats (dict): Base stats
        growth_rates (dict): Growth rates as decimals
        levels (int): Number of level-ups
        max_stats (dict, optional): Maximum values for each stat
        
    Returns:
        dict: Generated stats
    """
    stats = {}
    
    for stat, base in base_stats.items():
        growth = growth_rates.get(stat, 0)
        stats[stat] = calculate_growth(base, growth, levels)
        
        if max_stats and stat in max_stats:
            stats[stat] = min(stats[stat], max_stats[stat])
    
    return stats
