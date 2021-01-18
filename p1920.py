n = int(input())
l = sorted(map(int, input().split()))
n = int(input())
c = map(int, input().split())


def binary(value, low, high):
    mid = (high + low) // 2
    mid_val = l[mid]
    if low > high:
        return 0
    elif mid_val == value:
        return 1
    elif mid_val < value:
        return binary(value, mid + 1, high)
    else:
        return binary(value, low, mid - 1)


for i in c:
    print(binary(i, 0, len(l) - 1))
