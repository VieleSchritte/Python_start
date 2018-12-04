# Entering in one line members of the list, after which forming a new list that consists of sums of neighbors of each member.
# If these are the two extreme members, then the neighbor from the empty end is considered to be the member that stands in the opposite edge of the list.
a = [int(i) for i in input().split()]
b = [0]*len(a)
for i in range(len(a)):
    if len(a) == 1:
        b[i] = a[i]
        break
    elif i == 0:
        b[i] = a[i+1] + a[-1]
    elif (i != 0)and(i != (len(a)-1)):
        b[i] = a[i-1] + a[i+1]
    elif i == len(a)-1:
        b[i] = a[i-1] + a[0]
    i += 0
for i in range(len(b)):
    print(b[i], end = ' ')  