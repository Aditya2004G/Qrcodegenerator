def is_leap(n):
    l = False
    if n%4==0:
        if n%400==0:
            l=True
            return l
        elif n %100==0:
            return l
        elif n%4==0:
            l=True
            return l
    else:
        return l


year = int(input())
print(is_leap(year))
