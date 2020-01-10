import random


RULES = 'What number is missing in the progression?'


def get_challenge():
    step = random.randint(1, 10)
    start_point = random.randint(1, 100)
    progression = [start_point]
    for i in range(9):
        progression.append(progression[-1] + step)
    hidden_number_index = (random.randint(0, 9))
    progression.pop(hidden_number_index)
    progression.insert(hidden_number_index, '..')
    challenge = str(progression).replace(',', ' ')
    challenge = challenge[1:-1].replace("'..'", "..")
    if progression[0] == '..':
        solution = str(progression[1] - step)
    else:
        solution = str((progression[0] + (hidden_number_index * step)))
    return challenge, solution
