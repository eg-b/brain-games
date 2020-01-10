import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def get_challenge():
    challenge = random.randint(1, 500)
    for i in range(2, challenge):
        if not challenge % i:
            solution = 'no'
    solution = 'yes'
    return challenge, solution
