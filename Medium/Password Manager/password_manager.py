import json
from cryptography.fernet import Fernet
import base64
import hashlib

password_file = 'passwords.json'
master_pass = 'sama'
master_hash = hashlib.sha256(master_pass.encode()).hexdigest()

def verify_master_key():
    while True:
        master_attempt = input(f"enter your master pass: ")
        attempt_hash = hashlib.sha256(master_attempt.encode()).hexdigest()
        if attempt_hash == master_hash:
            print(f"access granted")
            return master_attempt
        else:
            print(f"access denied!!\n please reenter your master password")
            continue

def generate_key(master_attempt):
    key = hashlib.sha256(master_attempt.encode()).digest()
    return base64.urlsafe_b64encode(key)


master = verify_master_key()
if not master:
    exit()

key = generate_key(master)
cipher = Fernet(key)
    
passwords = []

while True:
    print(f"Welcome to your password manager app\n")
    print(f"1.Add Password")
    print(f"2.view Password")
    print(f"3.delete Password")
    print(f"4.Exit")

    try:
        choice = int(input(f"please choose an option:\n "))

    except ValueError:
        print("Invalid input, please enter a number 1-4.")
        continue

    if choice == 1:

        site = input(f"enter the site name: ")
        username = input(f"enter your username: ")
        password = input(f"enter your password: ")
        encrypted_password = cipher.encrypt(password.encode()).decode()

        with open (password_file, 'r') as file:
            passwords = json.load(file)

        passwords.append({
            'site' : site,
            'username' : username,
            'password' : encrypted_password
        })

        with open(password_file, 'w') as file:
            json.dump(passwords, file, indent=2)

        print(f"credentials added succesfully ✅")

    elif choice == 2:
        with open(password_file, "r") as file:
            passwords = json.load(file)

            if not passwords:
                print(f"No passwords stored yet")
            else:
                for entry in passwords:
                    decrypted_password = cipher.decrypt(entry['password'].encode()).decode()
                    print("-" * 20)
                    print(f"Site: {entry['site']}")
                    print(f"Username: {entry['username']}")
                    print(f"Password: {decrypted_password}")

    elif choice == 3:

        with open(password_file, "r") as file:
            passwords = json.load(file)

        deleted_site = input(f"choose a site to delete: \n")
        passwords = [entry for entry in passwords if entry['site'] != deleted_site ]

        with open(password_file, "w") as file:
            json.dump(passwords, file, indent=2)

            print("credentials deleted successfully ✅")

    elif choice == 4:
        print(f"Goodbye!!")
        break

    else:
        print(f"Invalid choice , please retry")
        continue

    