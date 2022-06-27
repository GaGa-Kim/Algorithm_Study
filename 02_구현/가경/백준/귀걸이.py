result = []
while True:
    n = int(input())
    if n == 0:
        break
    
    # 학생 이름 정보 
    names = [input() for _ in range(n)]
    # 귀걸이 정보 딕셔너리
    earing = {}

    for i in range(2 * n - 1):
        number, ab = input().split()
        if number in earing: # 두 번째로 등장하면 돌려받았음을 의미
            del earing[number]
        else:
            earing[number] = ab

    # 돌려 받지 못한 학생 순서 정보인 딕셔너리의 key 값만 가져와서 학생 이름 정보 찾기
    result.append(names[int(list(earing.keys())[0]) - 1])

for i in range(len(result)):
    print(i + 1, result[i])