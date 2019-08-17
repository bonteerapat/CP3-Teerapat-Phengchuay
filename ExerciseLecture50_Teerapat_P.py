num1 = int(input("input number1 : "))
operator = input("operator : ")
num2 = int(input("input number2 : "))
def Calculate(num1,operator, num2):
    if operator == "+":
        print("Total =",num1 + num2)
    elif operator == "-":
        print("Total =",num1 - num2)
    elif operator == "x":
        print("Total =",num1 * num2)
    elif operator == "/":
        print("Total =",num1 / num2)
Calculate(num1,operator,num2)
