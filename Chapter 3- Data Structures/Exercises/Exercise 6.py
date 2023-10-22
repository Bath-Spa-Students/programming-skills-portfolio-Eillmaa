#Shrinking Guest List
#Program from previous exercise
invited = ['xiao','neuvi','haitham','ayato']
print ('Hey ' + (invited[0]) + '!, you are invited to dinner')
print ('Hey ' + (invited[1]) + '!, you are invited to dinner')
print ('Hey ' + (invited[2]) + '!, you are invited to dinner')
print ('Hey ' + (invited[3]) + '!, you are invited to dinner'+ '\n')
print ((invited[3]) + ' can not make it to dinner' + '\n')
invited[3]='scara'
print ('Hey ' + (invited[0]) + '!, you are invited to dinner')
print ('Hey ' + (invited[1]) + '!, you are invited to dinner')
print ('Hey ' + (invited[2]) + '!, you are invited to dinner')
print ('Hey ' + (invited[3]) + '!, you are invited to dinner' + '\n')

#Print a message saying you can only invite 2 people
print ('Sorry, I can only invite 2 people for dinner' + '\n')

#Print a message to the people you can't invite and apologize to them and use pop() to remove their name from the list
print ('Sorry ' + (invited[1]) + ', there is no space at the table')
invited.pop(1)
print ('Sorry ' + (invited[1]) + ', there is no space at the table' + '\n')
invited.pop(1)

#Print a message to the 2 people who are invited
print ('Hey ' + (invited[0]) + ', you are still invited to dinner')
print ('Hey ' + (invited[1]) + ', you are still invited to dinner')

#Use del to remove the 2 people from the list
del invited[0]
del invited[0]

#Print the list to make sure you have an empty list
print (invited)