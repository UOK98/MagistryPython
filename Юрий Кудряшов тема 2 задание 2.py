import random

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys_count = len(boys)
girls_count = len(girls)

if girls_count != boys_count:
    print("Внимание, кто-то может остаться без пары!")
    exit()
   
print("Идеальные пары:")
n = 0
while n < girls_count: 
    n = n + 1
    one_girl = random.choice(girls)
    one_boy = random.choice(boys)
    print(one_girl, "и", one_boy)
    boys.remove(one_boy)
    girls.remove(one_girl)