### Goal: Fetch user data from a public API and write it to a CSV file that can be opened in Excel or Google Sheets.

## What I built: A script that fetches all users from the JSONPlaceholder API and writes their name, email, city, and company name to a formatted CSV file with a header row. Added success and failure messages using a try/except wrapper around the entire file writing block.

## What I struggled with:

Tried mixing csv.writer and csv.DictWriter — learned to pick one and stick with it
writeheader() belongs to DictWriter, not writer — with csv.writer you write the header as a plain writerow() call
Kept putting the loop outside the with open block — learned the loop needs to be inside so writer still exists
Used if user to check for success — learned that doesn't check file writing, it just checks if the list has data

## What I learned:

csv.writer writes rows as lists — writerow([val1, val2, val3])
The header row is just another writerow() call with column name strings
newline='' prevents extra blank lines when opening CSV files on Windows
Wrapping the entire operation in try/except gives you one clean success or failure message
Nested API data follows the same access pattern: user['address']['city'], user['company']['name']

Skills used: csv, requests, nested JSON, file I/O, try/except, if __name__ == "__main__"