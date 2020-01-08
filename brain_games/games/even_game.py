import random
import prompt


def greetings():
    print("Welcome to the Brain Games")
    print('Answer "yes" if number even otherwise answer "no". \n')


def get_challenge():
    challenge = random.randint(1, 100)
    return challenge


def print_question(challenge):
    print('Question: {}'.format(challenge))


def request_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(challenge):
    if challenge % 2 == 0:
        solution = 'yes'
    else:
        solution = 'no'
    return solution


def is_correct_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False
