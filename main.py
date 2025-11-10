"""
Main entry point for the Hybrid Cipher System
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from menu import Menu


def main():
    """Run the hybrid cipher application"""
    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()
