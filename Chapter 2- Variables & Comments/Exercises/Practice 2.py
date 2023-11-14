#Total marks
print('Enter you marks:')
maths=int(input())
english=int(input())
science=int(input())
history=int(input())
computer=int(input())

sum=(maths+english+science+history+computer)

average=(sum/5)
percentage=(sum/500)*100

print('Average mark:',average)
print('Percentage:',percentage)