# Quiz Creation Activity

# Quiz has 5 questions the user will answer.
# It will keep track of score and give a final result.

# This quiz will test the user on his/her knowledge of BTS, a KPop boy band.

# Import the time module to make the quiz more dramatic!
import time

# The quiz_score variable will store the user's points.
quiz_score = 0

# Greet the user and get the user's name.
username = input(f"Good day! I'm the BTS quiz bot. What's your name?\n")

# Introduce the quiz.
print(f"Hello, {username}! I'm going to ask you a few questions about BTS today.\n")

# Ask if the user is ready to start the quiz..
start_quiz_answer = input("Are you ready for my quiz?\nY/N\n")

if start_quiz_answer.lower().strip(".?/!") in ["y", "yes"]:
    # If the user says he/she is ready, run the quiz.
    run_quiz = True
elif start_quiz_answer.lower().strip(".?/!") in ["n", "no"]:
    run_quiz = False
    print("Okay, see you later!")
else:
    # If the user is not ready, do not run the quiz.
    run_quiz = False
    print("Sorry, I don't get what you're saying. I'll take that as a no!")

# If the run quiz variable is True, the quiz will begin..
while run_quiz:
    # List with nested lists of questions and answers.
    # In each nested list, the first element is the question and the second is the answer.
    questions = [
        ["What month is the anniversary of BTS? ", "june"],
        ["What is the first name of the youngest member in BTS?", "jungkook"],
        ["""What is the most recent song BTS released? Type one of the letters below:
    A: Butter
    B: Boy With Luv
    C: Permission to Dance
    D: Dynamite""", "c"],
        ["How many members are there in BTS?", "7"],
        ["Finally, what is the English translation of BTS' full name?", "bulletproof boy scouts"]
    ]

    # For each question, ask the question, get the user's answer, and check whether it is correct.
    for question in questions:
        print(question[0])

        user_answer = input()

        # If it is correct, let the user know he/she was correct and add one to the quiz score.
        if user_answer.lower().strip(".?/!") == question[1]:
            print("Correct!")
            quiz_score += 1

        # Else, let the user know he/she was wrong.
        else:
            print("Incorrect.")

    # Thank the user for taking the quiz.
    print("Thanks for taking my quiz! Your score is...")

    time.sleep(5)

    # Share the quiz score.
    print(f"{str(quiz_score)}/5 ({quiz_score / 5 * 100}%).")

    # React differently based on the user's final score.
    if quiz_score > 4:
        print("Wow! You're a BTS genius!")

    elif quiz_score > 3:
        print("Great work!")

    elif quiz_score > 2:
        print("Good job.")

    elif quiz_score > 1:
        print("Don't worry, it happens to all of us.")

    elif quiz_score > 0:
        print("At least you tried...")

    else:
        print("Do you even know who BTS is?")

    # End the run_quiz loop to finish the quiz and stop it from looping.
    run_quiz = False
