# 1789번
# 서로 다른 n개의 자연수의 합이 s라고 한다.
# s를 알 때, 자연수 n의 최댓값은?

# 최대한 많은 자연수를 사용해 s를 만들기 위해서는
# 서로 다른 자연수들이 최소가 되어야 한다.

# 방법 1) 값이 s보다 커질 때까지 1을 순차적으로 더해나가기
# 1 <= s <= 4,294,967,295
s = int(input())

total = 0 
count = 0

while True:
    count += 1
    total += count
    if total > s:
        break

print(count-1)

# 방법 2) 1부터 n까지 더하는 공식(n * (n+1) / 2) 이용하기
# 1 <= s <= 4,294,967,295
s = int(input())

n = 1
while n * (n+1) / 2 <= s:
    n += 1
    
print(n-1)