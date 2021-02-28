N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
card.reverse()
minimum = 0
for i, c1 in enumerate(card[:-2]):
    for j, c2 in enumerate(card[1 + i:-1]):
        for k, c3 in enumerate(card[2 + i + j:]):
            candidate = c1 + c2 + c3
            if minimum < candidate <= M:
                minimum = candidate
print(minimum)
