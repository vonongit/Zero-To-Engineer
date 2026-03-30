Day 3 Task: Write a Python script that reads a CSV file of server logs and generates a summary report.

Here's the scenario: your team's monitoring system exports daily logs as CSV files. A senior engineer asks you to write a script that reads the log file and summarizes what happened.

Create a CSV file called server_logs.csv with columns for timestamp, server name, event type (INFO, WARNING, ERROR), and a message. Make up 15-20 rows of realistic data — things like service started, high CPU usage, disk space low, deployment completed, connection timeout. Spread the events across a few different servers and mix up the event types.

Your script should read the CSV file, then report how many events of each type occurred (INFO, WARNING, ERROR), which server had the most errors, and list all ERROR events with their timestamp and message.

### Day 3 Documentation:

## Day 3: CSV Server Log Analyzer

I built a Python script that reads a CSV file of server logs and generates a summary report. The script counts events by type (info, warning, error), lists all error events with their timestamps and messages, and identifies which server had the most errors.

Key concepts I learned:

I used Python's csv module and csv.reader() to read a CSV file. Unlike json.load() which gives you a dictionary, csv.reader() gives you rows as lists where each column is accessed by index position — row[0] for the first column, row[1] for the second, and so on.

I used next(reader) to skip the header row so it wouldn't be processed as data.

I learned that once you loop through a csv.reader, it's exhausted — you can't loop through it again. This forced me to collect all the data I needed in a single pass through the file.

I used .lower() on string values to normalize capitalization so that 'Info' and 'info' would be counted the same way. Real-world data is messy and this protects against inconsistent input.

I learned the difference between sets and dictionaries in Python. Curly braces with just values {a, b, c} creates a set, while curly braces with key-value pairs {'key': value} creates a dictionary. 
Sets don't maintain order, which is why my data looked scrambled when I accidentally used them.

I used Counter from Python's collections module to count how many errors each server had, and .most_common(1) to find the server with the highest count.

How Day 3 builds on previous days:

I reused the pattern from Day 1 of collecting data into lists during a loop and reporting after the loop finishes. I also applied the Day 1 lesson of keeping related data together — instead of appending error details into separate flat lists, I appended dictionaries with named keys into a single error_log list.
Debugging moments: I learned that csv.reader doesn't have a .load() method like json does. I learned that printing a reader object gives you the object reference, not the data — you have to loop through it. I also learned that defining a list inside a loop resets it every iteration, which was the same mistake I made on Day 2.