n = int(input())
l = [[] for _ in range(51)]
for _ in range(n):
    w = input()
    w = [w, len(w)]
    count = l[w[1]].count(w)
    if count == 0:
        l[w[1]].append(w)
for i in range(51):
    l[i].sort()
    l[i].sort(key=lambda m:m[1])
    for w in l[i]:
        print(w[0])
