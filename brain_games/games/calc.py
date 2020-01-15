import random
import operator


RULES = 'What is the result of the expression?'
ALL_OPERATORS = [("+", operator.add), ("-", operator.sub), ('*', operator.mul)]


def get_challenge():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    sign, operation = random.choice(ALL_OPERATORS)
    challenge = "{} {} {}".format(num1, sign, num2)
    solution = str(operation(num1, num2))
    return challenge, solution
