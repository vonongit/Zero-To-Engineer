import json # Import JSON library - used for reading JSON files
import os # Import operating system (os) library - used for file path operations

folder_name = '/Users/travonmayo/Documents/zero-to-engineer/practice_tasks/day4-compare-config-files/json_configs' # Define folder path where both config files live

removed_keys = [] # List to collect fields that exist in current but were removed in proposed
new_keys = [] # List to collect fields that are new in proposed but don't exist in current
same_keys = [] # List to collect fields that exist in both but haven't changed

# Load the current configuration file into a dictionary
with open(os.path.join(folder_name, 'current_config.json'), 'r') as f:
    current_config = json.load(f)
# Load the proposed configuration file into a dictionary
with open(os.path.join(folder_name, 'proposed_config.json'), 'r') as g:
    proposed_config = json.load(g)

    print("--- VALUE COMPARISON ---")

    # Loop through each key in the current config
    for current in current_config:
        if current not in proposed_config:
            # Field was removed in the proposed config
            removed_keys.append(current)
        elif current in proposed_config and current_config[current] == proposed_config[current]:
            # Field exists in both and the value hasn't changed — skip it
            continue
        else:
            # Field exists in both but the value is different — print the old and new values
            print(f"{current} - Current: {current_config[current]}  |  New: {proposed_config[current]} ")

    # Loop through each key in the proposed config to find newly added fields
    for proposed in proposed_config:
        if proposed not in current_config:
            # Field is new in the proposed config
            new_keys.append(proposed)

print("--- LIST OF REMOVED KEYS ---")
print(removed_keys)
print("--- LIST OF NEW KEYS ---")
print(new_keys)