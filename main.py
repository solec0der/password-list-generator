# Code will be moved into classes, if basic functionallity is implemented.

class PasswordParameter:
    def __init__(self, display_value, value, allow_multiple):
        self.display_value = display_value
        self.value = value
        self.allow_multiple = allow_multiple

# Create a dictionary to store all user input
user_inputs = {}

# Prepare a list of parameters, which are going to be asked from the user.
password_parameters = [
    PasswordParameter('first name', 'first_name', False),
    PasswordParameter('last name', 'last_name', False),
    PasswordParameter('pet name', 'pet_name', False),
    PasswordParameter('date of birth (format: YYYY/MM/DD)', 'date_of_birth', False),
    PasswordParameter('place of birth', 'place_of_birth', False),
    PasswordParameter('miscellaneous or random words associated with the victim', 'random_words', True)
]

paramters_to_ask = ['first name', 'last name', 'pet name', 'birth year', 'birth month', 'birth day', 'place of birth', '']

for parameter in password_parameters:
    user_input = input('Enter ' + parameter.display_value + ' of the victim ' + ('(Seperate words with semicolons / ' if parameter.allow_multiple else '(') + 'If not given, leave empty): ')

    if user_input.strip():
        user_inputs[parameter.value] = user_input





