import brain_games.games
import brain_games.cli
import prompt


def run(game_name):
    print('Welcome to the Brain Games\n{} \n'.format(game_name.RULES))
    user_name = brain_games.cli.run()
    for i in range(3):
        challenge, solution = game_name.get_challenge()
        print('Question: {}'.format(challenge))
        user_answer = prompt.string('Your answer: ')
        if user_answer != solution:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                "Let's try again, {}!"
                .format(user_answer, solution, user_name)
            )
            break
        else:
            print('Correct!')
    else:
        print('Congratulations, {}!'.format(user_name))
