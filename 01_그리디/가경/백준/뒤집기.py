s = input() 
count0 = 0 # 전부 0으로 바꾸는 경우 
count1 = 0 # 전부 1로 바꾸는 경우

if s[0] == '1': # 첫 번째 원소에 대해서 처리
    count0 += 1
else: 
    count1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]: # 두 원소가 다르고
        if s[i + 1] == '1': # 다음 수에서 1로 바뀔 경우
            count0 += 1
        else: # 다음 수에서 0을 바뀔 경우
            count1 += 1

print(min(count0, count1))