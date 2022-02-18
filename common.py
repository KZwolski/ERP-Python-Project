""" Common module
implement commonly used functions here
"""

import random

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    generated = ''
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_characters = "!@#$%^&*?/"
    generated = random.choice(lower_letters)+random.choice(upper_letters)+random.choice(numbers)+random.choice(numbers)+random.choice(upper_letters)+random.choice(lower_letters)+random.choice(special_characters)+random.choice(special_characters)
    for i in range(len(table)):    
        if generated not in table[i][0]:
            return generated
    else: 
        generate_random(table)

