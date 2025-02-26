"""
This module provides a script to run the GBA-themed Streamlit app
"""
import os
import sys
import subprocess

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Run the Streamlit app using subprocess instead of bootstrap
if __name__ == "__main__":
    print("Starting Fire Emblem GBA Combat Simulator...")
    
    # Use subprocess to run the streamlit command with server.port option to ensure only one port is used
    subprocess.run(["streamlit", "run", "fe_gba_complete.py", "--server.port=8501"])
