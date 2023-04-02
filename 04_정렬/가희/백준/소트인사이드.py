# 1427번
# 숫자 n이 주어지면, n의 각 자리수를 내림차순으로 정렬해보자.

# n <= 1,000,000,000
n = list(input())

n.sort(reverse=True)

print(''.join(n))

"""
for i in n:
    print(i, end='')
"""
