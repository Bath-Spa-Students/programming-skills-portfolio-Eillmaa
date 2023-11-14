#Movie tickets
text='What is your age? '

while True:
    age=int(input(text))
    if age<3:
        print('Your ticket is free')
    elif age>=3 and age<=12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
        break