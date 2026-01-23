import json

password_file = 'passwords.json'

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

        with open (password_file, 'r') as file:
            passwords = json.load(file)

        passwords.append({
            'site' : site,
            'username' : username,
            'password' : password
        })

        with open(password_file, 'w') as file:
            json.dump(passwords, file, indent=2)

        print(f"credentials added succesfully")

    elif choice == 2:
        with open(password_file, "r") as file:
            passwords = json.load(file)

            if not passwords:
                print(f"No passwords stored yet")
            else:
                for entry in passwords:
                    print("-" * 20)
                    print(f"Site: {entry['site']}")
                    print(f"Username: {entry['username']}")
                    print(f"Password: {entry['password']}")

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

    