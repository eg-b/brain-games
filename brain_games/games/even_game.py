import random
import prompt


def greetings():
    print("Welcome to the Brain Games")
    print('Answer "yes" if number even otherwise answer "no". \n')


def get_challenge():
    challenge = random.randint(1, 100)
    print('Question: {}'.format(challenge))
    return challenge


def ask_question():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(num):
    if num % 2 == 0:
        solution = 'yes'
    else:
        solution = 'no'
    return solution


def check_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False
