import random
import operator

RULES = 'What is the result of the expression?'


def get_challenge():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    all_operators = {"+": operator.add, "-": operator.sub, '*': operator.mul}
    operation = random.choice(('+', '-', '*'))
    challenge = "{} {} {}".format(num1, operation, num2)
    solution = str(all_operators[operation](num1, num2))
    return challenge, solution
