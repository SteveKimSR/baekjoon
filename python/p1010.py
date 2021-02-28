import math


def solve():
    cases = int(input())
    for _ in range(cases):
        w, e = map(int, input().split())
        print(int(math.factorial(e) / (math.factorial(e - w) * math.factorial(w))))


solve()
