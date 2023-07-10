import random

score = 0

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    playerchoice = input("Enter rock, paper or scissors: ")
    player = playerchoice.lower()

    if player == "rock" or player == "paper" or player == "scissors":
        if player == "rock" and computer == "rock":
            print("Tie")
            score = score
        elif player == "rock" and computer == "paper":
            print("You Lost")
            score = score
        elif player == "rock" and computer == "scissors":
            print("You Win")
            score = score + 1
        elif player == "paper" and computer == "rock":
            print("You Win")
            score = score + 1
        elif player == "paper" and computer == "paper":
            print("Tie")
            score = score
        elif player == "paper" and computer == "scissors":
            print("You Lost")
            score = score
        elif player == "scissors" and computer == "rock":
            print("You Lost")
            score = score
        elif player == "scissors" and computer == "paper":
            print("You Win")
            score = score + 1
        elif player == "scissors" and computer == "scissors":
            print("Tie")
            score = score
        else:
            print("Please write rock paper or scissors")
        print("You win " + str(score) + " times")

        playAgain = input("Do you want to play again ? ")
        if playAgain.lower() == "yes":
            continue
        elif playAgain.lower() != "yes":
            print("Bye!")
            break
    elif player != "rock" or player != "paper" or player != "scissors":
        print("Please write rock paper scissors")
        continue