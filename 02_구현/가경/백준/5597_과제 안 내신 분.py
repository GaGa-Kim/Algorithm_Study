students = [i for i in range(1, 31)]
for _ in range(28):
    n = int(input())
    students.remove(n)
students.sort()
print(students[0])
print(students[1])