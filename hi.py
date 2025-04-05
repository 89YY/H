import requests
import random

def check_username_availability(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f'Good - {username}')
    elif response.status_code == 200:
        print(f'Bad - {username}')
    else:
        print(f'Block - {username}')

def generate_random_username():
    return ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for _ in range(5))

def check():
    while True:
        user = generate_random_username()
        check_username_availability(user)

check()
