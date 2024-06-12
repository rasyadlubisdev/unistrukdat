N = int(input())

beli_buku = []
ans = []


for _ in range(N):
    S = input().split()
    if S[0] == "BELI":
        beli_buku.append(S[1])
    elif S[0] == "JUAL":
        beli_buku.remove(S[1])
    elif S[0] == "PRINT":
        temp = [i for i in beli_buku]
        for i in temp:
            ans.append(i)
        ans.append("---")

for i in ans:
    print(i)