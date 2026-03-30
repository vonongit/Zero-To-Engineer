### Day 12 Task: Read your CSV file back into Python and generate a filtered HTML report from it.

Here's the scenario: A teammate receives your users.csv file and asks if you can generate a quick HTML report from it — but only showing users from specific companies. She wants a filtered view, not the full list. Your job is to read the CSV file you created on Day 11, filter the results, and generate an HTML file showing only the users that match.

Pick two or three company names from your CSV and filter for those. The HTML output should be a clean table showing name, email, city, and company — similar to what you built on Day 6, but this time the data source is a CSV file instead of JSON, and you're adding a filter condition.

What you'll need to figure out: You already know how to write CSV files — now look up how to read them using csv.DictReader. You also already know how to generate HTML from Python. The new piece is csv.DictReader and how it gives you each row as a dictionary, which makes filtering straightforward. Look it up in the docs before you start.


### Day 12 – Reading a CSV and Generating a Filtered HTML Report

## Goal: Read a CSV file back into Python, filter the rows by company name, and generate an HTML report showing only the matching users.

## What I built: A script that reads users.csv using csv.DictReader, filters for three specific companies, and writes a formatted HTML table to status.html containing only the matched rows.

## What I struggled with:

global syntax — tried to use it at the top level where the variable is defined. Learned that global is declared inside the function that needs to modify the variable

Kept putting html_string += closing tags and the with open write block in the wrong place — inside except or after main()

Used == to compare a string against a list — learned that in is the correct operator for checking membership in a list

f-string indentation was carrying over into the HTML output — fixed by putting everything on one line and adding \n for readability

## What I learned:

csv.DictReader automatically treats the first row as headers and returns each row as a dictionary — no need to skip the header manually

Column names must match exactly — row['company name'] not row['company']

global lets a function modify a variable defined outside it

HTML doesn't care about whitespace — rows on one line render identically to formatted rows in the browser

\n at the end of a string adds a newline for human readability without affecting the rendered output

## Skills used: csv.DictReader, filtering with in, global variables, HTML generation, file I/O, try/except, if __name__ == "__main__"