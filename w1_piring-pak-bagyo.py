def add(stack, value, count):
    for _ in range(count):
        stack.append(value)

def delete(stack, count):
    if not len(stack) == 0:
        for _ in range(count):
            stack.pop()

def adx(stack, value):
    temp_stack = []
    if not len(stack) == 0:
        for _ in range(len(stack)):
            current_element = stack.pop()
            modified_element = current_element + value
            temp_stack.append(modified_element)
    # print("temp", temp_stack)
    # while not len(stack) == 0:
    #     current_element = stack.pop()
    #     modified_element = current_element + value
    #     temp_stack.append(modified_element)
    
    if not len(temp_stack) == 0:
        for _ in range(len(temp_stack)):
            stack.append(temp_stack.pop())
    # print("stack akhir", stack)

    # while not len(temp_stack) == 0:
    #     stack.append(temp_stack.pop())

def dex(stack, value):
    temp_stack = []
    if not len(stack) == 0:
        for _ in range(len(stack)):
            current_element = stack.pop()
            modified_element = current_element - value
            temp_stack.append(modified_element)
    # print("temp", temp_stack)
    
    if not len(temp_stack) == 0:
        for _ in range(len(temp_stack)):
            stack.append(temp_stack.pop())
    # print("stack akhir", stack)
            
def mux(stack, value):
    temp_stack = []
    if not len(stack) == 0:
        for _ in range(len(stack)):
            current_element = stack.pop()
            modified_element = current_element * value
            temp_stack.append(modified_element)
    # print("temp", temp_stack)
    
    if not len(temp_stack) == 0:
        for _ in range(len(temp_stack)):
            stack.append(temp_stack.pop())
    # print("stack akhir", stack)


stack = []
results = []

T = int(input())
for _ in range(T):
    new_input = input().split()
    command = new_input[0]
    if command == "add":
        value = int(new_input[1])
        count = int(new_input[2])
        add(stack, value, count)
        # print("add", stack)
        if not len(stack) == 0:
            results.append(len(stack))
    elif command == "del":
        count = int(new_input[1])
        if not len(stack) == 0:
            results.append(stack[-1])
        delete(stack, count)
        # print("del", stack)
    elif command == "adx":
        value = int(new_input[1])
        adx(stack, value)
        # print("adx", stack)
    elif command == "dex":
        value = int(new_input[1])
        dex(stack, value)
        # print("dex", stack)
    elif command == "mux":
        value = int(new_input[1])
        mux(stack, value)
        # print("mux", stack)

# print(stack)

# print()
# print()

for item in results:
    print(item)