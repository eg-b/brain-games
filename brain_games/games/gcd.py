import random
import prompt


def greetings():
    print("Welcome to the Brain Games")
    print('Find the greatest common divisor of given numbers. \n')


def get_challenge():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    challenge = (num1, num2)
    return challenge


def print_question(challenge):
    num1, num2 = challenge
    print('Question: {} {}'.format(str(num1), str(num2)))


def request_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(challenge):
    num1, num2 = challenge
    divisor = num1 % num2
    if divisor == 0:
        solution = num2
        return str(solution)
    while divisor > 0:
        x = num2 % divisor
        if x == 0:
            solution = divisor
            return str(solution)
        num2 = divisor
        divisor = x


def is_correct_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False