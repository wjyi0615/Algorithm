from itertools import combinations, product, permutations

def solution(word):
    answer = 1
    alphet = ['A', 'E', 'I', 'O','U']
    book = []
    
    for i in range(1,6):
        for j in product(alphet,repeat=i):
            book.append(''.join(j))
    book.sort()
    
    for index, value in enumerate(book):
        if value == word:
            return index+1
    return 
