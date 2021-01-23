import sys

N = [i + 1 for i in range(int(sys.stdin.readline()))]
while len(N) > 1:
    if len(N) % 2:  # 패가 홀수
        temp = [N[-1]]
        temp.extend(N[1::2])
        N = temp
    else:  # 패가 짝수
        N = N[1::2]
print(N.pop())
