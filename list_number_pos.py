#List and number are entering. Positions if this number in the given list printed.

list_p = [i for i in input().split()]
x = int(input())
sp = []
for i in range(len(list_p)):
    if int(list_p[i]) == x:
        sp.append(i)
if len(sp) == 0:
    print('Отсутствует')
else:
    for i in sp:
        print(i, end = ' ')