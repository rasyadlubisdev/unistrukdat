ans = []
run = True
while run:
    temp_stack = []
    cmd = input()
    if cmd == "stop":
        break
    new_input = cmd.split('/')
    for i, char in enumerate(new_input):
        if char not in ["", ".", ".."]:
            temp_stack.append("/")
            temp_stack.append(char)
        if char == "..":
            temp_stack.pop()
            temp_stack.pop()
    if temp_stack[-1] == '/':
        temp_stack.pop()
    ans.append(temp_stack)

for answer in ans:
    print("".join(answer))
