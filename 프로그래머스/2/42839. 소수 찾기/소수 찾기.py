from itertools import permutations

def checkprime(n):
    if n < 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    total = set()
    num = list(numbers)
    
    for i in range(1,len(num)+1):
        for j in permutations(num,i):
            #print(type(j))
            #print(j)
            target = ''
            for i in j:
                target += i
            total.add(int(target))
    for i in total:
        if checkprime(i):
            answer +=1
        else:
            continue
    return answer

