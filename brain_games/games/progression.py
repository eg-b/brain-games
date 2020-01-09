import random
import prompt


def greetings():
    print("Welcome to the Brain Games")
    print('What number is missing in the progression? \n')


def get_challenge():
    step = random.randint(1, 10)
    start_point = random.randint(1, 100)
    progression = [start_point]
    for i in range(9):
        progression.append(progression[-1] + step)
    hidden_number_index = (random.randint(0, 9))
    progression.pop(hidden_number_index)
    progression.insert(hidden_number_index, '..')
    challenge = (hidden_number_index, progression, step)
    return challenge


def print_question(challenge):
    question = challenge[1]
    question = str(question).replace(',', ' ')
    print('Question: {}'.format(question[1:-1].replace("'..'", "..")))


def request_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(challenge):
    hidden_number_index, progression, step = challenge
    if progression[0] == '..':
        solution = str(progression[1] - step)
    else:
        solution = str((progression[0] + (hidden_number_index * step)))
    return solution


def is_correct_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False