prices = list(map(int, input().split()))
temp_stack = []

for i, price in enumerate(prices):
    while temp_stack and prices[temp_stack[-1]] >= price:
        past_index = temp_stack.pop()
        prices[past_index] -= price
    temp_stack.append(i)

print(prices)