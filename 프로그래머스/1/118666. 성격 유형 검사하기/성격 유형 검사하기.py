def solution(survey, choices):
    answer = []
    score = [[0,0],[0,0],[0,0],[0,0]]
    # mind = [[RT,TR],[FC,CF],[MJ,JM],[AN,NA]]
    # 점수 측정
    for i in range(len(choices)):
        if survey[i] == 'RT' and choices[i] == 1:
            score[0][0] += abs(choices[i] - 4)
        if survey[i] == 'RT' and choices[i] == 2:
            score[0][0] += 2
        if survey[i] == 'RT' and choices[i] == 3:
            score[0][0] += 1
        if survey[i] == 'RT' and choices[i] == 5:
            score[0][1] += 1
        if survey[i] == 'RT' and choices[i] == 6:
            score[0][1] += 2
        if survey[i] == 'RT' and choices[i] == 7:
            score[0][1] += 3

        if survey[i] == 'TR' and choices[i] == 1:
            score[0][1] += 3
        if survey[i] == 'TR' and choices[i] == 2:
            score[0][1] += 2
        if survey[i] == 'TR' and choices[i] == 3:
            score[0][1] += 1
        if survey[i] == 'TR' and choices[i] == 5:
            score[0][0] += 1
        if survey[i] == 'TR' and choices[i] == 6:
            score[0][0] += 2
        if survey[i] == 'TR' and choices[i] == 7:
            score[0][0] += 3
            
        # CF
        if survey[i] == 'CF' and choices[i] == 1:
            score[1][0] += 3
        if survey[i] == 'CF' and choices[i] == 2:
            score[1][0] += 2
        if survey[i] == 'CF' and choices[i] == 3:
            score[1][0] += 1
        if survey[i] == 'CF' and choices[i] == 5:
            score[1][1] += 1
        if survey[i] == 'CF' and choices[i] == 6:
            score[1][1] += 2
        if survey[i] == 'CF' and choices[i] == 7:
            score[1][1] += 3

        if survey[i] == 'FC' and choices[i] == 1:
            score[1][1] += 3
        if survey[i] == 'FC' and choices[i] == 2:
            score[1][1] += 2
        if survey[i] == 'FC' and choices[i] == 3:
            score[1][1] += 1
        if survey[i] == 'FC' and choices[i] == 5:
            score[1][0] += 1
        if survey[i] == 'FC' and choices[i] == 6:
            score[1][0] += 2
        if survey[i] == 'FC' and choices[i] == 7:
            score[1][0] += 3
        # JM
        if survey[i] == 'JM' and choices[i] == 1:
            score[2][0] += 3
        if survey[i] == 'JM' and choices[i] == 2:
            score[2][0] += 2
        if survey[i] == 'JM' and choices[i] == 3:
            score[2][0] += 1
        if survey[i] == 'JM' and choices[i] == 5:
            score[2][1] += 1
        if survey[i] == 'JM' and choices[i] == 6:
            score[2][1] += 2
        if survey[i] == 'JM' and choices[i] == 7:
            score[2][1] += 3

        if survey[i] == 'MJ' and choices[i] == 1:
            score[2][1] += 3
        if survey[i] == 'MJ' and choices[i] == 2:
            score[2][1] += 2
        if survey[i] == 'MJ' and choices[i] == 3:
            score[2][1] += 1
        if survey[i] == 'MJ' and choices[i] == 5:
            score[2][0] += 1
        if survey[i] == 'MJ' and choices[i] == 6:
            score[2][0] += 2
        if survey[i] == 'MJ' and choices[i] == 7:
            score[2][0] += 3
        # AN
        if survey[i] == 'AN' and choices[i] == 1:
            score[3][0] += 3
        if survey[i] == 'AN' and choices[i] == 2:
            score[3][0] += 2
        if survey[i] == 'AN' and choices[i] == 3:
            score[3][0] += 1
        if survey[i] == 'AN' and choices[i] == 5:
            score[3][1] += 1
        if survey[i] == 'AN' and choices[i] == 6:
            score[3][1] += 2
        if survey[i] == 'AN' and choices[i] == 7:
            score[3][1] += 3

        if survey[i] == 'NA' and choices[i] == 1:
            score[3][1] += 3
        if survey[i] == 'NA' and choices[i] == 2:
            score[3][1] += 2
        if survey[i] == 'NA' and choices[i] == 3:
            score[3][1] += 1
        if survey[i] == 'NA' and choices[i] == 5:
            score[3][0] += 1
        if survey[i] == 'NA' and choices[i] == 6:
            score[3][0] += 2
        if survey[i] == 'NA' and choices[i] == 7:
            score[3][0] += 3
    # 유형 결정
    for i in range(len(score)):
        if i == 0 and (score[0][0] >= score[0][1]):
            answer.append('R')
        elif i == 0 and (score[0][0] < score[0][1]):
            answer.append('T')
        elif i == 1 and (score[1][0] >= score[1][1]):
            answer.append('C')
        elif i == 1 and (score[1][0] < score[1][1]):
            answer.append('F')
        elif i == 2 and (score[2][0] >= score[2][1]):
            answer.append('J')
        elif i == 2 and (score[2][0] < score[2][1]):
            answer.append('M')
        elif i == 3 and (score[3][0] >= score[3][1]):
            answer.append('A')
        elif i == 3 and (score[3][0] < score[3][1]):
            answer.append('N')
    #print(score)
    answer = "".join(answer)
    return answer