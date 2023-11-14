#Deli
sandwich_orders=['tikka sandwich','vegetable sandwich','egg sandwich','chilli sandwich']
finished_sandwiches=[]

while sandwich_orders:
    making=sandwich_orders.pop()
    print('Your '+making+' is currently being made.')
    finished_sandwiches.append(making)
for sandwich in finished_sandwiches:
    print('Your '+sandwich+' is finished.')