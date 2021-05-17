import sys

try:
#    with open ('temp2.txt') as fh:
#        file_data = fh.read ()
#    print (file_data)
    1/0
except FileNotFoundError:
    print('cannot find')
except Exception as err:
#    err = sys.exc_info()
#    for e in err:
    print (err)
    print ("Some other error")

