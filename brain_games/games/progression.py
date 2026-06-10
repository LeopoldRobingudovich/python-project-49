from random import randint

DESCRIPTION = "What number is missing in the progression?"


def get_step_progression():
    return randint(1, 10)


def get_length_progression():
    return randint(5, 10)


def get_start_number():
    return randint(1, 50)


def get_qustion_right_answer() -> tuple[str, int]:
    length_progression = get_length_progression() + 1
    step_progression = get_step_progression()
    start_number = get_start_number()

    progression = []
    for index in range(length_progression):
        current_element = start_number + index * step_progression
        progression.append(current_element)

    replaceable_number = randint(0, length_progression - 1)
    right_answer = progression[replaceable_number]
    progression[replaceable_number] = ".."

    question = ""
    for element in progression:
        question = question + str(element) + " "
    question = question[:-1]

    return question, right_answer


# current_element = start_number + index * step_progression - формула из урока
