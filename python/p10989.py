N = int(input())
l = [0 for i in range(10001)]
for _ in range(N):
    l[int(input())] += 1
for num, i in enumerate(l):
    if i != 0:
        for _ in range(i):
            print(num)
