import random
import prompt


def greetings():
    print("Welcome to the Brain Games")
    print("What is the result of the expression? \n")


def get_challenge():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    all_operators = ('+', '-', '*')
    operator = random.choice(all_operators)
    challenge = "{} {} {}".format(num1, operator, num2)
    print('Question: {}'.format(challenge))
    return challenge


def ask_question():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(challenge):
    solution = str(eval(challenge))
    return solution


def check_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False
