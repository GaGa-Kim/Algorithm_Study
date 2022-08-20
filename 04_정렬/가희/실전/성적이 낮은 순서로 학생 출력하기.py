# n명의 학생 정보(이름, 성적)가 있을 때 성적이 낮은 순서로 학생 이름 출력

# 학생의 수 (1 <= n < = 100,000)
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append(input_data[0], int(input_data[1]))
    
array = sorted(array, key = lambda student : student[1])

for student in array:
    print(student[0], end=' ')