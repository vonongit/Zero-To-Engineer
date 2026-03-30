# Import the json module to read JSON files
import json

# Define the fields that must exist in the config
required_fields = ["server_name", "environment", "ip", "subnet", "cpu_count", "memory"]
# Create empty lists to track problems found during validation
missing_fields = []
missing_values = []

# Open the JSON file and load its contents into a Python dictionary
with open('server_config.json', 'r') as f:
    config = json.load(f)

# Loop through each required field
for fields in required_fields:
    # Check if the field exists in the config dictionary
    if fields not in config:
        # Field is missing — add it to the missing fields list
        missing_fields.append(fields)
    else:
        # Field exists — grab its value and check if it's empty or null
        values = config.get(fields)
        if values == "" or values == None:
            missing_values.append(fields)

# Report results after all fields have been checked
if missing_fields and missing_values:
    print('missing field(s)', missing_fields, 'and missing value(s)', missing_values)
elif missing_fields:
    print('missing field(s):', missing_fields)
elif missing_values:
    print('missing values(s)', missing_values)
else:
    print('All fields and values present')