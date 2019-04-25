"""
You quickly need to modify this function to return True even if user inputs uppercase 'Y'. However, your code
editor has a bug and only lets you add code to the end of the function's body (in this case, only inside of function).
What can u do?
"""


def prompt_consent():
    print('Agree? [y/N]')
    try:
        user_input = input()
        return user_input == 'y'
    except KeyboardInterrupt:
        return False
