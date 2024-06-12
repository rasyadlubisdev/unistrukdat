N = int(input())
macaron = input().split()
tumpukan_kedua = []
temp = []
ans = []
T = int(input())

for _ in range(T):
    cmd = input().split()
    if cmd[0] == "PULL":
        number = int(cmd[1])
        if number > len(macaron):
            ans.append("Macaron Furina tidak sebanyak itu pls!")
        else:
            length_macaron = len(macaron)
            for i in range(length_macaron-1, (length_macaron)-number, -1):
                temp.append(macaron.pop())
            tumpukan_kedua.append(macaron.pop())
            # print("F1-A", macaron)
            # print("F2-B", tumpukan_kedua)
            # print("F3-C", temp)
            length_temp = len(temp)
            for i in range(length_temp):
                macaron.append(temp.pop(0))
            # print("F4-A", macaron)
            # print("F5-B", tumpukan_kedua)
            # print("F6-C", temp)
    elif cmd[0] == "PUT":
        length_kedua = len(tumpukan_kedua)
        for i in range(length_kedua):
            macaron.append(tumpukan_kedua.pop())
        # print("F7-A", macaron)
        # print("F8-B", tumpukan_kedua)
        # print("F9-C", temp)
    else:
        ans.append("Apa itu? Furina tidak paham!")

if len(ans) != 0:
    for jwb in ans:
        print(jwb)
for i in range(len(macaron)):
    print(macaron[i], end=" ")
print()
for i in range(len(tumpukan_kedua)):
    print(tumpukan_kedua[i], end=" ")
print()

# t = ["A", "B", "C", "D", "E"]
# t.reverse()
# take = 4
# for i in range(len(t)-1, (len(t))-take, -1):
#     print(t[i])