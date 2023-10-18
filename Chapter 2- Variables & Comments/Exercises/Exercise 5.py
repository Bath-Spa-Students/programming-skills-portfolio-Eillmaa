#USB Shopper
#The amount she has and the price of the USB sticks
her_amount = 50
price = 6

#Calculate how many she's able to buy and print it
able_to_buy = (her_amount/price)
print ('Can buy:',int(able_to_buy),'USB sticks')

#Calculate how much she has left and print it
amount_left1 = (her_amount-price*able_to_buy)
print ('Pounds remianing: £',int(amount_left1))
