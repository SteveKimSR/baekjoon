N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

# 1. 문제의 의도대로 풀이
# ans = []
# for c in check:
#     ans.append(card.count(c))
#
# print(*ans)
# 결과 : 시간초과

# 2. count로 인한 시간초과 -> dict 사용
cards = {}
for c in card:
    if c in cards:
        cards[c] += 1
    else:
        cards[c] = 1

for i in check:
    print(cards[i] if i in cards else 0, end=' ')