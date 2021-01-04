# 20528번 문제
# https://www.acmicpc.net/problem/20529


def p20528():
    count = input()
    words = list(map(str, input().split()))

    first_word = words.pop(0)
    flag = 1
    for word in words:
        if first_word[0] != word[0]:
            flag = 0
            break
    print(flag)


if __name__ == "__main__":
    p20528()