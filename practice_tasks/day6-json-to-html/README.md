### Day 6 Task: Write a Python script that reads server configurations from a JSON file and generates a simple HTML status page.

Here's the scenario: your team wants a quick way to see the status of all servers at a glance. A senior engineer asks you to write a script that takes your server config data and generates an HTML file that can be opened in a browser — a basic status dashboard.

Create a JSON file with 5-6 servers, each with a name, IP address, status (running/stopped/warning), and CPU usage. Your script should read the JSON file and generate an HTML file with a table showing all servers. Color code the rows — green for running, red for stopped, yellow for warning.

What you'll need to figure out: you already know JSON and file reading. The new piece is writing an HTML file from Python. HTML is just text with tags — you'll build a string of HTML content and write it to a .html file. You don't need any new libraries. Look at basic HTML table syntax if you haven't seen it before.

## Documentation

Day 6 – JSON to HTML Server Status Dashboard

Goal: Read server data from a JSON file and generate a color-coded HTML dashboard using Python.

What I built: A Python script that reads a JSON file containing server configurations, loops through each server, and writes an HTML file with a styled table showing each server's name, status, IP, CPU usage, and memory. Rows are color-coded green for running, yellow for starting/restarting, and red for stopped.

What I struggled with:

Tried to json.load() a file I had opened in write mode — learned that 'w' mode is write-only

Had </table> inside the loop, causing it to repeat after every row

Forgot the f prefix on an f-string, so variables printed as literal text like {server_name}

Defined a function inside the loop instead of outside it

Had a typo (runnnig) that silently broke the color logic — no error, just wrong behavior

Built the color function but forgot to actually call it and apply the result to the <tr> tag

What I figured out:

HTML is just a string — you build it piece by piece and write it to a .html file with w.write()

Structure matters: opening tags belong before the loop, row tags inside, closing tags after

Defining functions outside loops keeps code clean and avoids redundant work

Using in for status matching can cause unintended matches (e.g. "running" matches inside "restarting") — == is safer for exact status values

Skills used: os, json, f-strings, functions, conditionals, file I/O, basic HTML structure