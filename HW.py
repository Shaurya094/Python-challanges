import random

def generate_password(length=12):
    l = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = '0123456789'
    p = '!@#$%^&*()-_=+[]{};:,.<>?'
    
    all = l + d + p
    password = ''.join(random.choice(all) for i in range(length))
    return password

print(generate_password())
