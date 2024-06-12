"""""
Breakdown:
1. Lakan
L = [i in x -> int]

2. Jinshi
J = [i in y -> int] with y >= x

tapi maks array itu sebanyak x atau len(x)

3. Maomao
M = [i in J -> int] len(M) == x

Selisih
B = max(abs(L[i] - M[i])) dengan i = 1 -> X
"""""

T = int(input())
ans = []

for _ in range(T):
    L = list(map(int, input().split()))
    L.pop()
    J = list(map(int, input().split()))
    J.pop()
    
    L.sort()
    J.sort()

    list1 = abs(L[0])
    
    
    

