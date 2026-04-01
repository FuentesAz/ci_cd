import random
import string

def generate_password(length: 12):
    characters = {
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.puntuacion
    }

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def has_uppercase(password):
    return any(c.isupper() for c in password)