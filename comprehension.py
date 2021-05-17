evens = []
#evens = [ num for num in data if not num % 2]

words = []
#words = [ num for num in data if isinstance (num, str)]

title = []
#title = [ word.title() for word in data ]

#vowels = {'a', 'e', 'i', 'o', 'u'}
#message = "Don't forget to pack your towel."

#found = set()
#for v in vowels:
#    if v in message:
#        found.add(v)
#print (found)
#found2 = { v for v in vowels if v in message }
#print (found2)

import requests
urls = ('http://headfirstlabs.com', 'http://oreill.com', 'http://twitter.com')

for resp in [requests.get(url) for url in urls]:
    print (len(resp.content), '->', resp.status_code, '->', resp.url)

