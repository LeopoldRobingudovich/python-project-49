from random import choice, randint

DESCRIPTION = "What is the result of the expression?"


def get_random_num():
    return randint(1, 100)


def get_random_operator():
    operators = "+-*"
    return choice(operators)


def get_question_right_answer() -> tuple[str, int]:
    random_number1 = get_random_num()
    random_number2 = get_random_num()
    random_operator = get_random_operator()
    question = f"Question: {random_number1} {random_operator} {random_number2}"

    match random_operator:
        case "+":
            right_answer = random_number1 + random_number2
            return question, right_answer
        case "-":
            right_answer = random_number1 - random_number2
            return question, right_answer
        case "*":
            right_answer = random_number1 * random_number2
            return question, right_answer
