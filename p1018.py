def solve():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    ans = 64
    board_type_1 = 'BWBWBWBW'
    board_type_2 = 'WBWBWBWB'
    for i in range(n - 7):
        for j in range(m - 7):
            type_1 = 0
            type_2 = 0
            for k in range(8):
                line = board[i+k][j:j + 8]
                if k % 2 == 0:
                    type_1 += differ(line, board_type_1)
                    type_2 += differ(line, board_type_2)
                else:
                    type_1 += differ(line, board_type_2)
                    type_2 += differ(line, board_type_1)
            minimum = min(type_1, type_2)
            if ans > minimum:
                ans = minimum
    print(ans)


def differ(line, board_type):
    count = 0
    for i in range(8):
        count += 1 if line[i] != board_type[i] else 0
    return count


solve()
