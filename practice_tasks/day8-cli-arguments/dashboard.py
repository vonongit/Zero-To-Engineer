# Import the json module for reading JSON files
import json
# Import the os module for interacting with the file system (listing folders, joining paths)
import os
# Import argparse for handling command-line arguments
import argparse

# --- 1. Functions ---

# This function takes a file path, opens it, and returns the parsed JSON data
def load_servers(filepath):
    try:
        # Open the file in read mode
        with open(filepath, 'r') as f:
            # Parse the JSON content and return it as a Python list or dictionary
            return json.load(f)
    except json.JSONDecodeError:
        # If the file exists but isn't valid JSON, print a message and skip it
        print(f"Skipping {filepath}: File is not valid JSON")
        # Return an empty list so the rest of the script doesn't crash
        return []

# This function takes a status string and returns a background color for that status
def get_status_color(status):
    # Convert to lowercase so comparisons aren't case-sensitive
    status = status.lower()
    if "running" in status:
        return "#90EE90"  # Light green
    elif "starting" in status or "restarting" in status:
        return "#FFFFE0"  # Light yellow
    elif "stopped" in status:
        return "#FFCCCB"  # Light red
    # If status doesn't match anything above, return white as a fallback
    return "white"

# This function takes a list of servers and builds the HTML table rows as a string
def build_html(servers):
    # Start with an empty string — rows will be added one by one
    rows = ""
    for server in servers:
        # Get the color for this server's status by calling get_status_color()
        color = get_status_color(server['status'])
        # Build an HTML table row with the color applied and the server's data in each cell
        rows += f"""<tr style="background-color: {color};">
            <td>{server['server_name']}</td><td>{server['status']}</td>
            <td>{server['ip']}</td><td>{server['cpu_usage']}</td><td>{server['memory']}</td>
        </tr>"""
    # Return the complete string of all rows
    return rows

# This function takes the HTML rows and an output path, wraps them in a full HTML page, and writes it to a file
def save_html(html_body, output_path):
    # Wrap the table rows in a complete HTML structure with a header row
    full_html = f"<html><body><h1>Server Status</h1><table border='1'><tr><th>Server Name</th><th>Status</th><th>IP</th><th>CPU Usage</th><th>Memory</th></tr>{html_body}</table></body></html>"
    # Open the output file in write mode and write the full HTML string to it
    with open(output_path, 'w') as w:
        w.write(full_html)

# --- 2. Main Execution ---

# This block only runs when the script is executed directly (not when imported by another script)
if __name__ == "__main__":

    # Create a parser object that will handle the command-line arguments
    parser = argparse.ArgumentParser(description="Generate a server status HTML report.")

    # Define the --folder argument — expects a string, has a default path if not provided
    parser.add_argument("--folder",
                        type=str,
                        default='/Users/travonmayo/Documents/zero-to-engineer/practice_tasks/day6-json-to-html/servers',
                        help="Path to the folder containing JSON server files")

    # Define the --output argument — expects a string, defaults to out.txt if not provided
    parser.add_argument("--output",
                        type=str,
                        default="out.txt",
                        help="Specify an output file [default: out.txt]")

    # Parse the arguments the user passed in and store them in args
    # args.folder and args.output are now available to use
    args = parser.parse_args()

    # Start with an empty string that will accumulate all the HTML rows
    all_rows = ""

    # Loop through every file in the folder the user specified
    for file_name in os.listdir(args.folder):
        # Only process files that end in .json — skip anything else
        if file_name.endswith('.json'):
            # Build the full file path by joining the folder path and file name
            path = os.path.join(args.folder, file_name)
            # Load the server data from this JSON file
            data = load_servers(path)
            # Build HTML rows from the data and add them to all_rows
            all_rows += build_html(data)

    # After all files are processed, save the complete HTML to the output file
    save_html(all_rows, args.output)
    print("Report generated successfully!")