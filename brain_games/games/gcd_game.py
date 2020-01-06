import random
import prompt


def greetings():
    print("Welcome to the Brain Games")
    print('Find the greatest common divisor of given numbers. \n')


def get_challenge():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    challenge = (num1, num2)
    print('Question: {}'.format(str(challenge)))
    return challenge


def ask_question():
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


def check_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False
