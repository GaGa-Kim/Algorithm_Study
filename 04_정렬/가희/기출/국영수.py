# 백준 10825번
# 반 학생 n명의 이름, 국어, 영어, 수학 점수가 주어질 때 
# 아래 조건으로 성적 정렬하는 프로그램 
# (1 <= 점수 <= 100, 이름은 알파멧 대소문자 구성 문자열, 길이 10 이하)
# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어, 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
#   (단, 아스키코드에서 대문자는 소문자보다 사전 순으로 앞섬)

import sys
input = sys.stdin.readline

# 반 학생 수 n (1 <= n <= 100,000)
n = int(input())

students = []
for _ in range(n):
    students.append(input().split())

# x가 튜플 형태로 존재할 때, 각 튜플을 구성하는 원소의 순서에 맞게 정렬됨 
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])