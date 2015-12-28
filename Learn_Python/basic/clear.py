#!/usr/bin/env python3
"""
A small script which can clear the console.

The interesting part is this script can works both on Windows or Unix,
because it checks the system before run commands.
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')
