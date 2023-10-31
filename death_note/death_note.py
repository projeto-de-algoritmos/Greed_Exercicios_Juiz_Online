n_dias, n_nomes_por_pagina = map(int,input().split())
a = list(map(int,input().split()))
result = []
sum1=0
 
for i in range(n_dias):
    sum1+=a[i]
    result.append(sum1//n_nomes_por_pagina)
    sum1=sum1%n_nomes_por_pagina

print(*result)
