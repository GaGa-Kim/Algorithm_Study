# 1475번
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값 출력

# 한 세트에는 0~9까지 숫자 하나씩
# 6, 9 서로 호환 가능

# 다솜이의 방 번호 N (1 <= N <= 1,000,000)
n = input()

list = [0] * 10
for i in range(len(n)):
    num = int(n[i])
    if num == 6 or num == 9:
        if list[6] <= list[9]:
            list[6] += 1
        else:
            list[9] += 1
    else:
        list[num] += 1
        
print(max(list))