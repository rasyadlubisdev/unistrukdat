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
    L = input().split()
    L.pop()
    La = []
    for value in L:
        La.append([value, 'La'])
    J = input().split()
    J.pop()
    Ji = []
    for value in J:
        Ji.append([value, 'Ji'])
    
    # temp = [i for i in La]
    # for value in Ji:
    #     temp.append(value)
    temp = Ji + La
    # print("Ji", Ji)
    # print("La", La)

    # print("temp", temp)
    # print("temp", max(temp))
    
    save = []
    ans_temp = []
    temp.sort()
    while len(ans_temp) != len(L) and len(temp) != 0:
        top = temp[-1]
        bottom = temp[0]
        print("temp", temp)
        print("t", top)
        print("b", bottom)
        if top[1] == bottom[1]:
            save.append(bottom)
            temp.remove(bottom)
            continue
        # if int(top[0]) == int(top[0])
            
        selisih = abs(int(top[0]) - int(bottom[0]))
        ans_temp.append(selisih)
        temp.remove(top)
        temp.remove(bottom)

        if len(save) != 0:
            for _ in range(len(save)):
                temp.append(save.pop())

        # print("selisih", selisih)
                
    ans.append(ans_temp)

# # print("L", L)
# # print("J", J)
# # print("ans", ans)

# union = [[1, 'A'], [3, 'B'], [0, 'A'], [1, 'B']]
# union.sort()
# print(union)

# # print(union)
# # maks = max(union)
# # print(maks)
# # union.remove(maks)
# # print(union)

for an in ans:
    total = sum(an)
    print(f"Maksimum total selisihnya {total} poin.")

