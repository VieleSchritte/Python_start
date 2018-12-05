# We have the matrix in the input. Each member of the resulting matrix in the (i,j)-position
# is a sum of first matrix members on the positions (i-1,j), (i+1,j), (i, j-1), (i, j+1). 

i = []
sp = []
while i != ['end']:
    i = input().split(' ')
    sp.append(i)
del [sp[len(sp)-1]]

i = 0
j = 0

Len_sp = len(sp)
Len_row = len(sp[0])

for i in range(Len_sp):
    for j in range(len(sp[i])):
        sp[i][j] = int(sp[i][j])

result = []
result = [[0]*(Len_row) for i in range(Len_sp)]
print()
sp_ind = [[0,1],[0,-1],[1,0],[-1,0]]
i = 0
j = 0
new_i = 0
new_j = 0

k = 0

for i in range(Len_sp):
    for j in range(Len_row):
        for k in range(len(sp_ind)):
            new_i = (i + sp_ind[k][0])%Len_sp
            new_j = (j + sp_ind[k][1])%Len_row
            result[i][j] += sp[new_i][new_j]
            
for row in result:
    for elem in row:
        print(elem, end = ' ')
    print()