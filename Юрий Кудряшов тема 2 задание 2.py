import random

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys =  sorted(boys)
girls = sorted(girls)

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
    exit()
   
print("Идеальные пары:")
n = 0
while n < len(boys): 
    print(girls[n], "и", boys[n])
    n = n + 1