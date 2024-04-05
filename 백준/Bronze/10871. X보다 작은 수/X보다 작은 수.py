a, b = map(int, input().split())
num_list = list(map(int, input().split()))
ans = []
for i in num_list:
    if b > i:
        print(i, end =' ')

