l = [[] for _ in range(200)]
for _ in range(int(input())):
    age, name = input().split()
    l[int(age)].append(name)
for age, group in enumerate(l):
    for p in group:
        print(age, p)
