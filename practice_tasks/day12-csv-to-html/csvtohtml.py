import csv
# html module imported but not needed — can be removed
import html

# Opening HTML structure with table headers — defined as a global string
# that will be built up as rows are added
html_string = """<html><body><h1>Server Status</h1><table border="1">
<tr><th>name</th><th>email</th><th>city</th><th>company</th></tr>
"""

def open_csv():
    # Declare html_string as global so we can modify it inside this function
    global html_string
    try:
        # Open the CSV file in read mode
        with open('users.csv', 'r') as f:
            # DictReader uses the first row as headers and returns each row as a dictionary
            reader = csv.DictReader(f)
            for row in reader:
                # Extract each field by its column name
                name = row['name']
                email = row['email']
                city = row['city']
                # Column name has a space in it — must match the header exactly
                company = row['company name']
                # Only add a row to the HTML if the company matches our filter list
                if company in ['Romaguera-Jacobson', 'Hoeger LLC', 'Yost and Sons']:
                    # Build and append an HTML table row for this user
                    # \n adds a newline after each row for readability in the output file
                    html_string += f"""<tr><td>{name}</td><td>{email}</td><td>{city}</td><td>{company}</td></tr>\n"""
        
        # Close the table and HTML document after all rows have been processed
        html_string += "</table></body></html>"

    except FileNotFoundError:
        # Runs if users.csv doesn't exist in the current directory
        print('CSV file not found')

def main():
    # Read the CSV and build the HTML string
    open_csv()
    # Write the completed HTML string to a file
    with open('status.html', 'w') as w:
        w.write(html_string)

# Only run main() when this script is executed directly
if __name__ == '__main__':
    main()