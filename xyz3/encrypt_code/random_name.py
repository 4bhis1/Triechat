import random
import string


def random_name():  # define the function and pass the length as argument
    # Print the string in Lowercase
    length = 6
    result = ''.join((random.choice(string.ascii_lowercase)
                     for x in range(length)))  # run loop until the define length

    return result
