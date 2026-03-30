### Day 9 Task: Write a Python script that makes a real HTTP request to a public API and processes the response.

## Here's the scenario: A senior engineer asks you to pull live data from an external source and display it in a readable format. No more hardcoded or made-up data — your script needs to talk to a real API over the internet and do something useful with what comes back.

Use the requests library to call this free public API: https://jsonplaceholder.typicode.com/users — it returns a list of fake users with names, emails, addresses, and more.

Your script should fetch the data, loop through the users, and print a clean formatted summary for each one showing their name, email, and city.

What you'll need to figure out: You haven't used requests before — it's not in the standard library so you'll need to install it first. Look up how to install Python 

packages using pip. Then read the requests documentation to understand how to make a GET request and how to access the response data. The API returns JSON, and requests gives you a built-in way to parse it without importing the json module separately.

## Goal: Write a Python script that fetches live data from a public API, handles errors gracefully, and prints a clean summary of the results.

### Documentation

## What I built:

A structured script that makes a GET request to a public API, parses the JSON response, and prints each user's name, city, and email. Broken into functions following the same pattern as Days 7 and 8.

## What I struggled with:

Each user's 'city' was nested inside 'address' — learned to access nested keys with users['address']['city']
Kept putting return in the wrong place — inside except blocks or outside try, causing crashes
Passed url to print_summary() instead of get_data() — learned to trace the data flow carefully
Used return print(...) inside a loop — learned that return exits the function immediately and should only be used to pass a value, not to trigger a print

## What I learned:

* requests.get() makes an HTTP GET request and returns a response object
* .raise_for_status() catches any bad status code in one shot instead of checking each one individually
* timeout=5 prevents the script from hanging indefinitely if the server doesn't respond
* Nested JSON requires chaining keys: user['address']['city']
* return passes a value out of a function — don't use it just to call print()
* Dropped parse_data() because get_data() already returned parsed JSON — recognized redundant code and removed it

***Skills used: requests, raise_for_status(), try/except, functions, nested JSON, if __name__ == "__main__"***