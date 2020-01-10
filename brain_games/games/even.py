import random


RULES = 'Answer "yes" if number even otherwise answer "no"'


def get_challenge():
    challenge = random.randint(1, 100)
    if challenge % 2 == 0:
        solution = 'yes'
    else:
        solution = 'no'
    return challenge, solution
