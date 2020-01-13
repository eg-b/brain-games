import random


RULES = 'What number is missing in the progression?'


def get_challenge():
    step = random.randint(1, 10)
    start_point = random.randint(1, 100)
    progression = []
    for i in range(10):
        progression.append(start_point + (i * step))
    hidden_number_index = (random.randint(0, 9))
    solution = str(progression[hidden_number_index])
    progression[hidden_number_index] = '..'
    challenge = ' '.join(str(i) for i in progression)
    return challenge, solution
