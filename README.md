To automate updating a JSON file's `identifier` property on GitHub every week, you can use GitHub Actions. Here is a step-by-step guide:

1. **Create a list of identifiers in a file (e.g., `identifiers.txt`) in your repository.**

2. **Add a script to update the JSON file.**

3. **Set up a GitHub Action workflow to run the script weekly.**

### Step 1: Create `identifiers.txt`
This file will contain a list of identifiers, one per line.

### Step 2: Add the update script

Create a script called `update_identifier.py`:

```python
import json
import random

# Load the list of identifiers from identifiers.txt
with open('identifiers.txt', 'r') as f:
    identifiers = [line.strip() for line in f.readlines()]

# Choose a random identifier
new_identifier = random.choice(identifiers)

# Load the config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Update the identifier
config['identifier'] = new_identifier

# Save the updated config.json
with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)
```

### Step 3: Set up GitHub Action workflow

Create a `.github/workflows/update_config.yml` file in your repository:

```yaml
name: Update Config Identifier

on:
  schedule:
    - cron: '0 0 * * 0'  # Runs every week on Sunday at midnight
  workflow_dispatch:

jobs:
  update-config:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install -r requirements.txt
        
      - name: Run update script
        run: python update_identifier.py

      - name: Commit changes
        run: |
          git config --global user.name 'github-actions'
          git config --global user.email 'github-actions@users.noreply.github.com'
          git add config.json
          git commit -m 'Update identifier'
          git push
```

### Summary
1. **identifiers.txt**: List of identifiers.
2. **update_identifier.py**: Python script to update the JSON file.
3. **.github/workflows/update_config.yml**: GitHub Action workflow to run the script weekly.
