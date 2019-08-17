number = int(input("Enter your number :"))
for x in range(number):
    tab = " "*(number-x)
    star = "*"*(2*x+1)
    result = tab + star
    print(result)
