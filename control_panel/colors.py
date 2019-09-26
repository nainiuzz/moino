"""
COLORS
"""

from sys import platform

b = '\033[94m'
g = '\033[92m'
y = '\033[93m'
r = '\033[91m'
w = '\033[0m'

if platform == "win32":
    b = ''
    g = ''
    y = ''
    r = ''
    w = ''