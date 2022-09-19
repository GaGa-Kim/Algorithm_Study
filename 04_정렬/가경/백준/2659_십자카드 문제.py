# 시계수
def get_clock_num(n):
    min = int(''.join(map(str, n)))
    for i in range(1, 4):
        # 더 작은 수가 있다면 시계수 변경
        tmp = int(''.join(map(str, n[i:] + n[:i])))
        if min > tmp:
            min = tmp
    return min

n = list(map(int, input().split()))
clock_num = get_clock_num(n)
count = 0
# 1111부터 clock_num까지 clock_num보다 작은 시계수
for i in range(1111, clock_num):
    # 십자카드에 0이 없고 i가 시계수일 경우
    if '0' not in list(str(i)) and i == get_clock_num(list(map(int, str(i)))):
        count += 1
print(count + 1)
