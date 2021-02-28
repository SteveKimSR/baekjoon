line = {}
for i in range(int(input()) + 1):
    line[i] = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    line[x].append(y)
    line[y].append(x)
l = [1]
for i in l:
    for j in line[i]:
        if j not in l:
            l.append(j)
print(len(l) - 1)
