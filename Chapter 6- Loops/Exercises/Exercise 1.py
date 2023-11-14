#Pizza toppings
text='''\nEnter a topping you would like to add on your pizza
Enter quit when finished:'''

while True:
    pizza_topping=input(text)
    if pizza_topping != 'quit':
        print('I will add '+pizza_topping+' to your pizza')
    else:
        break