import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
students = list(map(int, input().split()))

photo = dict()
for i in range(m):
    # 사진이 게시된 학생이 다른 학생의 추천을 받은 경우
    if students[i] in photo:
        photo[students[i]][0] += 1
    # 사진이 게시되지 않은 학생이 다른 학생의 추천을 받은 경우
    else:
        # 비어있는 사진틀이 있을 경우
        if len(photo) < n:
            photo[students[i]] = [1, i] # {학생번호: [추천 수, 들어온 순서]}
        # 비어있는 사진틀이 없을 경우
        else:
            # 추천 받은 횟수가 가장 적은 학생을 찾거나 
            # 같을 경우 게시된 지 가장 오래된 사진을 삭제
            del_list = sorted(photo.items(), key= lambda x : (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[students[i]] = [1, i]
answer_list = list(sorted(photo.keys()))
print(*answer_list)