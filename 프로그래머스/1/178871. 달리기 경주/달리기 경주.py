def solution(players, callings):
    rank = {}

    for i in range(len(players)):
        rank[players[i]] = i

    for name in callings:
        current = rank[name]
        front = current - 1

        front_player = players[front]

        players[front], players[current] = players[current], players[front]

        rank[name] = front
        rank[front_player] = current

    return players