from itertools import combinations

def solution(nums):
    answer = 0

    for numbers in combinations(nums, 3):
        total = sum(numbers)
        is_prime = True

        for j in range(2, int(total ** 0.5) + 1):
            if total % j == 0:
                is_prime = False
                break

        if is_prime:
            answer += 1

    return answer