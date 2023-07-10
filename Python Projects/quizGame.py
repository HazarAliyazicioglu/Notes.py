# ------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------")
        print(key)
        for i in answers[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------")
    print("RESULTS")
    print("-------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = correct_guesses / len(questions) * 100
    print("Your score is: " + str(score))

def playAgain():
    response = input("Do you want to play again?: (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "Who is the main character of Medievil? ": "B",
    "What year was Spyro the Dragon first time released?": "D",
    "Does the Popeye have his own game?": "A",
    "What is the best game console ever?": "C"
}

answers = [
    ["A. Spyro", "B. Sir Daniel Fortesque", "C. Arthur Morgan", "D. Kratos"],
    ["A. 1995", "B. 1996", "C. 1997", "D. 1998"],
    ["A. Yes", "B. No", "C. I dont know", "D. What is Popeye?"],
    ["A. Atari", "B. Xbox", "C. Playstation", "D. Switch"]
    ]

new_game()

while playAgain():
    new_game()

print("Byee!")