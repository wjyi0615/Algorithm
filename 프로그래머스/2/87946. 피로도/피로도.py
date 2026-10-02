from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for i in permutations(dungeons, len(dungeons)):
        fatigue = k  # 새로운 순서는 처음 피로도로 시작
        count = 0    # 이 순서에서 탐험한 던전 수

        for j in range(len(dungeons)):
            if fatigue < i[j][0]:
                break

            fatigue -= i[j][1]
            count += 1

        answer = max(answer, count)

    return answer