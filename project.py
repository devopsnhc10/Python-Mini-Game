import random

while True:
    my_answer = input("Choose: rock, paper, or scissors: ")
    my_answer = my_answer.lower()

    if my_answer not in ["rock", "paper", "scissors"]:
        print("Please choose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_answer}")

    if my_answer == computer_answer:
        print("It's a tie!")
    elif (my_answer == "paper" and computer_answer == "rock") or \
         (my_answer == "rock" and computer_answer == "scissors") or \
         (my_answer == "scissors" and computer_answer == "paper"):
        print("You Win!")
        break
    else:
        print("Computer Wins!")
        break
