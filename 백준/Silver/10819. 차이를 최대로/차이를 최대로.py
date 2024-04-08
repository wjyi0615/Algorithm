#특정한 수가 있는 것이 아니라 완전탐색(브루트포스)을 해야함
import sys
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
ans = 0

#(1)순열을 만들자
p = list(permutations(nums, N))
#print(p) 모든 순열 생성되었는지 확인 (팩토리얼)
for i in p:
    sum = 0
    for j in range(0,N-1):
        sum += abs(i[j]-i[j+1])
    ans = max(ans, sum)    
    
print(ans)