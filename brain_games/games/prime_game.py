import random
import prompt


def greetings():
    print("Welcome to the Brain Games")
    print('Answer "yes" if given number is prime. Otherwise answer "no". \n')


def get_challenge():
    challenge = random.randint(1, 500)
    return challenge


def print_question(challenge):
    print('Question: {}'.format(challenge))


def request_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(challenge):
    for i in range(2, challenge):
        if not challenge % i:
            solution = 'no'
            return solution
    solution = 'yes'
    return solution


def check_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False
