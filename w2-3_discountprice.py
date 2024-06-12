prices = list(map(int, input().split()))
#as stack
prices.reverse()
#as temp_stack
simpan = []
results = []

while not len(prices) == 0:
    # price = prices.pop()
    global price
    if len(simpan) == 0:
        price = prices.pop()
    print("F1", price, prices[-1])
    if price >= prices[-1]:
        results.append(price - prices[-1])
        if not len(prices) == 0:
            if not len(simpan) == 0:
                while (not len(simpan) == 0):
                    print("test")
                    prices.append(simpan.pop())
        # if (not len(prices) == 0) and (not len(simpan) == 0):
        #     prices.append(simpan.pop())
    else:
        simpan.append(prices.pop())
    print(price, prices, simpan)
    if len(prices) == 1 and len(simpan) == 0:
        print("WOIII", price, prices, simpan)
        results.append(prices.pop())

    if len(prices) == 0:
        results.append(price)
        if len(simpan) == 0:
            break
        else:
            simpan.reverse()
            while(not len(simpan) == 0):
                results.append(simpan.pop())


print(prices)
print(results)
#8 7 4 2 8 1 7 7 10 1