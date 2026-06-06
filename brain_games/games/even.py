from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random_num():
    return randint(1, 100)


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def get_question_right_answer() -> tuple[str, str]:
    random_number = get_random_num()
    question = f"Question: {random_number}"

    even_or_not = is_even(random_number)
    if even_or_not:
        return question, "yes"
    elif not even_or_not:
        return question, "no"
