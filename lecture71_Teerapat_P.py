menuList = []
priceList = []

def showBill():
    print('MY Food'.center(21,'-'))
    for number in range(len(menuList)):
        print(menuList[number] , priceList[number])

def showTotalPrice():
    total = 0
    for number in range(len(priceList)):
        total = total + float(priceList[number])
    print('Total Price = ',total,'Baht')

while True:
    menuName = input("Enter menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Enter price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
showTotalPrice()

