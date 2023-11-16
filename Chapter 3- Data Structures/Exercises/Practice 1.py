#Write a program to remove all occurrences of item 20 from the given list

list1 = [5, 20, 15, 20, 25, 50, 20]
remove=20

for num in list1:
    if num==remove:
        list1.remove(remove)

print (list1)