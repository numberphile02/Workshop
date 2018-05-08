def fib_no(n):
    a=1
    b=1
    c=a+b
    if type(n)==int and n>0:
        if n==1 or n==2:
            return 1
        elif n>=3:
            for i in range(1,(n+2)//3):
                a=b+c
                b=c+a
                c=a+b
            if n%3==0:
                return c
            elif n%3==1:
                return a 
            elif n%3==2:
                return b
