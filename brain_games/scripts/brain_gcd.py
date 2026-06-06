from brain_games.engine import WELCOME_MSG, run_game
from brain_games.games.gcd import DESCRIPTION, get_question_right_answer


def main():
    print(WELCOME_MSG)

    run_game(get_question_right_answer, DESCRIPTION)


if __name__ == "__main__":
    main()
