N = int(input())
l = {}
for _ in range(N):
    a, b = map(int, input().split())
    if l.get(a) is None:
        l[a] = [b]
    else:
        temp = l[a]
        temp.append(b)
        l[a] = temp
k = list(l.keys())
k.sort()
for key in k:
    li = l[key]
    li.sort()
    for v in li:
        print(key, v)