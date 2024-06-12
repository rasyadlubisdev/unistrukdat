stack = []

S = input()
number = 0

for i, char in enumerate(S):
    if char == "(":
        number += 1
    elif char == ")":
        number -= 1
    else:
        print("Input tidak sesuai")
        break
    # print("len", len(stack))
    stack.append(char)
    if (char == "(" and number == 1) or (char == ")" and number == 0):
        # print(i, number, char)
        # if len(stack) > 0:
        #     stack.pop()
        stack.pop()
    # else:
    #     stack.append(char)

    # print(number)

print("".join(stack))