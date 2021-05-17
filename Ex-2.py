from utils import *

price = [5, 2, 5, 7, 2,15, 18]
print (find_max(price))

#total = 0
#for i in price:
#    total += i
#    print('x' * i)
#print (total)
#new_price_list = price.sort
#max = price[0]
#for i in range(len(price)):
#    if price[i] > max:
#        max = price[i]
#print (max)

# Printing duplicates
#for items in price:
#    if price.count(items) > 1:
#        price.remove(items)
#        print (items)

#print (price)

def Dictionary_function (Input_phone_no):
    Dictionary = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
    }
    output = ""
    for i in Input_phone_no:
        output += Dictionary.get(i, "!") + " "
    return output
    
#Input_phone = input("Phone:")
#print (Dictionary_function(Input_phone))


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"I am {self.name}")

new_person = Person("Visham")
new_person.talk()

new_person2 = Person("Josh")
new_person2.talk()

random_num_gen = Random()
print(random_num_gen.roll())

from pathlib import Path

path = Path()
for files in path.glob('*.xlsx'):
    print(files)