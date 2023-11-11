#Pets

pet_1 = {'type':'cat',
         'owner':'xiao',
         'color':'black'}
pet_2 = {'type':'bunny',
         'owner':'nuevi',
         'color':'white'}
pet_3 = {'type':'parrot',
         'owner':'scara',
         'color':'blue'}
pet_4 = {'type':'dog',
         'owner':'ayato',
         'color':'black'}

pets = [pet_1,pet_2,pet_3,pet_4]

for pet in pets:
    print ('\nWhat I know about the pet: ')
    for x,y in pet.items():
        print(x+': '+y)