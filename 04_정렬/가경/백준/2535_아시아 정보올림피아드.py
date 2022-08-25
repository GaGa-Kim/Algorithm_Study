n = int(input())
students = []
for _ in range(n):
    students.append(list(map(int, input().split())))

students = sorted(students, key = lambda x: -x[2])

if (students[0][0] == students[1][0]) : # 1등과 2등의 국가가 같을 경우
    print(students[0][0], students[0][1])
    print(students[1][0], students[1][1])
    
    for i in range(2, n):
        if(students[0][0] != students[i][0]):
            print(students[i][0], students[i][1])
            break
else :
    print(students[0][0], students[0][1])
    print(students[1][0], students[1][1])
    print(students[2][0], students[2][1])