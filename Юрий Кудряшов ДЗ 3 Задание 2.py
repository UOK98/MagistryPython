def trim_and_repeat(string, offset, repetitions):
    n = 0
    newstring = ''
    string = string[offset:]
    while n < repetitions: 
        newstring = newstring + string
        n = n + 1
    return newstring




print('Input your string: ')
string = input()
print('Input offset: ')
offset = int(input())
print('Input repetitions count: ')
reppetitions = int(input())

resultstring = trim_and_repeat(string, offset, reppetitions)

print(resultstring)

