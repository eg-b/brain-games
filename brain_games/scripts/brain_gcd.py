#!/usr/bin/env python3
from brain_games import games, game_engine


def main():
    game_engine.run(games.gcd)


if __name__ == '__main__':
    main()
