D = int(input("enter the number of days : "))
Years = D // 365  # calculating year
Months = (D - Years * 365) //30 # calculating months
Days = (D - Years * 365) - (Months * 30)  # calculating days
print(Years)
print(Months)
print(Days)
