### Day 7 Task: Refactor your Day 6 script using functions and add error handling.

Here's the scenario: A senior engineer reviews your dashboard script and says it works, but it's not maintainable. Everything is flat — if something breaks, it's hard to tell where. She asks you to refactor it so each action is its own function, and to make sure it handles bad input gracefully instead of crashing with a traceback.

What to build: Restructure your Day 6 script so that loading the JSON, building the HTML, and writing the file are each their own function. Then add error handling so the script prints a clear message instead of crashing if a file doesn't exist or the JSON is malformed.

What you'll need to figure out: You already know how to write the logic — the new pieces are function definitions with parameters and return values, try/except blocks, and the if __name__ == "__main__" pattern. Look that last one up in the Python docs before you start — it's a standard convention you'll see everywhere and it's worth understanding why it exists before you use it.

### DOCUMENTATION

## Day 7 – Refactoring with Functions and Error Handling

Goal: Restructure the Day 6 script so each action is its own function, and add error handling so the script fails gracefully instead of crashing.

What I built: Refactored the server dashboard script into four distinct functions — load_servers(), get_status_color(), build_html(), and save_html() — and wrapped the main execution block in if __name__ == "__main__".

What I learned:

Refactoring means restructuring working code without changing what it does

Functions make code easier to read, debug, and reuse

try/except catches specific errors and lets you handle them with a readable message instead of a crash

if __name__ == "__main__" ensures code only executes when the file is run directly, not when it's imported by another script