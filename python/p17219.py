import sys
n, m = map(int, sys.stdin.readline().split())

p = {}
for _ in range(n):
    site, passwd = sys.stdin.readline().split()
    p[site] = passwd
for _ in range(m):
    site = sys.stdin.readline().rsplit()[0]
    print(p[site])