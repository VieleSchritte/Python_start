# Choosing only repeated numbers in the list

list_one = [int(i) for i in input().split()]
if len(list_one) == 1:
    print()
list_one = sorted(list_one)
list_one += '@'
list_two = []
i = 0
n = 1
for i in range(len(list_one) - 1):
    if (list_one[i] == list_one[i+1])and(n == 1):
        list_two.append(list_one[i])
        n += 1
        i += 1
    elif (list_one[i] == list_one[i+1])and(n != 1):
        i += 1
        n += 1
        continue
    elif list_one[i] != list_one[i+1]:
        n = 1
        i += 1
k = 0
for k in range(len(list_two)):
    print(list_two[k], end = ' ')