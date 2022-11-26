from datetime import datetime, timedelta
import sys
input = sys.stdin.readline

n, l, f = map(str, input().split())
# 대여기간 날짜 연산
n, l, f = int(n), timedelta(days=int(l[:3]), hours=int(l[4:6]), minutes=int(l[7:])), int(f)
minute = timedelta(minutes=1)

rent_dict = {} # 부품 대여장
people = {} # 벌금을 내는 사람들
for _ in range(n):
    string = input().rstrip()
    time = datetime.strptime(string[:16], '%Y-%m-%d %H:%M') # 시각
    part, name = string[16:].split() # 부품 이름, 회원 닉네임
    # 한 번도 부품을 빌린 적이 없다면 부품 대여장에 이름 추가
    if name not in rent_dict:
        rent_dict[name] = {}
    # 부품 대여장에 대여 기록이 있다면 (반납)
    if part in rent_dict[name]:
        # 대여 기간 계산 = 반납 시간 - 빌린 시간
        result = time - rent_dict[name].pop(part)
        # 대여 기간보다 늦게 반납했다면
        if result > l:
            # 벌금을 내는 사람들에 이름 추가
            if name not in people:
                people[name] = 0
            # 벌금 추가
            people[name] += ((result - l) // minute) * f
    # 부품 대여장에 대여 기록이 없다면 (대여)
    else:
        rent_dict[name][part] = time

# 이름을 사전순으로 정렬하고 벌금내는 사람과 벌금 출력
if people:
    for name, pay in sorted(people.items(), key=lambda x: x[0]):
        print(name, pay)
else:
    print(-1)