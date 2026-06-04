from brain_games.engine import WELCOME_MSG, run_game
from brain_games.games.even import DESCRIPTION, get_right_answer


def main():
    print(WELCOME_MSG)

    run_game(get_right_answer, DESCRIPTION)


if __name__ == "__main__":
    main()
