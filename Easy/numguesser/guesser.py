# import random

# class NumberGuesser:
#     def __init__(self, lowerbound=0, upperbound=100):
#         # initialize game range and secret number
#         self.lowerbound = lowerbound
#         self.upperbound = upperbound
#         self.secretnum = random.randint(self.lowerbound, self.upperbound)
#         self.attempts = 0
#         self.previous_guesses = []  # optional: track all guesses

#     def tries(self):
#         """Ask for one guess and return True if correct, False otherwise"""
#         while True:
#             try:
#                 guess = int(input(f"Pick a number between {self.lowerbound} and {self.upperbound}: "))
#                 break
#             except ValueError:
#                 print("Invalid input! Please enter a number.")

#         self.attempts += 1
#         self.previous_guesses.append(guess)

#         if guess < self.secretnum:
#             print("Number is less than the secret number.")
#             return False
#         elif guess > self.secretnum:
#             print("Number is more than the secret number.")
#             return False
#         else:
#             print(f"🎉 Congratulations!! You guessed the number {self.secretnum} in {self.attempts} attempt(s).")
#             return True

#     def play(self):
#         """Main loop: keep guessing until correct"""
#         correct = False
#         while not correct:
#             correct = self.tries()
#             if not correct:
#                 print(f"Try again! Previous guesses: {self.previous_guesses}\n")


# # ---- Main Program ----

# print("Welcome to the Number Guesser Game!")
# game = NumberGuesser()
# game.play()

# import random
# class NumberGuesser:
#     def __init__(self, lowerbound=0, upperbound=100):
#         self.lowerbound = lowerbound
#         self.upperbound = upperbound
#         self.secretnum = random.randint(self.lowerbound, self.upperbound)
#         self.attempts = 0

#     def tries(self):
#         while True:
#             try:
#                 guess = int(input(f"Pick a number between {self.lowerbound} and {self.upperbound}: "))
#                 break
#             except ValueError:
#                 print("Invalid input! Please enter a number.")

#         self.attempts += 1

#         if guess < self.secretnum:
#             print("Number is less than the secret number.")
#             return False
#         elif guess > self.secretnum:
#             print("Number is more than the secret number.")
#             return False
#         else:
#             print(f"🎉 Congratulations!! You guessed the number {self.secretnum} in {self.attempts} attempt(s).")
#             return True

#     def play(self):
#         correct = False
#         while not correct:
#             correct = self.tries()


import random

lowerbound = 0
upperbound = 100
secretnum = random.randint(lowerbound, upperbound)
attempts = 0
while True:
    guess = int(input("guess a number "))
    attempts+=1
    if guess == secretnum:
        print("congratualitons")
        break
    elif guess < secretnum:
        print("number is less than secret num")
    elif guess > secretnum:
        print("number is more than secret num")
        
print("done")