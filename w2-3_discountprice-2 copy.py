# prices = list(map(int, input().split()))
prices = [8,4,6,2,3]
temp_stack = []
for i, price in enumerate(prices):
    if len(temp_stack) > 0:
        last_index = temp_stack.pop()
        if prices[last_index] >= price:
            prices[last_index] = prices[last_index] - price
        else:
            sisa = prices[2:5]
            print(sisa)
            for future_value in sisa:
                print(future_value)
                if prices[last_index] >= future_value:
                    prices[last_index] = prices[last_index] - future_value
                    print(prices[last_index], future_value)
    temp_stack.append(i)

print(prices)