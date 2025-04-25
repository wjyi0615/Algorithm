def is_vps_stack(ps):
    stack = []
    for ch in ps:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

T = int(input())
for _ in range(T):
    ps = input().strip()
    print(is_vps_stack(ps))
