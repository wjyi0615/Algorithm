def solution(brown, yellow):

    total = brown + yellow

    for w in range(total, 0, -1):

        if total % w == 0:
            h = total // w

            if w >= h:
                if (w - 2) * (h - 2) == yellow:
                    return [w, h]