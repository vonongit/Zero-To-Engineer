## Scenario

Day 2 Task: Build a script that reads multiple server config files from a directory and generates a validation report for all of them.

Here's the scenario: your team doesn't have just one server config. They have a folder full of them — one JSON file per server. A senior engineer asks you to write a script that checks every config file in a directory and produces a single report showing which ones passed and which ones have problems.

Create a folder called configs/ inside your day 2 directory. Put 4 or 5 JSON config files in it — some valid, some with missing fields, some with empty values. Give them realistic names.

Your script should find all JSON files in that directory, validate each one using the same logic you built yesterday, and print a summary at the end that tells you which files passed and which failed and why.

# MY DOCUMENTATION

Day 2: Multi-File JSON Configuration Validator

I took my Day 1 single-file validator and scaled it to scan an entire directory of server config files, producing a validation report for each one.

What changed from Day 1 to Day 2:
In Day 1, I hardcoded a single filename with open('server_config.json'). In Day 2, I used os.listdir() to dynamically grab every file in a directory so the script adapts automatically when new config files are added.

In Day 1, my validation logic ran once. In Day 2, I wrapped the entire validation logic inside an outer loop that iterates through each file. I had to reset my missing_fields and missing_values lists inside this loop so each file gets a clean check — otherwise results would carry over between files.

In Day 1, I opened files with just the filename. In Day 2, I learned that os.listdir() returns only filenames without the folder path, so I used os.path.join() to combine the folder path and filename into a full path that Python can actually open.

New concepts I learned:
I used os.listdir() to get all filenames from a directory and os.path.join() to build full file paths. I used .endswith('.json') to filter out non-JSON files, and continue to skip to the next iteration of the loop when a file should be ignored.

I learned the importance of resetting variables inside a loop — without clearing the lists for each file, results from one file would bleed into the next.

I also hit a JSONDecodeError because some of my test config files had missing values for number fields. I learned that unlike strings, you can't leave a number field blank in JSON — you have to use null to represent an empty value.

How Day 1 connects to Day 2: The core validation logic is identical. The only difference is the scaffolding around it — reading from a directory instead of a single file, looping through multiple files, and reporting results per file. This is a common pattern in engineering: take something that works for one item and scale it to handle many.

# Mistake that I caught after completing:

One thing I caught, in my last loop I did not account for if both missing fields and missing values occur at the same time. So I made the below addition to account for this. I originally found this mistake on day 1 task which is why I corrected this day 2 task.
```python
if missing_fields and missing_values: # Added this first because if this was last the loop would never reach this if funtion in the loop
    print('missing field(s)', missing_fields, 'and missing value(s)', missing_values)
elif missing_fields:
    print('missing field(s):', missing_fields)
elif missing_values:
    print('missing values(s)', missing_values)
else:
    print('All fields and values present')
```