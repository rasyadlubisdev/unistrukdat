# prices = list(map(int, input().split()))
prices = [8,4,6,2,3]
# 8
# 4
# 6
# 2
# 3
prices_index = [i for i in range(len(prices))]
prices.reverse()
prices_index.reverse()

compare = []
results = []
simpan = []
buang = []

index_top = len(prices) - 1

length = len(prices)

for _ in range(length):
    if len(prices) > 1:
        print("f1", len(prices))
        if prices[-1] > prices[-2]:
            print("f2", prices[-1], prices[-2])
            results.append(prices[-1] - prices[-2])
            print("if1", prices)
            prices.pop()
            if not len(simpan) == 0:
                prices.append(simpan.pop())
        else:
            print("f3", "www")
            simpan.append(prices.pop())
            buang.append(prices.pop())
            prices.append(simpan.pop())

print(results)









