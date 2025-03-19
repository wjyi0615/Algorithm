import sys

# 한 번에 입력을 받아 공백 기준으로 분리
data = sys.stdin.read().split()

# 첫 번째 값은 N
N = int(data[0])

# 다음 N개의 값은 A_i 리스트
A_i = list(map(int, data[1:N+1]))

# 마지막 두 개는 B, C
B, C = map(int, data[N+1:N+3])

# 총 감독관은 한 시험장에 1명 필수
ans = N

# 각 시험장에서 총감독관이 맡고 남은 학생 처리
for students in A_i:
    remaining = students - B  # 총감독관이 맡고 남은 학생 수
    if remaining > 0:
        ans += (remaining // C) + (1 if remaining % C != 0 else 0)

print(ans)