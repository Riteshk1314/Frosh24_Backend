import png, pyqrcode, os
import random, string

def qr_maker(value, registration_id):
    qr = pyqrcode.create(value)
    qr.png(f'{registration_id}.png', scale=6)
    return f'{registration_id}.png'

def generate_user_secure_id():
        return ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k=8))