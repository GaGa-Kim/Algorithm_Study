# 1244번
# 학생들이 입력되는 순서대로 자기의 성별과 받은 수에 따라
# 스위치를 바꿨을 때, 스위치들의 마지막 상태를 출력하는 프로그램

# 1: on / 0: off
# 학생 몇명에게 자연수 하나씩 나눠줌
# 학생들은 자신의 성별과 받은 수에 따라 아래 방식으로 스위치 조작

# 1. 남학생(1)은 자기가 받은 수(3)의 배수인 번호의 스위치(3, 6) 상태 바꿈
# 2. 여학생(2)은 자기가 받은 수와 같은 번호의 스위치를 중심으로
#    좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
#    그 구간에 속한 스위치 상태 모두 바꿈 
#    (구간에 속한 스위치 개수는 항상 홀수) 

# 스위치 개수 (1 <= switch_cnt <= 100)
switch_cnt = int(input())
# 스위치 초기 상태
switch_state = list(map(int, input().split()))
# 학생 수 (1 <= student_cnt <= 100)
student_cnt = int(input())

# 각 학생의 성별과 받은 수
student_info = []
for i in range(student_cnt):
    sex, num = map(int, input().split())
    student_info.append((sex,num))
    
for i in student_info:
    # 남학생인 경우
    if i[0] == 1:
        for j in range(switch_cnt):
            if (j+1) % i[1] == 0:
                switch_state[j] = int(not switch_state[j])
    # 여학생인 경우
    else:
        for j in range(switch_cnt):
            if (j+1) == i[1]:
                switch_state[j] = int(not switch_state[j])
                front = j-1
                back = j+1
                while True:
                    if front < 0 or back >= switch_cnt:
                        break
                    else:
                        if switch_state[front] == switch_state[back]:
                            switch_state[front] = int( not switch_state[front])
                            switch_state[back] = int(not switch_state[back])
                        else: 
                            break
                        front -= 1
                        back += 1


for i in range(0, switch_cnt, 20):
    print(*switch_state[i:i+20])     
    
'''
for i in range(0, len(switch_state)):   
    print(switch_state[i], end=' ')
    if not i % 20:
        print()
''' 