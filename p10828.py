import sys

N = int(sys.stdin.readline())
l = []
for _ in range(N):
    temp = sys.stdin.readline().split()
    c = temp[0]
    if c == 'push':
        l.append(int(temp[1]))
    elif c == 'pop':
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop(-1))
    elif c == 'size':
        print(len(l))
    elif c == 'empty':
        print(0 if len(l) else 1)
    elif c == 'top':
        print(l[-1] if len(l) else -1)