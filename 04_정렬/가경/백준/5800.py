k = int(input())
for i in range(1, k + 1):
    student = list(map(int, input().split()))
    student = student[1:] # 학생 수 제거
    student.sort()
    diff = 0
    for j in range(0, len(student) - 1):
        if student[j + 1] - student[j] > diff:
            diff = student[j + 1] - student[j]
    print(f'Class {i}')
    print(f'Max {max(student)}, Min {min(student)}, Largest gap {diff}')
