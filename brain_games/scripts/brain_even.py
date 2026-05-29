from random import randint

import brain_games.cli as cli


def welcome_message():
    print("Welcome to the Brain Games!")


def show_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_random_num():
    return randint(1, 100)


def get_answer():
    return input("Your answer: ").lower()


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def run_game(name_gamer):
    count_correct_answer = 1

    while count_correct_answer < 4:
        random_number = get_random_num()
        even_or_not = is_even(random_number)

        print(f"Question: {random_number}")

        answer = get_answer()

        if (answer == "yes" and even_or_not) or (
            answer == "no" and not even_or_not
        ):
            print("Correct!")
        elif answer != "yes" and even_or_not:
            return print(
                f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\n"
                f"Let's try again, {name_gamer}!"
            )
        else:
            return print(
                f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\n"
                f"Let's try again, {name_gamer}!"
            )
        count_correct_answer += 1
    print(f"Congratulations, {name_gamer}!")


def main():
    welcome_message()
    name = cli.welcome_user()
    show_rules()
    run_game(name)


if __name__ == "__main__":
    main()
