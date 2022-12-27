import math

t = int(input())
for _ in range(t):
    numbers = list(map(int, input().split()))
    result = 0
    # numbers[1]부터 차례대로 쌍을 만들어서 GCD를 구하고 더해줌
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            result += math.gcd(numbers[i], numbers[j])
    print(result)