number = input()
set = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

for i in range(len(number)):
    if number[i] in ['6', '9']:
        set['6'] += 1
    else:
        set[number[i]] += 1

if set['6'] % 2 == 0:
    # 4개라면 6, 6, 9, 9 이므로 6은 2
    set['6'] = set['6'] // 2
else:
    # 3개라면 6, 6, 9 이므로 6은 2
    set['6'] = set['6'] // 2 + 1

print(max(set.values()))