import random
import prompt
import brain_games.cli


def generate_question():
    num = random.randint(1, 100)
    print('Question: {}'.format(num))
    return num


def ask_question():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def is_even(num):
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


def game():
    name = brain_games.cli.run()
    answ_counter = 0
    for i in range(3):
        num = generate_question()
        user_answer = ask_question()
        correct_answer = is_even(num)
        check_answer(user_answer, correct_answer)
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
