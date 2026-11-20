
N = int(input())
answer = 0

for _ in range(N):
    word = input()
    seen = set()
    prev = ''
    is_group = True

    for char in word:
        if char != prev:
            if char in seen:
                is_group = False
                break

            seen.add(char)

        prev = char

    if is_group:
        answer += 1

print(answer)
