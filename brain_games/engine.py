from typing import Callable

import brain_games.cli as cli

WELCOME_MSG = "Welcome to the Brain Games!"


def get_answer():
    return input("Your answer: ")


def run_game(
    get_question_right_answer: Callable[[], tuple], rules_game: str
) -> None:

    name_gamer = cli.welcome_user()

    print(rules_game)

    count_correct_answer = 1
    while count_correct_answer < 4:
        question, right_answer = get_question_right_answer()

        print(question)

        answer = get_answer()
        if answer.lower() == str(right_answer):
            print("Correct!")
        elif answer != str(right_answer):
            return print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {right_answer}.\n"
                f"Let's try again, {name_gamer}!"
            )
        count_correct_answer += 1
    print(f"Congratulations, {name_gamer}!")
