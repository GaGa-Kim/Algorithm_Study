# 1244번
# 학생들이 입력되는 순서대로 자기의 성별과 받은 수에 따라 
# 스위치의 상태를 바꿨을 때, 스위치들의 마지막 상태를 출력하는 프로그램

# <스위치 조작>
# 남학생) 스위치 번호가 자기가 받은 수의 배수이면, 스위치 상태 바꿈
# 여학생) 자기가 받은 수와 같은 번호의 스위치를 중심으로 
#       좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서
#       그 구간에 속한 스위치의 상태 모두 바꿈
#       (이때 구간에 속한 스위치 개수는 항상 홀수)

# 0 < 스위치 개수 <= 100
n = int(input())
# 스위치 상태 (0:off, 1: on)
switch = list(map(int, input().split()))

# 0 < 학생 수 <= 100
m = int(input())
# 학생의 성별(1:남, 2:여), 학생이 받은 수(<= n)
student = []
for _ in range(m):
    sex, num = map(int, input().split())
    student.append((sex, num))

for i in student:
    if i[0] == 1: # 남학생인 경우
        for j in range(n):
            if (j+1) % i[1] == 0:
                switch[j] = int(not switch[j])
    else: # 여학생인 경우
        for j in range(n):
            if (j+1) == i[1]:
                switch[j] = int(not switch[j])
                front = j-1
                back = j+1
                while True:
                    if front < 0 or back >= n:
                        break
                    else:
                        if switch[front] == switch[back]:
                            switch[front] = int(not switch[front])
                            switch[back] = int(not switch[back])
                        else:
                            break
                        front -= 1
                        back += 1

# 스위치의 상태를 1번 스위치에서 시작하여 
# 마지막 스위치까지 한 줄에 20개씩 출력
for i in range(0, n, 20):
    print(*switch[i:i+20])      
    
'''
for i in range(0, len(switch_state)):   
    print(switch_state[i], end=' ')
    if not i % 20:
        print()
'''                   


