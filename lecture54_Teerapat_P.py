#login
#showMenu
#selectMenu
#VatCalculate
#PriceCalculate
def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "1234":
        return True
    else:
        return False

def showMenu():
    print(20*"-"+"Menu"+20*"-")
    print("1 : Vat Calculator")
    print("2 : Price Calculator")

def selectMenu():
    userSelected = input("Choose Number(1,2) >> ")
    if userSelected == "1":
        print("Vat Price = ",VatCalculate(int(input("Price : "))),"Baht")
    elif userSelected == "2":
        print("Total Price = ",PriceCalculate(),"Baht")

def VatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

def PriceCalculate():
    price1 = int(input("First Product :  "))
    pricr2 = int(input("Second Product : "))
    return VatCalculate(price1+price2)

if login() == True:
    showMenu()
    selectMenu()
else:
    print("Not allow !!")
