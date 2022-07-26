# 10773번

# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서,
# 가장 최근에 재민이가 쓴 수를 지우게 시킨다.

# 재민이가 모든 수를 받아 적은 후 그 수의 합을 구해야 한다.

# 1 <= K <= 100,000
k = int(input()) # 

list = []
for i in range(k):
    # 0 <= x <= 1,000,000
    x = int(input())
    if x == 0:
        list.pop()
    else:
        list.append(x)

print(sum(list))
        