### Day 8 Task: Add command-line arguments to your dashboard script.

Here's the scenario: A senior engineer likes your dashboard script but says it's too hardcoded — the folder path and output file are baked into the script itself. She asks you to modify it so those values can be passed in when you run the script from the terminal, like this:

```bash
bashpython dashboard.py --folder /path/to/servers --output report.html
```

What you'll need to figure out: You already have the script structure from Day 7. The new piece is the argparse module from the Python standard library — it lets you define what arguments your script accepts and parses them automatically. Look it up in the official Python docs before you start.

### DOCUMENTATION

## Day 8 – Command-Line Arguments with argparse
Goal: Remove hardcoded values from the dashboard script and replace them with command-line arguments so the script can be run flexibly from the terminal.
What I built: Extended the Day 7 script to accept --folder and --output arguments using Python's argparse module. The script can now be run like a real CLI tool, with default values as a fallback if no arguments are passed.
What I struggled with:

python command not found on Mac — learned that macOS uses python3
Confused type= in add_argument() for a default value — learned that type specifies the data type and default is a separate parameter
Called save_html() inside the loop by mistake, causing it to write the file after every single JSON file instead of once at the end

What I learned:

argparse lets you define what arguments a script accepts, their types, default values, and help text
args = parser.parse_args() reads whatever the user passed in from the terminal and makes it available as args.folder, args.output, etc.
Default values mean the script still works even if the user doesn't pass any arguments
You need to cd into the correct directory before running a script from the terminal
On Mac, Python 3 is invoked with python3, not python

Skills used: argparse, functions, file I/O, terminal/CLI, if __name__ == "__main__"