def solution(prices):
    answer = []
    #count = 0
    for i in range(len(prices)):
        count = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                count +=1
            elif prices[i] > prices[j]:
                count+=1
                break
            else:
                break
        answer.append(count)
        
    return answer