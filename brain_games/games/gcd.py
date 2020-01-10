import random


RULES = 'Find the greatest common divisor of given numbers.'
    
    
def get_challenge():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    challenge = '{} {}'.format(num1, num2)
    divisor = num1 % num2
    if divisor == 0:
        solution = str(num2)
    while divisor > 0:
        x = num2 % divisor
        if x == 0:
            solution = str(divisor)
        num2 = divisor
        divisor = x
    return challenge, solution

