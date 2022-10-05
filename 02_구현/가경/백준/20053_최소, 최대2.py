t = int(input())
for _ in range(t):
    n = int(input())
    number = list(map(int, input().split()))
    print(min(number), max(number))