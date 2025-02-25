"""
This module provides a script to run the GBA-themed Streamlit app
"""
import os
import sys

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import needed modules
import streamlit

# Run the Streamlit app
if __name__ == "__main__":
    print("Starting Fire Emblem GBA Combat Simulator...")
    streamlit.bootstrap.run("fe_gba_complete.py", "", [], flag_options=[])
