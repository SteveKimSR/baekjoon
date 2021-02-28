ans = {0: [1, 0], 1: [0, 1]}


def fibo(n):
    if n == 0:
        return ans[0]
    elif n == 1:
        return ans[1]
    else:
        if ans.get(n - 1) is None:
            x = fibo(n - 1)
            ans[n - 1] = x
        else:
            x = ans.get(n - 1)
        if ans.get(n - 2) is None:
            y = fibo(n - 2)
            ans[n - 2] = y
        else:
            y = ans.get(n - 2)
        return [z + w for z, w in zip(x, y)]


T = int(input())
for i in range(T):
    zero = 0
    one = 0
    print(*fibo(int(input())))
