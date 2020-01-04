import random
import prompt
import brain_games.cli

def greetings():
    print("Welcome to the Brain Games")
    print('Answer "yes" if number even otherwise answer "no". \n')


def get_challenge():
    challenge = random.randint(1, 100)
    print('Question: {}'.format(challenge))
    return challenge


def ask_question():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def get_solution(num):
    if num % 2 == 0:
        solution = 'yes'
    else:
        solution = 'no'
    return solution


def check_answer(user_answer, solution):
    if user_answer == solution:
        return True
    else:
        return False


def even_game():
    greetings()
    name = brain_games.cli.run()
    answ_counter = 0
    for i in range(3):
        challenge = get_challenge()
        user_answer = ask_question()
        solution = get_solution(challenge)
        if check_answer(user_answer, solution) is not True:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                "Let's try again, {}!"
                .format(user_answer, solution, name)
            )
            break
        else:
            print('Correct!')
            answ_counter += 1
    if answ_counter == 3:
        print('Congratulations, {}!'.format(name))
