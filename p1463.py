n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[n])

'''
- dp가 꼭 여러 입력을 거쳐 정답을 저장할 필요는 없다는 것.
- 횟수를 배열에 저장하는 방법도 있다는 것.
'''