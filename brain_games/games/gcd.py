from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_random_number():
    return randint(0, 100)


# Ищем наибольший общий делитель двух чисел(НОД):
def get_question_right_answer() -> tuple[str, int]:
    random_num1 = get_random_number()
    random_num2 = get_random_number()

    question = f"Question: {random_num1} {random_num2}"

    if random_num2 == 0:
        right_answer = random_num1
        return question, right_answer

    number1 = random_num1
    number2 = random_num2
    while number2 != 0:
        if number1 % number2 >= 0:
            remainder = number1 % number2
            number1, number2 = number2, remainder
            right_answer = number1
    return question, right_answer
