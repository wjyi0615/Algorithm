#나무의 수 N, 나무의 길이 M
N, M = map(int, input().split())
wood_list = list(map(int, input().split()))
#print(wood_list)
start, end = 1, max(wood_list)

while start <= end:
    mid = (start+end)//2
    
    wood_sum = 0
    for i in wood_list:
        get = i - mid
        if get >= 0:
            wood_sum += get
            
    #벌목 높이를 이분탐색
    if wood_sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
            