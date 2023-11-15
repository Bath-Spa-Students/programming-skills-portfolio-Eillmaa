#T-Shirt
def make_shirt(size, message):
    print('The size of the shirt is '+size)
    print('The message printed on the shirt is: '+message)

shirt_size='small'
shirt_message='I love cats'

#Positional argument
make_shirt(shirt_size,shirt_message)

#Keyword argument
make_shirt(size='medium',message='Cats are the cutest')