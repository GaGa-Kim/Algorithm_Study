import sys

l = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

numbers.sort()

if n in numbers:
    print(0)
else:
    min = 0
    max = 0
    # 배열 중에서 n과 가장 근접한 두 수를 구함
    # 배열이 1 7 14 10 이고 n이 2이면, min은 1, max는 7
    for number in numbers:
        if number < n:
            min = number
        elif number > n and max == 0:
            max = number
    # 좋은 구간을 만족하려면 모든 정수가 집합에 속하지 않아야 하므로
    # min은 2, max는 6
    max -= 1
    min += 1
    # [2, 3], [2, 4], [2, 5], [2, 6]
    print((n - min) * (max - n + 1) + (max - n))