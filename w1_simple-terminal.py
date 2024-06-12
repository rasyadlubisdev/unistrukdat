def last_pend(stack, value):
    stack.append(value)

def pre_pend(stack, value):
    temp_stack = []
    if not len(stack) == 0:
        for _ in range(len(stack)):
            temp_stack.append(stack.pop())
    stack.append(value)
    if not len(temp_stack) == 0:
        for _ in range(len(temp_stack)):
            stack.append(temp_stack.pop())

def copy(stack, index_copy, index_paste):
    temp_stack = []
    for _ in range(len(stack)-1, index_copy-1, -1):
        temp_stack.append(stack.pop())
    simpan_value = temp_stack[-1]
    length_stack = len(stack)
    # length_temp_stack = len(temp_stack)
    # passing_index = (length_stack + length_temp_stack) - 1
    for i in range(len(temp_stack)):
        # print("cek index 1", i)
        # print("cek index 2", length_stack)
        # print("cek index 3", index_paste)
        if (i + length_stack == index_paste):
            stack.append(simpan_value)
        stack.append(temp_stack.pop())
    # print(stack)
    # print(temp_stack)
    # print(simpan_value)
        
def move(stack, index_source, index_dest):
    temp_stack = []
    for _ in range(len(stack)-1, index_source, -1):
        temp_stack.append(stack.pop())
    simpan_value = stack[-1]
    length_stack = len(stack)
    stack.pop()
    # print("stack tengah", stack)
    for i in range(len(temp_stack)):
        stack.append(temp_stack.pop())
        if (i + length_stack == index_dest):
            stack.append(simpan_value)

    # print(stack)
    # print(temp_stack)
    # print(simpan_value)




stack = []
running = True

while running:
    new_input = input().split()
    command = new_input[0]
    if command == "append":
        value = new_input[1]
        last_pend(stack, value)
    elif command == "prepend":
        value = new_input[1]
        pre_pend(stack, value)
    elif command == "cp":
        index_copy = int(new_input[1])
        index_paste = int(new_input[2])
        copy(stack, index_copy, index_paste)
    elif command == "mv":
        index_source = int(new_input[1])
        index_dest = int(new_input[2])
        move(stack, index_source, index_dest)
    elif command == "rm":
        index_source = int(new_input[1])
        stack.pop(index_source)
    
    elif command == "stop":
        running = False
    else:
        print("Bukan perintah valid")


print(len(stack))
for item in stack:
    print(item)
