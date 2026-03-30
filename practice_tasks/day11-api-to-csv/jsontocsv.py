import csv
import requests
# Import ConnectionError directly so we can reference it without the full module path
from requests.exceptions import ConnectionError

# Base URL for fetching all users
user_url = "https://jsonplaceholder.typicode.com/users"

def get_data(url):
    try:
        # Make a GET request with a 5 second timeout to avoid hanging
        response = requests.get(url, timeout=5)
        # Raise an exception if the response status code indicates a failure
        response.raise_for_status()
        # Parse and return the response body as a Python list
        return response.json()
    except ConnectionError:
        # Runs if the script cannot reach the server at all
        print('could not connect to server, check your connection')
    except Exception as e:
        # Catches any other unexpected error and prints what it was
        print(f"an unexpected error occured {e}")

def main():
    try:
        # Fetch all users from the API
        users = get_data(user_url)
        # Open a new CSV file for writing — newline='' prevents extra blank rows on Windows
        with open('user.csv', 'w', newline='') as f:
            # Create a csv writer object that will write to the file
            writer = csv.writer(f)
            # Write the header row as a list of column names
            header = ['name', 'email', 'city', 'company name']
            writer.writerow(header)
            # Loop through each user and write their data as a row
            for user in users:
                name = user['name']
                email = user['email']
                # city is nested inside address
                city = user['address']['city']
                # company name is nested inside company
                comp_name = user['company']['name']
                # Write this user's data as a single row
                writer.writerow([name, email, city, comp_name])
        # Only prints if everything above completed without error
        print('Csv created successfully!')
    except:
        # Catches any failure — file permission errors, bad data, etc.
        print('Csv creation failed')

# Only run main() when this script is executed directly
if __name__ == '__main__':
    main()