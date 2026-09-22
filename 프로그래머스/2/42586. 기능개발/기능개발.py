def solution(progresses, speeds):
    days = []

    # 각 기능이 완료되기까지 걸리는 날짜
    for i in range(len(progresses)):
        day = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        days.append(day)

    answer = []

    deploy_day = days[0]
    cnt = 1

    for i in range(1, len(days)):

        # 앞 기능보다 먼저 또는 같은 날 완성
        if days[i] <= deploy_day:
            cnt += 1

        # 앞 기능보다 늦게 완성
        else:
            answer.append(cnt)
            cnt = 1
            deploy_day = days[i]

    answer.append(cnt)

    return answer