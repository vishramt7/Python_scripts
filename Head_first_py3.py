
#todos = open('todos.txt','a')
#todos = open('todos.txt')
#print ('Feed the cat', file=todos)

with open('todos.txt') as tasks:
    for chore in tasks:
        print (chore, end='')
#for lines in todos:
#    print(lines, end='')
    
#todos.close()

# This is a practice func
#def log_request (req: 'flask request', res:str) -> None:
   with open ('vsearch.log','a') as file_handle:
       str =[]
       for line in file_handle:
           line_list = line.split('|')
           str.append(line_list)
        return str(contents
#       print(req res, file = file_handle)
