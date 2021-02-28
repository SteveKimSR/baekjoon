import sys

T = int(sys.stdin.readline())
case = []
for _ in range(T):
    case.append(sys.stdin.readline())

for c in case:
    flag = 0
    for ch in c:
        if flag < 0:
            break
        if ch == '(':
            flag += 1
        elif ch == ')':
            flag -= 1
    print("YES" if flag == 0 else "NO")