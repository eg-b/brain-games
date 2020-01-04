import random
import prompt
import brain_games.cli

def greetings():
    print("Welcome to the Brain Games")
    print("What is the result of the expression? \n")


def generate_question():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    operator = random.choice(('+', '-', '*'))
    challenge = (num1, num2, operator)
    print('Question: {}'.format(challenge))
    return challenge


def ask_question():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(num):
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


def calc_game():
    greetings()
    name = brain_games.cli.run()
    answ_counter = 0
    for i in range(3):
        challenge = generate_question()
        user_answer = ask_question()
        correct_answer = get_solution(challenge)
        if check_answer(user_answer, correct_answer) is not True:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                "Let's try again, {}!"
                .format(user_answer, correct_answer, name)
            )
            break
        else:
            print('Correct!')
            answ_counter += 1
    if answ_counter == 3:
        print('Congratulations, {}!'.format(name))
