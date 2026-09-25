import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    #print(scoville)
    
    while scoville[0] < K:
        a = heapq.heappop(scoville) + (heapq.heappop(scoville))*2
        heapq.heappush(scoville,a)
        #print(scoville)
        answer += 1
        if (len(scoville) == 1) and scoville[0] < K:
            return -1
    return answer