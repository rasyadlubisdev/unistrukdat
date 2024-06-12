#source: file:///Users/puspaningrummardjoeki/Documents/FOLDER%20RASYAD/ITS/RESOURCES/SEMESTER%202/STRUKTUR_DATA/Hands-On%20Data%20Structures%20and%20Algorithms%20with%20Python%203rd%20(2022).pdf
#page: 178
#about: stack

def check_bracket(stack, strng):
    for char in strng:
        if char in ('(', '[', '{'):
            stack.append(char)
        if char in (')', ']', '}'):
            last = stack.pop()
            if last == '(' and char == ')':
                continue
            elif last == '[' and char == ']':
                continue
            elif last == '{' and char == '}':
                continue
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

S = input()
# {(foo)(bar)}[hello](((this)is)a)
stack = []

result = check_bracket(stack, S)
print(result)


        
