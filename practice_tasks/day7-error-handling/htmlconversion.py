import os
import json

# --- 1. Functions ---

def load_servers(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Skipping {filepath}: File is not valid JSON")
        return [] # Return empty list so the loop doesn't crash

def get_status_color(status):
    status = status.lower()
    if "running" in status: 
        return "#90EE90"
    elif "starting" in status or "restarting" in status:
        return "#FFFFE0"
    elif "stopped" in status:
        return "#FFCCCB"
    return "white"

def build_html(servers):
    rows = ""
    for server in servers:
        color = get_status_color(server['status'])
        rows += f"""<tr style="background-color: {color};">
            <td>{server['server_name']}</td><td>{server['status']}</td>
            <td>{server['ip']}</td><td>{server['cpu_usage']}</td><td>{server['memory']}</td>
        </tr>"""
    return rows

def save_html(html_body, output_path):
    full_html = f"<html><body><h1>Server Status</h1><table border='1'><tr><th>Server Name</th><th>Status</th><th>IP</th><th>CPU Usage</th><th>Memory</th></tr>{html_body}</table></body></html>"
    with open(output_path, 'w') as w:
        w.write(full_html)

# --- 2. Main Execution ---
if __name__ == "__main__":
    folder_name = '/Users/travonmayo/Documents/zero-to-engineer/practice_tasks/day6-json-to-html/servers'
    all_rows = ""

    for file_name in os.listdir(folder_name):
        full_path = os.path.join(folder_name, file_name)
        # Load data
        server_data = load_servers(full_path)
        # Build the rows for this file and add to the main string
        all_rows += build_html(server_data)

    # Save the final file
    save_html(all_rows, 'status.html')
    print("Report generated successfully!")