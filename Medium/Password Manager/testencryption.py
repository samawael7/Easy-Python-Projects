import cryptography.fernet
from cryptography.fernet import Fernet
import base64
import hashlib

master_key = input(f"enter your master key: ")

key = hashlib.sha256(master_key.encode()).digest()
key = base64.urlsafe_b64encode(key)

cipher = Fernet(key)

test = 'heloo'

enc = cipher.encrypt(test.encode())
dec = cipher.decrypt(enc).decode()

print(enc)
print(dec)