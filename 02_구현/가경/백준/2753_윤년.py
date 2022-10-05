n = int(input())

# 윤년 - 4의 배수이면서, 100의 배수가 아닐 때
if n % 4 == 0 and n % 100 != 0:
    print(1)
# 윤년 - 400의 배수일 때
elif n % 400 == 0:
    print(1)
# 윤년이 아님
else:
    print(0)
