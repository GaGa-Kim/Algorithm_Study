n = int(input())
dasom = int(input())
other = []
count = 0

for _ in range(n - 1):
    other.append(int(input()))
other.sort(reverse=True)

if n == 1:
    print(0)
else:
    while(other[0] >= dasom): # 다솜보다 득표수가 많을 경우
        dasom += 1 # 다솜이 표를 매수
        other[0] -= 1
        count += 1
        other.sort(reverse=True)
    print(count)