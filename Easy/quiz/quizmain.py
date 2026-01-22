print(f"Welcome to your quiz game!\n you'll be asked 10 questions and for each correct answer you'll get 1 point")

playing = input(f"do you want to play? Yes/No")

if playing.lower() == "yes":
    print(f"let's start")
else: quit()

correct_answers = 0
answer = input(f"vvvvvv") 
if answer == "v":
    print(f"correct")
    correct_answers+=1
else: print(f"incorrect")

answer = input(f"ddddd") 
if answer == "d":
    print(f"correct")
    correct_answers+=1
else: print(f"incorrect")

print(correct_answers)