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
    hidden_number = (random.randint(0, 9))
    progression.pop(hidden_number)
    progression.insert(hidden_number, '..')
    challenge = (hidden_number, progression, step)
    return challenge


def print_question(challenge):
    question = challenge[1]
    question = str(question).replace(',', ' ')
    print('Question: {}'.format(question[1:-1].replace("'..'", "..")))


def request_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(challenge):
    hidden_number, progression, step = challenge
    solution = str(progression[0] + (hidden_number * step))
    return solution


def check_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False
