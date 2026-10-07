import math

def solution(fees, records):
    answer = []
    stack = {}  # 차량별 입차 시각
    total = {}  # 차량별 누적 주차 시간

    for i in records:
        record = i.split()

        car = record[1]
        hour, minute = map(int, record[0].split(':'))
        time = hour * 60 + minute

        if record[2] == 'IN':
            stack[car] = time

            if car not in total:
                total[car] = 0

        else:
            total[car] += time - stack[car]
            del stack[car]

    # 아직 주차 중인 차량 처리
    for car in stack:
        total[car] += 1439 - stack[car]

    # 차량 번호 순으로 요금 계산
    for car in sorted(total):
        fee = fees[1]

        if total[car] > fees[0]:
            extra = total[car] - fees[0]
            fee += math.ceil(extra / fees[2]) * fees[3]

        answer.append(fee)

    return answer