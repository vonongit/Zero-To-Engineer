## Day 5 Task: Write a Python script that monitors a directory for new files and logs when changes are detected.

## Scenario

Here's the scenario: your team has a directory where automated pipelines drop configuration files after deployments. A senior engineer wants a simple script that watches that directory and logs whenever a new file appears or an existing file is removed. Think of it as a lightweight file watcher.

Create a directory called watch_folder/ and put a few JSON files in it to start.

Your script should check the directory, record what files are there, wait a few seconds, check again, and report what's new and what's been removed since the last check. It should keep doing this in a loop — checking, comparing, reporting — until you manually stop it.

What you'll need to figure out: you already know os.listdir() and how to compare things. The new piece is making your script run continuously and pause between checks. Look at the time module in the standard library docs.

### DOCUMENTATION

## Day 5 Documentation:

## Day 5: Directory File Monitor

I built a Python script that continuously monitors a directory for file changes. The script takes two snapshots of the directory contents with a pause between them, compares the snapshots, and reports any files that were added or removed with a timestamp. It runs in an infinite loop until manually stopped.
Key concepts I learned:

I used time.sleep() to pause script execution for a set number of seconds. This creates a window during which changes can happen before the script checks again.

I used while True to create an infinite loop that runs the monitoring cycle continuously until I manually stop it with Ctrl+C. This is a common pattern for monitoring scripts and background services. 

I initially tried placing while True inside a for loop with continue, which froze the script doing nothing. I learned that while True needs to be the outermost structure that wraps everything.

I used datetime.datetime.now() to capture the current time and include it in my output. I initially tried passing my file list into datetime.datetime.now() as an argument, which caused a TypeError about unhashable types. I learned that now() takes no arguments — it returns the current time on its own and needs to be kept separate from the data being printed.

I learned that variables defined inside a while True loop reset every cycle, which is exactly what I needed — the removed and added file lists clear out each round so results from previous cycles don't pile up. When I originally defined the lists outside the loop, old results accumulated across cycles.

I used .endswith('.json') to filter the directory listing so the script only monitors JSON config files and ignores other file types. I discovered this was necessary when my own Python script file showed up in the results after I accidentally moved it into the watch folder. I also caught a bug where my second loop used the wrong variable name — files instead of files2 — which caused the filter to use the leftover value from the first loop instead of the current file being checked.

I learned to only print when changes are detected by wrapping my print statements in if removed_files: and if added_files: checks. My earlier versions printed every cycle regardless of whether anything changed, which created noisy output. I also learned to move print statements outside the for loops so the complete list of changes prints once per cycle instead of printing a growing list after each individual file is appended.

How Day 5 builds on previous days:

The core comparison logic is the same pattern from Day 4 — looping through one collection to find items missing from another. On Day 4 I compared dictionary keys between two config files. On Day 5 I compared file lists between two directory snapshots. The logic is identical, just applied to a different data source.

I reused os.listdir() from Day 2 for getting directory contents, the .endswith() filtering from Day 2 for ignoring non-JSON files, and the separate loops for "removed" and "added" that I first used when comparing configs on Day 4. The new skills were while True for continuous execution, time.sleep() for pausing, and datetime.datetime.now() for timestamping — all of which are standard tools for monitoring and automation scripts.