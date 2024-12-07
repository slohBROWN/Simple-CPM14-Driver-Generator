import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from driver import Driver
import random

def visualize_driver_skills(driver):
    skill_names = list(driver.skills.keys())
    skill_values = list(driver.skills.values())
    
    # Adjust color map points to the range [0, 1]
    colors = [
        (0.0, "red"),         # Maps to skill level 1.0
        (0.3, "orange"),      # Maps to skill level 3-4
        (0.5, "yellow"),      # Maps to skill level 5-6
        (0.7, "lightgreen"),  # Maps to skill level 7.0
        (0.99, "darkgreen"),  # Maps to skill level 9.9
        (1.0, "blue"),        # Maps to skill level 10.0
    ]
    
    cmap = mcolors.LinearSegmentedColormap.from_list("custom_skill_map", colors)
    norm = mcolors.Normalize(vmin=1.0, vmax=10.0)
    bar_colors = [cmap(norm(value)) for value in skill_values]

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(skill_names, skill_values, color=bar_colors)
    ax.set_xlabel("Skill Level")
    ax.set_title(f"{driver.name}'s Skill Profile")
    ax.set_xlim(1, 10)
    
    # Add color gradient legend
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label="Skill Level")

    plt.show()

# Example to visualize a random driver's skills
is_rookie = random.choice([True, False])
sample_driver = Driver(is_rookie=is_rookie)
visualize_driver_skills(sample_driver)
