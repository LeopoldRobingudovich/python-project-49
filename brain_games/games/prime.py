from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_random_number():
    return randint(0, 100)


def get_question_right_answer() -> tuple[str, str]:
    random_number = get_random_number()
    question = f"Question: {random_number}"

    if random_number < 2:
        return question, "no"

    half_number = random_number // 2

    divider = 2
    while divider <= half_number:
        if random_number % divider == 0:
            return question, "no"
        divider = divider + 1
    return question, "yes"


# простое число всегда > 1 и делится только на 1 и на само себя:
# делим рандом = 5 на 2,3,4 от 2 до 5(не включая). Достаточно делить до half...
