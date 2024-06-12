N = int(input())
tas = []

for _ in range(N):
    B, M = map(int, input().split())
    tas.append((B, M))

X = int(input())

# sorted_list = sorted(tas, key=lambda x: x[1], reverse=True)
tas.reverse()

for i in range(len(tas)-1, -1, -1):
    if tas[i][0] == X:
        tas.pop()
        print(N - len(tas))
        break
    if i == 0:
        print("Barangnya gak ada beb")
    # print(tas[i][0])
    tas.pop()
# print(tas)



