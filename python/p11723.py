import sys

s = {i: 0 for i in range(1, 21)}

for _ in range(int(sys.stdin.readline())):
    op = sys.stdin.readline().split()
    if op[0] == "add":
        s[int(op[1])] = 1
    elif op[0] == "remove":
        s[int(op[1])] = 0
    elif op[0] == "check":
        print(s[int(op[1])])
    elif op[0] == "toggle":
        s[int(op[1])] = int(not s[int(op[1])])
    elif op[0] == "all":
        s = {i: 1 for i in range(1, 21)}
    elif op[0] == "empty":
        s = {i: 0 for i in range(1, 21)}
