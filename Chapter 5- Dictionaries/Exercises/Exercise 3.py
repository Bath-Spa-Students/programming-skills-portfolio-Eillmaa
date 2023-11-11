#Glossary 2

glossary = {'Variable':'A name that represents value stored in the computer memory.',
            'List':'An object that contains multiple data items',
            'Dictionary':'An object that stores a collection of data',
            'Print':'A function that shows the result of the code written',
            'Input':'A built in function that gets input from the user by showing a promt',
            'Float':'A function that converts values into floating point numbers',
            'Loop':'Repeating somthing overand over unitl a particular condition is satisfied',
            'Boolean':'It is used to represent the truth value of an expression',
            'Comment':'A free text that is ignored when the code is run',
            'Key':'First item of a key-value pair in a dictionary'}

for x, y in glossary.items():
    print(f'\n{x.title()}: {y}')