import pprint
from utils import search_letters

def vowel_finder(input_string:str) -> set:
    """Displays any vowel in the entered string"""
    #string = input("Type a line\n")
    vowels = "aeiou"
    vowels_set = set(vowels)
    found = vowels_set.intersection(set(input_string))
    #for vowel in found:
    #    print(vowel)
    #return bool(found)
    return (found)

#print(found)
#for letter in string:
#    if (set(letter))
#    found.append(letter)
people = {}
people['Ford'] ={'Name': 'Ford Prefect', 'Gender': 'Male', 
    'Occupation': 'Researcher', 'Home Planet': 'Betelgeuse Seven'}
people['Arthur'] = {'Name': 'Arthur Dent','Gender': 'Male',
    'Occupation': 'Sandwich-Maker','Home Planet': 'Earth'}
people['Trillian'] = {'Name': 'Tricia McMillan', 'Gender': 'Female', 
    'Occupation': 'Mathematician', 'Home Planet': 'Earth'}
people['Robot'] = {'Name': 'Marvin', 'Gender': 'Unknown', 
    'Occupation': 'Paranoid Android', 'Home Planet': 'Unknown'}

#print(people)
#pprint.pprint(people['Ford']['Name'])
#string = input("Type a line\n")
string = "galaxy"
#print (search_letters(string))
#print(help(search_letters))
for k,v in people.items():
    print ("This is the output", k, v)
