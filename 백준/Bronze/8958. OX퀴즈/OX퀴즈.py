a = int(input())
ans = []

for i in range(0,a):
    quiz = list(input())
    total = 0
    score = 0
    for i in quiz:
        if i == 'X':
            score = 0
        if i == 'O':
            score +=1
            total = total + score
    ans.append(total)
for i in ans:
    print(i)