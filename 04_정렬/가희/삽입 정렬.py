array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # i부터 1까지 감소
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[i], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작은 데이터 만나면 멈춤
        break
    
print(array)