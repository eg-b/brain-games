# Makefile
install:
	poetry install 

configure:
	@poetry install

lint:
	poetry run flake8 brain_games
