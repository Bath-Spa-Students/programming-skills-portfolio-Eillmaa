#Control structure

purchase = float(input('Enter purchase amount:'))

if purchase > 200:
    discount = '50%'
else:
    discount = 0
print('Discount recieved: ' + str(discount))
if purchase > 200:
    discount = (purchase/2)
else:
    discount = purchase
print('Amount: $'+ str(discount))

#Nested Disicion structure
experiece = int(input('Enter how many years of experiece you have:'))
degree = str(input('Enter your qualifications:'))

#Company hiring employees asks for experiece in their work feild and your degree
if experiece > 4:
    if degree == ('masters'):
         print('You are qualified enough')
    else:
        print('You are not qualified')
else:
    print ('You are not experieced enough')

#Grading system
marks = int(input('Enter your marks out of 200:'))
if marks <= 50:
    print ('You failed')
elif marks <= 100:
    print ('You received a E')
elif marks <= 125:
    print ('You recieved a D')
elif marks <= 150:
    print ('You recieved a C')
elif marks <= 175:
    print ('You recived an B')
elif marks <= 194:
    print ('You recieved an A')
else:
    print ('You recieved an A* good job!')