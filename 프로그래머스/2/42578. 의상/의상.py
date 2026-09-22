def solution(clothes):
    a = {}
    answer = 1
    for i in clothes:
        if i[1] not in a:
            a[i[1]] = 1
        elif i[1] in a:
            a[i[1]] += 1
    # print(a.values())
    
    for i in a.values():
        answer = answer*(i+1)
    
    # 2 1 1 1 일때
    # 5+ 9 + 7 + 2
    # 3*2*2*2
    
    answer -= 1
    return answer