def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
num=7
if num<0:
    print("does not exist")
elif num==0:
    print("fact is 0 is 1")
else:
    print(recur_factorial(num))
