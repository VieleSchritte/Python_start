gene = input()
gene.lower()
gene += '@'
i = 0
n = 1
gene_new = gene[0]

while i < len(gene) - 1:
    if gene[i] == gene[i+1]:
        n += 1
        i += 1
        continue
    elif (gene[i] != gene[i+1])and(i != len(gene) - 2):
        gene_new += (str(n) + gene[i+1])
        n = 1
        i += 1
        continue
    elif (gene[i] != gene[i+1])and(i == len(gene) - 2):
        gene_new += str(n)
    n = 1
    i += 1
    
print(gene_new)