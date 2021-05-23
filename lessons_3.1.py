import random
import string
import datetime

def generate_password(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def now():
    return str(datetime.datetime.now())
