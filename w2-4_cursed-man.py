T = int(input())
N = list(map(int, input().split()))

temp = []
biggest = max(N)

for num in N:
    if num < biggest:
        print('')
        temp.append(num)
    else:
        print(num)
