#name = input ('type your name \n')
#color = input ('type your favourite color \n')
#print (name + ' likes ' + color)
#weight_pounds = input ('type your weight in pounds \n')
#weight = int (input ('Weight:'))
#unit = input ('(L)bs or (K)g:')
#if unit.lower() == 'k':
#    output = weight / 0.4536
#    print (f"Weight is {output} pounds")
#elif unit.lower() == 'l':
#    output = weight * 0.4536
#    print (f"Weight is {output} Kg")
#else:
#    print ('Incorrect units')

#weight_kg = float (weight_pounds) * 0.4536
#print ('your weight in Kg is :')
#print (weight_kg )

#house_price = 10 ** 6
#good_credit = False
#print ('The down payment is')
#if good_credit:
#    down_payment = 0.1 * house_price
#else:
#    down_payment = 0.2 * house_price
#print (f"Down payment is {down_payment}")
#name_length = len(name)
#if name_length < 3:
#    print ('Name must be atleast 3 characters long')
#elif name_length > 50:
#    print ('Name can be a max of 50 chars')
#else :
#    print ('name looks good')
start_count = 0
stop_count = 0 
while 1:
    input_command = input ('>').lower()
    if input_command == 'help':
        print ('Start : to start the car \nStop: to stop the car \nQuit: to exit')
    elif input_command == 'start' :
        if start_count == 0:
            print ('The car has started')
        else:
            print ('The car has already started')
        start_count += 1
    elif input_command == 'stop':
        if stop_count == 0:
            print ('The car has stopped')
        else:
            print ('The car has already stopped')
        stop_count += 1
    elif input_command == 'quit':
        print ('You have exited')
        break
    else:
        print ('Type a valid command')

