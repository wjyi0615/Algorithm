n = int(input())
def honoi(n,a,b,c):
    if n>20:
        return
    if n == 1:
        print(a, c)
    else:
        honoi(n-1, a, c, b)
        print(a, c)
        honoi(n-1, b, a, c)
sum = 2**n-1
print(sum)

honoi(n, 1, 2, 3)