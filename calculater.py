print("1 for addition",
      "2 for difference",
      "3 for product",
      "4 for quotient",
      "5 for remainder",
      "6 for exit program")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
N=int(input("enter the number between 1 to 6 to perform operators :"))
while N<=6:
    if N==1:
        print(a+b)
    elif N==2:
        print(a-b)
    elif N==3:
        print(a*b)
    elif N==4:
        print(a//b)
    elif N==5:
        print(a%b)
    N+=1
else:
    print("exit")