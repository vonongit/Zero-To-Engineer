### Day 1: JSON Configuration Validator

I built a Python script that reads a JSON configuration file and validates it against a list of required fields. The script checks two things: whether all required fields exist in the config, and whether any fields have empty values (empty strings or null).

Key concepts I learned:

I used Python's json module and json.load() to read a JSON file into a Python dictionary. I discovered that JSON structure maps almost directly to Python dictionaries — key-value pairs with similar syntax.

I worked with lists as collectors — creating empty lists (missing_fields, missing_values) before a loop and using .append() to gather results, then reporting after the loop finishes instead of printing inside it.

I used config.get() to pull values from a dictionary by key, and if fields not in config to check for missing keys.

I learned that .append() returns None, so I can't put it inside a print() call. One action per line.

I learned that JSON uses null for empty values, which Python converts to None. I handled both empty strings and None with if values == "" or values == None.

I also explored isinstance() to check a value's type before calling string methods on it, but my final solution didn't require it since I checked for empty strings and None directly.

Debugging habits I practiced: reading error messages (JSONDecodeError, SyntaxWarning about 'is' vs ==), intentionally breaking my input to test edge cases, and building logic incrementally rather than trying to write everything at once.