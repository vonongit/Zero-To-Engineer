### Day 4 Documentation:

## The Scenario:

Day 4 Task: Write a Python script that compares two server configuration files and reports the differences.

Here's the scenario: your team is about to push a configuration update to a server. Before applying it, a senior engineer wants to see exactly what's changing. They hand you the current config and the proposed config and ask you to write a script that shows what's been added, removed, or modified.

Create two JSON files — current_config.json and proposed_config.json. They should have mostly the same fields but with some differences: a changed value in one field, a new field added in the proposed config, and a field removed from the proposed config.

Your script should read both files, compare them, and print a clear report showing what was added, what was removed, and what was changed (including the old and new values).

## Day 4: Configuration File Comparison Tool

I built a Python script that reads two JSON configuration files — a current config and a proposed config — and generates a report showing what changed between them. The script identifies three types of differences: fields that were removed, fields that were added, and fields where the value changed.

## Key concepts I learned:

I learned to load two separate JSON files into two separate dictionaries and compare them against each other. Instead of checking data against a hardcoded list of required fields like I did on Days 1 and 2, I used the dictionaries themselves as the source of truth — looping through current_config gives me all the keys without needing to define them manually.

I used current_config[current] and proposed_config[current] to access the actual values from both dictionaries using the same key, which let me compare them directly.

I used elif to chain my conditions properly so that when a field is caught as removed, the script doesn't try to access it in the proposed config — which would cause a KeyError. This taught me that the order of conditions matters, and that if/elif/else prevents later blocks from running once a match is found, while separate if statements all run independently.

I used continue to skip fields where the values haven't changed, so the report only shows actual differences. This was a refinement I added at the end after the script was already working — my first version printed every shared field regardless of whether the value changed. Adding the continue made the output cleaner and more useful.

## How Day 4 builds on previous days:

This task combined skills from Days 1 and 2. I reused the JSON loading pattern from Day 1 (json.load()), the os.path.join() pattern from Day 2 for building file paths, and the same loop-and-check logic I've been building since the beginning. The new skill was comparing two dictionaries against each other instead of checking one dictionary against a predefined list.

Debugging moments: I hit a KeyError when my else block tried to access proposed_config['subnet'] for a field that had been removed. This happened because I used a separate if/else instead of elif, so the removed field check and the value comparison both ran. Switching to elif fixed it by ensuring only one branch executes per field.