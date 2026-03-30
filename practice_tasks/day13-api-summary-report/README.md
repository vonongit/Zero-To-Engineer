### Day 13 Task: Write a Python script that fetches API data and sends a summary report as a formatted email.

## Here's the scenario: A senior engineer wants the server status report delivered to her inbox automatically instead of having to open an HTML file. She asks you to write a script that pulls user data from the API, builds a plain text summary, and sends it as an email.

Use Python's built-in smtplib and email modules to send the report. Use your own email address as both sender and recipient to test it. Gmail works well for this — you'll need to generate an App Password in your Google account settings since Gmail doesn't allow direct password authentication for scripts.

What you'll need to figure out: Look up smtplib and email.mime.text in the Python docs. You'll need to understand how to create a message object, set the subject and body, connect to Gmail's SMTP server, and send it. This is a common real-world automation task — scripts that email reports run on schedules in production environments all the time.

