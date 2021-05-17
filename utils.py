import random

def find_max(input):
    max_val = input[0]
    for values in input:
        if values > max_val:
            max_val = values
    return max_val

class Random:
    def roll(self):
        int1 = random.randint(1,6)
        int2 = random.randint(1,6)
        return int1, int2

def search_letters(input_string:str, search_against:str="aeiou") -> set:
    """ Returns letters of search_against found in the input_string"""
    found = set(search_against).intersection(set(input_string))
    return (found)