import random 

def rules(user_choice, computer_choice):
    result = ""
    if user_choice == computer_choice:
        result = "tie"
    elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper")):
        result = "user wins!"
    else:
        result = "computer wins!, you lose"
    return result
    
user_choice = input("enter rock, paper, or scissors: ").lower()
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(f"computer choice is {computer_choice}")
print(rules(user_choice, computer_choice))