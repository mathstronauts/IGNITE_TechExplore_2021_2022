"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""
#print greetings
print('Welcome to my simple calculator!')

#get user inputs
operation = input('Please enter operation(+,-,*,/,**): ')
if (operation == '**'):
    base = input('Please enter base integer: ')
    exp = input('Please enter exponent: ')
else:
    first_num = input('Please enter first integer: ')
    second_num = input('Please enter second integer: ')

#if sum operation
if(operation == '+'):    
    #sum the two numbers
    result = int(first_num) + int(second_num)

    #output the sum to the user
    print('The sum of the two numbers is', result)
	
#if subtract operation
elif(operation == '-'):    
    #subtract the two numbers
    result = int(first_num) - int(second_num)

    #output the difference to the user
    print('The difference of the two numbers is', result)

#if multiply operation
elif(operation == '*'):    
    #multiply the two numbers
    result = int(first_num) * int(second_num)

    #output the product to the user
    print('The product of the two numbers is', result)

#if divide operation
elif(operation == '/'):    
    #divide the two numbers
    result = int(first_num) / int(second_num)

    #output the quotient to the user
    print('The quotient of the two numbers is', result)

#if exponent operation USING FOR LOOP
elif(operation == '**'):    
    #base to the power of exponent
    result = 1
    for i in range(int(exp)):
        result = result * int(base)

    #output the total to the user
    print(base, 'to the power of', exp, 'is', result)

#operation not valid
else:
    print('Sorry operation is not recognized!')

print('Thanks for using my calculator!')
