T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = []
    check = []
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage.append([x, y])
    count = 0
    for c in cabbage:
        if c not in check:
            check.append(c)
            to_do = [c]
            for ch in to_do:
                near = [[ch[0] + 1, ch[1]], [ch[0] - 1, ch[1]], [ch[0], ch[1] + 1], [ch[0], ch[1] - 1]]
                for i in near:
                    if i in cabbage and i not in check:
                        cabbage.remove(i)
                        check.append(i)
                        to_do.append(i)
            count += 1
    print(count)