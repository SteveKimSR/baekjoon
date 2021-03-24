global w, b
w, b = 0, 0


def check(p):
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][j] != p[0][0]:
                return False
    return True


def divide(p):
    half = int(len(p) / 2)
    return [i[:half] for i in p[:half]], [i[half:] for i in p[:half]], \
           [i[:half] for i in p[half:]], [i[half:] for i in p[half:]]


def do(p):
    global w, b
    if check(p):
        if p[0][0]:
            b += 1
        else:
            w += 1
    else:
        for i in divide(p):
            do(i)


do([list(map(int, input().split())) for _ in range(int(input()))])
print(w)
print(b)
