import sys
input = sys.stdin.readline

numbers = [] # 등장하는 카드 숫자
cnt_color = {'R': 0, 'B': 0, 'Y': 0, 'G': 0} # 카드 색 등장 횟수
cnt_number = [0 for _ in range(11)] # 1부터 9까지 카드 숫자 등장 횟수
for _ in range(5):
    color, number = input().split()
    cnt_color[color] += 1
    cnt_number[int(number)] += 1
    numbers.append(int(number))
    
# 1번 규칙 (카드 5장이 모두 같은 색 + 카드 5장의 숫자가 연속적)
sort_nums = numbers.copy()
sort_nums.sort()
if 5 in cnt_color.values() and sort_nums[0] + 1 == sort_nums[1] and sort_nums[1] + 1 == sort_nums[2] and sort_nums[2] + 1 == sort_nums[3] and sort_nums[3] + 1 == sort_nums[4]:
        score = max(numbers) + 900

# 2번 규칙 (카드 4장이 같은 숫자)
elif 4 in cnt_number:
    score = cnt_number.index(4) + 800

# 3번 규칙 (카드 3장이 같은 숫자 + 나머지 2장도 같은 숫자)
elif 3 in cnt_number and 2 in cnt_number:
    score = cnt_number.index(3) * 10 + cnt_number.index(2) + 700

# 4번 규칙 (카드 5장이 모두 같은 색)
elif 5 in cnt_color.values():
    score = max(numbers) + 600

# 5번 규칙 (카드 5장의 숫자가 연속적)
elif sort_nums[0] + 1 == sort_nums[1] and sort_nums[1] + 1 == sort_nums[2] and sort_nums[2] + 1 == sort_nums[3] and sort_nums[3] + 1 == sort_nums[4]:
    score = max(numbers) + 500

# 6번 규칙 (카드 3장이 같은 숫자)
elif 3 in cnt_number:
    score = cnt_number.index(3) + 400

# 7, 8번 규칙
elif 2 in cnt_number:
    # 2장이 같은 것을 제거했을 때도 2장이 같은 것이 남아있는지 확인
    first = cnt_number.index(2)
    cnt_number[first] = 0
    if 2 in cnt_number: # 7번 규칙 (카드 2장이 같은 숫자 + 나머지 2장도 같은 숫자)
        second = cnt_number.index(2)
        score = max(first, second) * 10 + min(first, second) + 300
    else: # 8번 규칙 (카드 2장이 같은 숫자)
        score = first + 200

# 9번 규칙 (어떤 경우에도 해당하지 않음)
else:
    score = max(numbers) + 100

print(score)