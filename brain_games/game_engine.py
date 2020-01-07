import brain_games.games
import brain_games.cli


def run_game(game_name):
    game_name.greetings()
    user_name = brain_games.cli.run()
    win_counter = 0
    for i in range(3):
        challenge = game_name.get_challenge()
        game_name.print_question(challenge)
        user_answer = game_name.request_answer()
        solution = game_name.get_solution(challenge)
        if game_name.check_answer(user_answer, solution) is not True:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                "Let's try again, {}!"
                .format(user_answer, solution, user_name)
            )
            break
        else:
            print('Correct!')
            win_counter += 1
    if win_counter == 3:
        print('Congratulations, {}!'.format(user_name))
