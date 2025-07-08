#!/usr/bin/env python3
"""
JourneyStamp - SceneSenseAI Auto Tagging POC
Entry point for the Streamlit application
"""

import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Import and run the main application
from app.main import main

if __name__ == "__main__":
    main()