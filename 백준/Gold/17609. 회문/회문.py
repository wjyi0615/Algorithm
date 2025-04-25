def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def check_type(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # 한 문자 제거해서 회문 가능 여부 확인
            if is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1):
                return 1  # 유사회문
            else:
                return 2  # 일반 문자열
        left += 1
        right -= 1
    return 0  # 회문

T = int(input())
for _ in range(T):
    s = input().strip()
    print(check_type(s))
