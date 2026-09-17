def solution(name, yearning, photo):
    score = {}
    result = []

    for i in range(len(name)):
        score[name[i]] = yearning[i]

    for i in photo:
        sums = 0
        
        for j in i:
            if j in score:
                sums += score[j]
            else:
                pass
        
        result.append(sums)

    return result