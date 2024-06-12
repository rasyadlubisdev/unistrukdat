T = int(input())
N = list(map(int, input().split()))
temp = []

for char in N:
    if char in temp:
        continue
    else:
        temp.append(char)
print(len(temp))

