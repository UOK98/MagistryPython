def sum_distance(fromm, to):
    if fromm > to:
        fromm, to = to, fromm 


    n = fromm
    summ = 0
    while n <= to:
        summ = summ+n
        n = n + 1

    return summ

print('введите число from: ')
fromm = int(input())
print('Введите число to: ')
to = int(input())

summ = sum_distance(fromm, to)

print(summ)