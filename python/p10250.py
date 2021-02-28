for _ in range(int(input())):
    H, W, N = map(int, input().split())
    h = N % H if N % H != 0 else H
    r = N // H if N % H == 0 else N // H + 1
    print(f'{h}{0 if r < 10 else ""}{r}')