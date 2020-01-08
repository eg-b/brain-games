#!/usr/bin/env python3
from brain_games.games import calc_game
from brain_games.game_engine import run_game


def main():
    run_game(calc_game)


if __name__ == '__main__':
    main()
