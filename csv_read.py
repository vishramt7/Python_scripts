
import csv
import pprint

with open ('music.csv') as file_input:
#    for lines in file_input:
#        print (lines, sep='temp')
    #print (file_input.read())

#    for lines in csv.reader(file_input):
#        print (lines)

#    for lines in csv.DictReader(file_input):
#        print (lines)

    ignore = file_input.readline()
    age_music = {}
    for line in file_input:
        a, g , m = line.strip().split(',')
        M = m.upper()
#        age_music [a] = m
        print (a,g,M)

#pprint.pprint(age_music)

flighsts = {}
#for key, values in age_music.items():
#    print (key, values)
#    flighsts[key] = values.title()
#pprint.pprint (flighsts)

original_list = ["Perl", "Python", "C", "Shell"]
#for items in original_list:
#    print (items)


new_list = []
new_list = [ items*2 for items in original_list ]
#new_list = [for new_vals in age_music.values()]
#print (new_list)


