# check whether the number is prime or not

n = int(input("enter the number :"))
d = 2
p = False
while d < n:
    if n % d == 0:
        p = True
    d += 1
if p:
    print("not prime")
else:
    print("prime")
