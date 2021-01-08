# 20529번 문제
# https://www.acmicpc.net/problem/20529

def p20529():
    T = int(input())
    for t in range(T):
        N = int(input())
        people = list(map(str, input().split()))
        ans = 100
        if N > 32:
            print(0)
        else:
            for i, p1 in enumerate(people[:N - 2]):
                for j, p2 in enumerate(people[i + 1:N - 1]):
                    for p3 in people[i + j+2:]:
                        count = 0
                        for x in range(4):
                            if p1[x] != p2[x]: count += 1
                            if p2[x] != p3[x]: count += 1
                            if p1[x] != p3[x]: count += 1
                        if ans > count:
                            ans = count
            print(ans)

p20529()
