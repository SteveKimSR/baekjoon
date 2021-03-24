import collections

ans = []
for _ in range(int(input())):
    op = input()
    l = int(input())
    if l == 0:
        input()
        a = collections.deque([])
    else:
        a = collections.deque(list(map(int, input()[1:-1].split(','))))
    flag = 0
    try:
        for i in op:
            if i == 'R':
                flag = int(not flag)
            else:
                if flag:
                    a.pop()
                else:
                    a.popleft()
        if flag:
            a.reverse()
            ans.append(list(a))
        else:
            ans.append(list(a))
    except IndexError:
        ans.append("error")
for i in ans:
    print(str(i).replace(' ', ''))
# 공백출력 하지 말 것...