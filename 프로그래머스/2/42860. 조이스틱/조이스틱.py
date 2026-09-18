def solution(name):
    answer = 0

    # 1. 위/아래 이동
    for i in name:
        up = ord(i) - ord('A')
        down = ord('Z') - ord(i) + 1

        answer += min(up, down)

    # 2. 좌/우 이동
    n = len(name)

    # 그냥 오른쪽으로 끝까지 가는 경우
    move = n - 1

    for i in range(n):
        next = i + 1

        # 다음 문자가 A라면 연속된 A를 전부 건너뜀
        while next < n and name[next] == 'A':
            next += 1

        # 오른쪽으로 갔다가 다시 왼쪽으로 돌아가는 경우
        move = min(move, i * 2 + n - next)

        # 왼쪽으로 먼저 크게 갔다가 오른쪽으로 가는 경우
        move = min(move, i + (n - next) * 2)

    answer += move

    return answer