import os # Import operating system library - used for listing directory contents
import time # Import time library - used for pausing between checks
import datetime # Import datetime library - used for timestamping changes

folder_name = '/Users/travonmayo/Documents/zero-to-engineer/practice_tasks/day5-directory-monitor/watch_folder' # Path to the directory being monitored

# Run continuously until manually stopped with Ctrl+C
while True:
    
    removed_files = [] # Reset removed files list each cycle so results don't carry over
    added_files = [] # Reset added files list each cycle
    timestamp = datetime.datetime.now() # Capture the current time for this check cycle
    
    all_files1 = os.listdir(folder_name) # First snapshot of directory contents
    time.sleep(5) # Wait 5 seconds before taking the second snapshot
    all_files2 = os.listdir(folder_name) # Second snapshot of directory contents

    # Check for removed files — anything in the first snapshot that's missing from the second
    for files in all_files1:
            if not files.endswith('.json'): # Only monitor JSON files, skip everything else
                continue
            if files not in all_files2: # File was in the first snapshot but not the second — it was removed
                removed_files.append(files)
    # Check for added files — anything in the second snapshot that wasn't in the first
    for files2 in all_files2:
            if not files2.endswith('.json'): # Only monitor JSON files, skip everything else
                continue
            if files2 not in all_files1: # File is in the second snapshot but not the first — it was added
                added_files.append(files2)
    
    # Only print when changes are detected — keeps output clean with no noise
    if removed_files:
         print(f"{timestamp}: {removed_files} was removed")
    if added_files:
         print(f"{timestamp}: {added_files} was added")