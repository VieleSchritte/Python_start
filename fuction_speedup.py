# Meanings x enter. We have function f(x). We need to spped up the calculation process
def f(x):
    f = x + 10
    return(f)

n = int(input())

i = 1
meanings_f = {}

for i in range(1,n+1):
    x = int(input())
    if x in meanings_f:
        print(meanings_f[x])
    else:
        meanings_f[x] = f(x)
        print(meanings_f[x])
    i += 1