#!/usr/bin/env python3
import sys

current_action = None
current_count = 0

# Le reducer reçoit les données triées du mapper
for line in sys.stdin:
    line = line.strip()
    
    try:
        action, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    # Si c'est la même action, on additionne
    if current_action == action:
        current_count += count
    else:
        # Si on change d'action, on affiche le total de la précédente
        if current_action:
            print("{}\t{}".format(current_action, current_count))
        current_action = action
        current_count = count

# Ne pas oublier d'afficher la toute dernière action
if current_action == action:
    print("{}\t{}".format(current_action, current_count))