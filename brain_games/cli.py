import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}! \n'.format(user_name))
    return user_name
