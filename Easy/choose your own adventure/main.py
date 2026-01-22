print("Welcome to the Adventure Game!")
print("You are standing at a crossroads.")

choice1 = input("Do you go left or right? ").lower()

if choice1 == "left":
    choice2 = input("You see a river. Do you swim or walk around it? ").lower()

    if choice2 == "swim":
        print("You tried to swim but got tired. Game over 😢")
    elif choice2 == "walk":
        print("You found a bridge and crossed safely. You win! 🎉")
    else:
        print("Invalid choice. Game over.")

elif choice1 == "right":
    choice2 = input("You meet a stranger. Do you talk or run? ").lower()

    if choice2 == "talk":
        print("The stranger helps you find treasure. You win! 💰")
    elif choice2 == "run":
        print("You got lost in the forest. Game over 😢")
    else:
        print("Invalid choice. Game over.")

else:
    print("Invalid choice. Game over.")
