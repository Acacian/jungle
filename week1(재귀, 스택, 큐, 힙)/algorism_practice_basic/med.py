def med(a,b,c):
    if a <= b:
        if a >= c:
            return a
        
    elif a >= b:
        if a >= c and b >= c:
            return b
        
    elif a >= b:
        if a >= c and c >= b:
            return c
        
    elif a <= b:
        if a <= c and b <= c:
            return b

    elif a <= b:
        if a <= c and c <= b:
            return c

    else:
        return b  

a = input()
b = input()
c = input()  

print(med(a,b,c))