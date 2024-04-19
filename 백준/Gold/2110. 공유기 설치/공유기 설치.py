N, C = map(int, input().split())

router = []
for _ in range(N):
    router.append(int(input()))
router.sort()

#이분탐색 검색 범위설정
start = 1 #공유기 거리 최소
end = router[-1] - router[0]
result = 0

#이분탐색 
while start<=end:
    mid = (start + end)//2 #설치하고 다음으로 이동할 공유기 거리
    cnt = 1 #공유기 갯수
    current = router[0]
    
    #최소거리 자체를 이분탐색으로 
    for i in range(1, len(router)):
        if router[i] >= current + mid:
            cnt +=1  #공유기 설치
            current = router[i]
    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
print(end)