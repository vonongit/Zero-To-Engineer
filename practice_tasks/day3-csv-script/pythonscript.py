import os # Import os (operating system) library - used for file path operations
import csv # Import csv library - used for reading CSV files
from collections import Counter # Import Counter - used for counting occurrences in a list

file_name = '/Users/travonmayo/Documents/zero-to-engineer/practice_tasks/day3-csv-script/server_logs/server_logs.csv - Sheet1.csv' # File path to the CSV log file

info_count = [] # List that will collect every info event for counting later
warning_count = [] # List that will collect every warning event for counting later
error_count = [] # List that will collect every error event for counting later

server_error_counter = [] # List that will collect the server name each time an error occurs, for finding which server has the most errors

with open(file_name, 'r') as f: # Open the CSV file for reading
        reader = csv.reader(f) # Create a CSV reader object that will parse each row into a list
        next(reader) # Skip the header row so it isn't processed as data

        print('--- Error Summary ---')

        for row in reader: # Loop through each row in the CSV file
            
            timestamp = row[0].lower() # Column 0: timestamp of the event
            server_name = row[1].lower() # Column 1: server name
            event_type = row[2].lower() # Column 2: event type, lowercased to normalize inconsistent capitalization
            message = row[3].lower() # Column 3: event message
            
            # Check event type and append to the appropriate list
            if event_type == 'info':
                info_count.append(event_type) 
            elif event_type == 'warning':
                warning_count.append(event_type) 
            elif event_type == 'error':
                error_count.append(event_type)
                server_error_counter.append(server_name) # Track which server had this error
                print({'timestamp': timestamp, 'server': server_name, 'message': message}) # Print error details

# Find the server with the most errors using Counter
if server_error_counter:    
    counts = Counter(server_error_counter) # Count occurrences of each server name
    most_common_server_tuple = counts.most_common(1) # Get the top 1 most common as a list of tuples
    most_frequent_server = most_common_server_tuple[0][0] # Extract just the server name from the tuple
else:
     most_frequent_server = "None" # No errors found

print(f"--- Server Count ---")
print(f"The server with the most errors is: {most_frequent_server}")
print('--- Event Summary ---')
print(f"There are {len(info_count)} info events.")
print(f"There are {len(warning_count)} warning events.")
print(f"There are {len(error_count)} error events.")