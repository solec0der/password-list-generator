# Code will be moved into classes, when basic functionallity is implemented.

class PasswordParameter:
    def __init__(self, display_value, value, allow_multiple):
        self.display_value = display_value
        self.value = value
        self.allow_multiple = allow_multiple

def combine_parameters(parameter_a, parameter_b):
    combinations = []
    combinations.append(parameter_a.lower() + parameter_b.lower())
    combinations.append(parameter_a.lower() + parameter_b.upper())
    combinations.append(parameter_a.upper() + parameter_b.lower())
    combinations.append(parameter_a.upper() + parameter_b.upper())
    return combinations

def append_numbers_to_combination(parameter_a, parameter_b):
    combinations = []
    for i in range(0, 2500):
        combinations.extend(combine_parameters(str(i) + parameter_a, parameter_b))
        combinations.extend(combine_parameters(parameter_a, parameter_b + str(i)))
    return combinations


# Create a dictionary to store all user input
user_inputs = {}

# Prepare a list of parameters, which are going to be asked from the user.
password_parameters = [
    PasswordParameter('first name', 'first_name', False),
    PasswordParameter('last name', 'last_name', False),
    PasswordParameter('nick name', 'nick_name', False),
    PasswordParameter('pet name', 'pet_name', False),
    PasswordParameter('year of birth', 'year_of_birth', False),
    PasswordParameter('month of birth', 'month_of_birth', False),
    PasswordParameter('day of birth', 'day_of_birth', False),
    PasswordParameter('place of birth', 'place_of_birth', False),
    PasswordParameter('miscellaneous or random words associated with the victim', 'random_words', True)
]

# Get inputs from the user
for parameter in password_parameters:
    user_input = input('Enter ' + parameter.display_value + ' of the victim ' + ('(Seperate words with semicolons / ' if parameter.allow_multiple else '(') + 'If not given, leave empty): ')

    if user_input.strip():
        if parameter.allow_multiple:
            user_inputs[parameter.value] = user_input.split(';')    
        else:
            user_inputs[parameter.value] = user_input

# Combine every word with each word (dumb test)
combinations = []

for user_input_a in user_inputs:
    for user_input_b in user_inputs:
        parameter_a = user_inputs[user_input_a]
        parameter_b = user_inputs[user_input_b]

        # Check if parameters contains a list of values
        if isinstance(parameter_a, list) and not isinstance(parameter_b, list):
            for sub_parameter_a in parameter_a:
                combinations.extend(combine_parameters(sub_parameter_a, parameter_b))
                combinations.extend(append_numbers_to_combination(sub_parameter_a, parameter_b))
        elif isinstance(parameter_b, list) and not isinstance(parameter_a, list):
            for sub_parameter_b in parameter_b:
                combinations.extend(combine_parameters(parameter_a, sub_parameter_b))
                combinations.extend(append_numbers_to_combination(parameter_a, sub_parameter_b))
        elif not parameter_a == parameter_b:
            combinations.extend(combine_parameters(parameter_a, parameter_b))
            combinations.extend(append_numbers_to_combination(parameter_a, parameter_b))

# Output amount of passwords generated
print(len(combinations))

# Figure out how to write to file
with open('password_list.txt', 'w') as output_file:
    for combination in combinations:
        output_file.write(combination + "\n")
