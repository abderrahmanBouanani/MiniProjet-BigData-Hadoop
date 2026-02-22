#!/usr/bin/env python3
import sys
import re

# Le mapper lit chaque ligne de log depuis l'entrée standard
for line in sys.stdin:
    line = line.strip()
    
    # On cherche le mot clé "action=..."
    match = re.search(r"action=(\w+)", line)
    
    if match:
        action = match.group(1)
        # On affiche l'action et le chiffre 1, séparés par une tabulation
        print("{}\t1".format(action))