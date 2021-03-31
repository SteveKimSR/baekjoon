import sys

for _ in range(int(sys.stdin.readline())):
    dic = {}
    k = int(sys.stdin.readline())
    for _ in range(k):
        name, kind = sys.stdin.readline().split()
        if dic.get(kind):
            dic[kind].append(name)
        else:
            dic[kind] = [name]
    # 나머지 조합 : (key + 1(없음 추가)) * ans - 1(넷 다 없음 일 경우)
    ans = 1
    for i in dic.keys():
        ans = (len(dic[i]) + 1) * ans
    print(ans - 1)
