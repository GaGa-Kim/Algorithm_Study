# 1026번
# s의 최솟값을 출력하는 프로그램
# 길이가 n인 정수 배열 a와 b가 있다. 
# 다음과 같이 함수 s를 정의할 때, s의 값을 가장 작게 만들기 위해 a의 수를 재배열한다.
# 단, b에 있는 수는 재배열하면 안 된다.

# s = a[0] * b[0] + ... + a[n-1] * b[n-1]


# => a에서 가장 작은 수 * b에서 가장 큰 수

# 1 <= n <= 50
n = int(input())

# a, b <= 100 (음이 아닌 정수)
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sorted = sorted(a, reverse=True)
b_sorted = sorted(b)

result = 0
for i in range(n):
    result += a_sorted[i] * b_sorted[i]

print(result)

#-------------------------------------------------
# 1 <= n <= 50
n = int(input())

# a, b <= 100 (음이 아닌 정수)
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for i in range(n):
    result += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(result)