import random
import operator


RULES = 'What is the result of the expression?'
ALL_OPERATORS = [("+", operator.add), ("-", operator.sub), ('*', operator.mul)]


def get_challenge():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    operation = random.choice(ALL_OPERATORS)
    challenge = "{} {} {}".format(num1, operation[0], num2)
    solution = str(operation[1](num1, num2))
    return challenge, solution
