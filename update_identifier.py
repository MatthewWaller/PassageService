import json
import random

# Load the list of identifiers from identifiers.txt
with open('identifiers.txt', 'r') as f:
    identifiers = [line.rstrip() for line in f.readlines()]

# Choose a random identifier
new_identifier = random.choice(identifiers)

# Load the config.json
with open('heroConfig.json', 'r') as f:
    config = json.load(f)

# Update the identifier
config['heroId'] = new_identifier

# Save the updated config.json
with open('heroConfig.json', 'w') as f:
    json.dump(config, f, indent=4)
