#!/usr/bin/env python3
# Import build in modules
import os

# Function to clear the terminal on all OS
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
