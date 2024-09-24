def solution(a, b, c, d):
    answer = 0
    if a == b == c == d:
        a = a * 1111
        return a
    
    if a == b == c != d :
        return (a*10 + d)**2
    if a == b == d != c :
        return (a*10 + c)**2
    if a == c == d != b :
        return (a*10 + b)**2
    if b == c == d != a :
        return (b*10 + a)**2
        
    if a == b != c == d:
        return (a+c)*abs(a-c)
    if a == c != b == d:
        return (a+b)*abs(a-b)
    if a == d != b == c:
        return (a+b)*abs(a-b)
    
    if a == b != c != d:
        return c*d
    if a == c != b != d:
        return b*d
    if a == d != b != c:
        return b*c
    if b == c != a != d:
        return a*d
    if b == d != a != c:
        return a*c
    if c == d != a != b:
        return a*b
                           
    if a != b != c != d:
        return min(a,b,c,d)
    
    