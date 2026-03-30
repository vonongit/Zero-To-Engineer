import requests
# Import only the ConnectionError exception from requests so we can reference it directly
from requests.exceptions import ConnectionError

# The API endpoint we're pulling data from
url = "https://jsonplaceholder.typicode.com/users"

def get_data(url):
    try:
        # Make a GET request to the URL with a 5 second timeout
        response = requests.get(url, timeout=5)
        # Raise an exception if the status code indicates a failure (4xx, 5xx)
        response.raise_for_status()
        print('successful connection')
        # Parse the response body as JSON and return it as a Python list
        return response.json()
    except ConnectionError:
        # Runs if the script can't reach the server at all
        print('could not connect to server, check your connection')
    except Exception as e:
        # Catches any other unexpected error and prints what it was
        print(f"an unexpected error occured {e}")

def print_summary(users):
    try:
        # Loop through each user in the list
        for user in users:
            # Extract the fields we want — city is nested inside address
            name = user['name']
            email = user['email']
            address = user['address']['city']
            # Print a clean summary line for each user
            print(f"{name} lives in {address} and their email is {email}")
    except requests.exceptions.JSONDecodeError:
        # Runs if the data can't be read as JSON
        print('data unable to be read')

def main():
    # Fetch and parse the data from the API
    data = get_data(url)
    # Print a summary for each user
    print_summary(data)

# Only run main() when this script is executed directly, not when imported
if __name__ == '__main__':