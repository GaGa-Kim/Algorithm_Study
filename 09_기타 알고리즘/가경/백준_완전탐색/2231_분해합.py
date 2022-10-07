import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    # 1부터 n까지의 수에 대한 분해합을 구함
    n_string = list(map(int, str(i)))
    s = i + sum(n_string)
    if (s == n):
        print(i)
        break
    elif (i == n):
        print(0)