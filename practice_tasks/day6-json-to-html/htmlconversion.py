import os
import json

folder_name = '/Users/travonmayo/Documents/zero-to-engineer/practice_tasks/day6-json-to-html/servers'
server_folder = os.listdir(folder_name)

# 1. Function moved outside and typo fixed
def get_status_color(status):
    status = status.lower()
    if "running" in status: 
        return "#90EE90"  # Light Green
    elif "starting" in status or "restarting" in status:
        return "#FFFFE0"  # Light Yellow
    elif "stopped" in status:
        return "#FFCCCB"  # Light Red
    return "white"

html_string = """<html><body><h1>Server Status</h1><table border="1">
<tr><th>Server Name</th><th>Status</th><th>IP</th><th>CPU Usage</th><th>Memory</th></tr>
"""

for files in server_folder:
    full_path = os.path.join(folder_name, files)
    with open(full_path, 'r') as f:
        config = json.load(f)
        
        # 2. Loop through the list in the JSON file to avoid TypeError
        for server in config:
            server_name = server['server_name']
            status = server['status']
            ip = server['ip']
            cpu_usage = server['cpu_usage']
            memory = server['memory']

            # 3. Get the color and apply it to the <tr> tag
            row_color = get_status_color(status)
            html_string += f"""<tr style="background-color: {row_color};">
                <td>{server_name}</td><td>{status}</td><td>{ip}</td><td>{cpu_usage}</td><td>{memory}</td>
            </tr>"""

html_string += "</table></body></html>"

with open('status.html', 'w') as w:
    w.write(html_string)