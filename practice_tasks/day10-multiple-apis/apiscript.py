import requests
from requests.exceptions import ConnectionError

user_url = "https://jsonplaceholder.typicode.com/users"
posts_url = "https://jsonplaceholder.typicode.com/posts"

def get_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except ConnectionError:
        print('could not connect to server, check your connection')
    except Exception as e:
        print(f"an unexpected error occured {e}")

def main():
    users = get_data(user_url)
    for user in users:
        user_id = user['id']
        name = user['name']
        posts = get_data(f"{posts_url}?userId={user_id}")
        post_count = len(posts)
        print(f"{name} has {post_count} posts")

if __name__ == '__main__':
    main()