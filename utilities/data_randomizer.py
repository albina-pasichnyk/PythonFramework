import random
import string


def generate_random_token(length=25):
    random_token = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return random_token


def generate_random_user_name(length=15):
    random_user_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return random_user_name


def generate_random_user_email():
    validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    loginlen = random.randint(4, 15)
    login = ''
    for i in range(loginlen):
        pos = random.randint(0, len(validchars) - 1)
        login = login + validchars[pos]
    if login[0].isnumeric():
        pos = random.randint(0, len(validchars) - 10)
        login = validchars[pos] + login
    servers = ['@gmail', '@exalate', '@hotmail']
    servpos = random.randint(0, len(servers) - 1)
    random_email = login + servers[servpos]
    tlds = ['.com', '.net', '.org']
    tldpos = random.randint(0, len(tlds) - 1)
    random_email = random_email + tlds[tldpos]
    return random_email


def generate_invalid_invitation_code(length=100):
    invalid_invitation_code = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return invalid_invitation_code
