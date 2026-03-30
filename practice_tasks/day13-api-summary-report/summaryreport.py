import requests
import smtplib
import email
import email.mime.text 
from email.message import EmailMessage

api = 'https://jsonplaceholder.typicode.com/users'

def api_parse(api):
    try:
        response = requests.get(api, timeout=5)
        response.raise_for_status()
        print('successful connection')
        return response.json()
    except ConnectionError:
        print('could not connect to server, check your connection')
    except Exception as e:
        # Catches any other unexpected error and prints what it was
        print(f"an unexpected error occured {e}")

def collect_data(users):
    global template
    for user in users:
        name = user['name']
        email_addr = user['email']
        city = user['address']['city']
        template = f"""{name}'s email is {email_addr} and they live in {city}."""
    return template
        
def email_contents(template):
        msg = EmailMessage()
        msg.set_content(template)
        msg['Subject'] = 'No-reply Automated report'
        msg['From'] = 'tdmayo1230@gmail.com'
        msg['To'] = 'tdmayo1230@gmail.com'

def main():
     if __name__ == '__main__':
        main()