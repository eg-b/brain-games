import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def get_challenge():
    challenge = random.randint(1, 500)
    if not is_prime(challenge):
        solution = 'no'
    else:
        solution = 'yes'
    return challenge, solution


def is_prime(num):
    for i in range(2, num):
        if not num % i:
            return False
        else:
            return True
