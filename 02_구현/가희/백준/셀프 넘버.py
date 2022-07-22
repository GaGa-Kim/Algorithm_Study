# 4673번
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램
# (오름차순)

# 양의 정수 n에 대하여 ( n은 d(n)의 생성자 )
# d(n) = n과 n의 각 자리수 더하는 함수
# d(75) = 75 + 7 + 5 = 87

# 셀프 넘버) 생성자가 없는 숫자

list = [0] * 10001

for num in range(1, 10001):
    sum = num
    for i in str(num):
        sum += int(i)
    if sum <= 10000:
        list[sum] += 1
    
for i in range(1, 10001):
    if list[i] == 0:
        print(i)
        
# ------------------------------------------
# set 이용
nums = set(range(1, 10001))
remove_set = set()  # 생성자 set
for num in nums :
    for n in str(num):
        num += int(n)
    remove_set.add(num) 

self_numbers = nums - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)