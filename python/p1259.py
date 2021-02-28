ans = []
while True:
    i = input()
    if i == '0':
        break
    else:
        ans.append(i)
for i in ans:
    flag = True
    for w in range(len(i) // 2):
        if i[w] != i[len(i) - w-1]:
            flag = False
    print('yes' if flag else 'no')
