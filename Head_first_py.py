person3 = {'Name':'Ford prefect',
            'Gender': 'Male',
            'Occupation':'Researcher',
            'Home planet':'Betelgeuse Seven'
}
#print(person3['Gender'])
string = input("Type a line\n")
vowels ="aeiou"
vowels_list = list(vowels)
#found = {
#    'a' : 0,
#    'e' : 0,
#    'i' : 0,
#    'o' : 0,
#    'u' : 0
#}
found ={}

for words in string:
    if words in vowels_list:
#        if words not in found:
#            found[words] = 0        
        found.setdefault(words, 0)
        found[words] += 1
#        print(words)

#print(found)
for k,v in sorted(found.items()):
    print(k,v)