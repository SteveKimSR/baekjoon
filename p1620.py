import sys

n, p = map(int, sys.stdin.readline().split())
l = []
d = {}
for _ in range(n):
    name = sys.stdin.readline().strip()
    l.append(name)
    d[name] = len(l)

for _ in range(p):
    q = input()
    if q.isalpha():
        print(d[q])
    else:
        print(l[int(q)-1])

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dic = {}
for i in range(1, N+1):
    name = input().rstrip()
    dic[name] = str(i)
    dic[str(i)] = name

for _ in range(M):
    print(dic[input().rstrip()])