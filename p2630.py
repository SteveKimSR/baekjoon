def solve(p):
    if check(p):
        if p[0][0]:
            global b
            b += 1
        else:
            global w
            w += 1
    else:
        for i in divide(p):
            solve(i)


def check(p):
    for i in p:
        for j in i:
            if j != p[0][0]:
                return False
    return True


def divide(p):
    length = int(len(p) / 2)
    a = [i[:length] for i in p[:length]]
    b = [i[length:] for i in p[:length]]
    c = [i[:length] for i in p[length:]]
    d = [i[length:] for i in p[length:]]
    return a, b, c, d


paper = []
w, b = 0, 0
for _ in range(int(input())):
    paper.append(list(map(int, input().split())))
solve(paper)
print(f'{w}\n{b}')
