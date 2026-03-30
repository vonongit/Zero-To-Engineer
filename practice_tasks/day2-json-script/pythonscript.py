# Import the json module to read JSON files
import json
# Import the os module to work with file system directories and paths
import os

# Define the path to the folder containing all server config files
folder_name = '/Users/travonmayo/Documents/zero-to-engineer/practice_tasks/day2-json-script/server_configs'

# Get a list of all filenames inside the folder
all_files = os.listdir(folder_name)

# Define the fields that every config file must have
required_fields = ["server_name", "environment", "ip", "subnet", "cpu_count", "memory"]

# Loop through each file in the directory
for files in all_files:
    # Skip any file that isn't a JSON file
    if not files.endswith('.json'):
        continue

    # Build the full file path by combining the folder path and filename
    full_path = os.path.join(folder_name, files)
    # Reset the tracking lists for each new file
    missing_fields = []
    missing_values = []

    # Open and read the JSON file into a Python dictionary
    with open(full_path, 'r') as f:
        config = json.load(f)

    # Loop through each required field and check if it exists in the config
    for fields in required_fields:
        if fields not in config:
            # Field is missing entirely — add it to the missing fields list
            missing_fields.append(fields)
        else:
            # Field exists — now check if its value is empty or null
            values = config.get(fields)
            if values == "" or values == None:
                missing_values.append(fields)

    # Print the results for this file
    print(f"--- Results for {files} ---")
    if missing_fields and missing_values:
        print('missing field(s)', missing_fields, 'and missing value(s)', missing_values)
    elif missing_fields:
        print('missing field(s):', missing_fields)
    elif missing_values:
        print('missing values(s)', missing_values)
    else:
        print('All fields and values present')