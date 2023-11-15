#No Pastrami
print('Deli has run out of pastrami sandwich')
sandwich_orders=['tikka sandwich','pastrami sandwich','vegetable sandwich','pastrami sandwich','egg sandwich','pastrami sandwich','chilli sandwich']
finished_sandwiches=[]

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    making=sandwich_orders.pop()
    print('Your '+making+' is currently being made.')
    finished_sandwiches.append(making)
for sandwich in finished_sandwiches:
    print('Your '+sandwich+' is finished.')