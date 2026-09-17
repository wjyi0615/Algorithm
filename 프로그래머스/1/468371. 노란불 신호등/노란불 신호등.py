from math import gcd

def solution(signals):
    # 최소공배수 구하기
    limit = 1

    for G, Y, R in signals:
        cycle = G + Y + R
        limit = limit * cycle // gcd(limit, cycle)

    # 1초부터 전체 주기가 반복되는 시점까지 확인
    for t in range(1, limit + 1):
        all_yellow = True

        for G, Y, R in signals:
            cycle = G + Y + R
            pos = (t - 1) % cycle

            if not (G <= pos < G + Y):
                all_yellow = False
                break

        if all_yellow:
            return t

    return -1