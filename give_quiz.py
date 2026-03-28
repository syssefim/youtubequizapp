import string
import emoji




def give_quiz(answer_key):
    num_answered_correctly = 0

    for question in answer_key.questions:
        print(f"{question.id}. {question.question}")
        
        # enumerate() gives us a counting number (index) starting at 0
        for choice in question.options:
            print(f"    {choice}")


        # Get the user's answer
        user_answer = input("Your answer: ")

        if user_answer != question.correct_answer[0]:
            print(f"Incorrect! The correct answer was {question.correct_answer[0]}\n")
        else:
            print(emoji.emojize("Correct! :party_popper:\n"))
            num_answered_correctly += 1

    display_results(answer_key, num_answered_correctly)


def display_results(answer_key, score):
    print(f"You answered {score} out of {len(answer_key.questions)} questions correctly.")
    print(f"Your score is {round(100 / len(answer_key.questions) * score, 2)}%.")