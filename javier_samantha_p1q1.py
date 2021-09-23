# Quiz Creation Activity

# Quiz has 5 questions the user will answer.
# It will keep track of score and give a final result.

# Import the time module to make the quiz more dramatic!
import time

# The quiz_score variable will store the user's points.
quiz_score = 0

# Greet the user and get the user's name
name = input(f"Good day! I'm the BTS quiz bot. What's your name?\n")

# Introduce the quiz
print(f"Hello, {name}! I'm going to ask you a few questions about BTS today.\n")

# Ask if the user is ready to start the quiz.
start_quiz = input("Are you ready?\nY/N\n")

if start_quiz.lower() in ["y", "yes"]:
    # If the user says he/she is ready, run the quiz
    run_quiz = True
else:
    # If the user is not ready, do not run the quiz
    run_quiz = False
    print("Okay, see you later!")

# If the run quiz variable is true, the quiz will begin.
while run_quiz:
    print("Question #1!")
    # Ask the question and create a variable to store the user's answer
    anniversary_answer = input("What month is the anniversary of BTS?\n")

    if anniversary_answer.lower() == "june":
        # if the user's answer is correct, let him/her know and add a point to the quiz score.
        print("Correct!")
        quiz_score += 1
    else:
        # Else, let the user know the answer was wrong.
        print("Incorrect.")

    print("Question #2!")
    # Ask the question and create a variable to store the user's answer
    youngest_answer = input("What is the first name of the youngest member in BTS?\n")

    if youngest_answer.lower() == "jungkook":
        # if the user's answer is correct, let him/her know and add a point to the quiz score.
        print("Correct!")
        # Else, let the user know the answer was wrong.
        quiz_score += 1
    else:
        print("Incorrect.")

    print("Question #3!")
    # Ask the question and create a variable to store the user's answer
    recent_song_answer = input("What is the most recent song BTS released?\n")

    if recent_song_answer.lower() == "permission to dance":
        # if the user's answer is correct, let him/her know and add a point to the quiz score.
        print("Correct!")
        # Else, let the user know the answer was wrong.
        quiz_score += 1
    else:
        print("Incorrect.")

    print("Question #4!")
    # Ask the question and create a variable to store the user's answer
    members_count_answer = input("How many members are there in BTS?\n")

    if members_count_answer == "7":
        # if the user's answer is correct, let him/her know and add a point to the quiz score.
        print("Correct!")
        # Else, let the user know the answer was wrong.
        quiz_score += 1
    else:
        print("Incorrect.")

    print("Final question!")
    # Ask the question and create a variable to store the user's answer
    name_meaning_answer = input("Finally, what is the English translation of BTS' full name?\n")

    if name_meaning_answer.lower() == "bulletproof boy scouts":
        # if the user's answer is correct, let him/her know and add a point to the quiz score.
        print("Correct!")
        # Else, let the user know the answer was wrong.
        quiz_score += 1
    else:
        print("Incorrect.")

    # Thank the user for taking the quiz and share the score.
    print("Thanks for taking my quiz! Your score is...")
    time.sleep(5)
    print(f"{str(quiz_score)}/5!")

    # React differently based on the user's score.
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
    run_quiz = False
