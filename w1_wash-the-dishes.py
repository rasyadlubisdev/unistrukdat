N = int(input())

piring_kotor = [i for i in range(N, 0, -1)]
piring_sabun = []
piring_bilas = []

M = int(input())

for _ in range(M):
    C, D = map(int, input().split())
    if C == 1:
        ambil = D
        if D > len(piring_kotor):
            ambil = len(piring_kotor)
        for _ in range(ambil):
            piring_sabun.append(piring_kotor.pop())
    elif C == 2:
        ambil = D
        if D > len(piring_sabun):
            ambil = len(piring_sabun)
        for _ in range(ambil):
            piring_bilas.append(piring_sabun.pop())

max_height = max(len(piring_kotor), len(piring_sabun), len(piring_bilas))
while len(piring_kotor) < max_height:
    piring_kotor.append(" ")
while len(piring_sabun) < max_height:
    piring_sabun.append(" ")
while len(piring_bilas) < max_height:
    piring_bilas.append(" ")
#if element pertama (paling bawah) bukan angka, tetapi " " -> list[-1] = "-"
if piring_kotor[0] == " ":
    piring_kotor[-1] = "-"
if piring_sabun[0] == " ":
    piring_sabun[-1] = "-"
if piring_bilas[0] == " ":
    piring_bilas[-1] = "-"

for i in range(max_height-1, -1, -1):
    print(f"{piring_kotor[i]}\t{piring_sabun[i]}\t{piring_bilas[i]}")