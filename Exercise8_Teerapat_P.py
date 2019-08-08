username = input("Username : ")
password = input("Password : ")
if username == "teerapat" and password == "1234":
    print("WELCOME")
    print(10*"-","BOOKSHOP",10*"-")
    print("* Books for high school students *")
    print("1 : Mathematics Book x1 = 150 Baht")
    print("2 : Chemistry Book x1 = 200 Baht")
    print("3 : Biology Book x1 = 250 Baht")
    print(" Q >> What number of book do you want to buy ? (1,2 or 3)")
    SelectedBook = input("I want to buy number :")
    if SelectedBook == "1":
        print("How many book do you want ?")
        MathBook = int(input("I want : "))
        result1 = MathBook * 150
        print("Total Price = ",result1,"Baht")
    elif SelectedBook == "2":
        print("How many book do you want ?")
        ChemBook = int(input("I want : "))
        result2 = ChemBook * 200
        print("Total Price = ",result2,"Baht")
    elif SelectedBook == "3":
        print("How many book do you want ?")
        BioBook = int(input("I want : "))
        result3 = BioBook * 250
        print("Total Price",result3,"Baht")
else:
    print("SORRY! Your username or password is NOT correct , please check")
