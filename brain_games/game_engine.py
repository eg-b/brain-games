import brain_games.games
import brain_games.cli


def run(game_name):
    game_name.greetings()
    user_name = brain_games.cli.run()
    for i in range(3):
        challenge = game_name.get_challenge()
        game_name.print_question(challenge)
        user_answer = game_name.request_answer()
        solution = game_name.get_solution(challenge)
        if game_name.is_correct_answer(user_answer, solution) is not True:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                "Let's try again, {}!"
                .format(user_answer, solution, user_name)
            )
            break
        else:
            print('Correct!')
            print('Congratulations, {}!'.format(user_name))
