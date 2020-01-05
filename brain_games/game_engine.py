import brain_games.games.even_game
import brain_games.games.calc_game
import brain_games.cli


def run_game(game_name):
    game_name.greetings()
    name = brain_games.cli.run()
    answ_counter = 0
    for i in range(3):
        challenge = game_name.get_challenge()
        user_answer = game_name.ask_question()
        solution = game_name.get_solution(challenge)
        if game_name.check_answer(user_answer, solution) is not True:
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
