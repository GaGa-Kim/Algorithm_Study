# 2529번
# k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾는 프로그램
# 각 부등호 앞뒤에 들어가는 숫자는 0 ~ 9 중 하나여야 하며, 중복 선택x

from itertools import permutations

# 부등호 문자 개수 (2 <= k <= 9)
k = int(input())
# k개의 부등호 기호
sign = list(input().split())

result = []
num = list(permutations(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), k+1))

for per in num:
    flag = True
    for i in range(k):
        if sign[i] == '<':
            if per[i] < per[i+1]:
                continue
            else:
                flag = False
                break
        elif sign[i] == '>':
            if per[i] > per[i+1]:
                continue
            else:
                flag = False
                break
    if flag:
        result.append(per)

print(''.join(max(result)))
print(''.join(min(result)))



