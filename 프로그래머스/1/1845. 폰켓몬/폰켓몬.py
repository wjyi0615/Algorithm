def solution(nums):
    answer = 0
    # len(nums)//2
    # print(set(nums))
    if len(set(nums)) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(set(nums))
    return answer