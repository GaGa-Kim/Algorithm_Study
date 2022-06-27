month, day, year, time = input().split()
day = int(day[:-1])
year = int(year)
hour, minute = map(int, time.split(':'))

month_list = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# 윤년 계산
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    month_day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 해당 년도 전체 날짜 수
total_time = sum(month_day_list) * 24 * 60

# 지금까지의 날짜 수
current_month = month_list.index(month)
current_time = (sum(month_day_list[:current_month]) + day - 1) * 24 * 60 + hour * 60 + minute

print(current_time / total_time * 100)
