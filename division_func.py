#The function deletes odd numbers from the given list and even numbers completely divides by 2

def modify_list(lst):
    i = len(lst)
    l = len(lst)-1
    for i in range(l,-1,-1):
        if lst[i] % 2 != 0:
            del lst[i]
        else:
            lst[i] = lst[i] // 2

lst = [1,2,3,4,5]
modify_list(lst)
print(lst)