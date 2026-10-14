# Add method
# Calculator - look ka demo (Add + Exit)

print("=" * 30)
print("   ANKIT'S  Addition CALC")
print("=" * 30)

name = input("Tumhara naam kya hai?  ")
print("Namaste", name, "!")

count = 0   # kitni calculations hui

while True:
    print("\n1. Add (+)")
    print("2. Exit")
    choice = input("Option chuno: ")

    if choice == "1":
        x = float(input("Pehla number: "))
        y = float(input("Doosra number: "))
        print("-" * 30)                       # divider line
        print(x, "+", y, "=", x + y)          # safe format
        print("-" * 30)
        count += 1

    elif choice == "2":
        print("Dhanyavaad", name, "! Tumne", count, "calculations ki.")
        break

    else:
        print("Galat option! 1 ya 2 chuno.")


print("=" * 30)
print("   ANKIT'S Addition CALC")
print("=" * 30)

name = input("Tumhara naam kya hai? ")
print("Namaste", name, "!")

count = 0

while True:
    print("\n1. Add (+)")
    print("2. Exit")
    choice = input("Option chuno: ")

    if choice == "1":
        print("\n--- ADD ---")
        print("1. Do numbers")
        print("2. Teen numbers")
        print("3. Kai numbers (n baar)")
        print("4. Kai numbers (done likhne tak)")
        print("5. Wapas jao")
        sub = input("Sub-option chuno: ")

        if sub == "1":
            x = float(input("Pehla number: "))
            y = float(input("Doosra number: "))
            print("-" * 30)
            print(x, "+", y, "=", x + y)
            print("-" * 30)
            count += 1

        elif sub == "2":
            a = float(input("Pehla number: "))
            b = float(input("Doosra number: "))
            c = float(input("Teesra number: "))
            print("-" * 30)
            print("Total:", a + b + c)
            print("-" * 30)
            count += 1

        elif sub == "3":
            n = int(input("Kitne numbers add karne hain? "))
            total = 0
            for i in range(n):
                num = float(input("Number daalo: "))
                total += num
            print("-" * 30)
            print("Total:", total)
            print("-" * 30)
            count += 1

        elif sub == "4":
            total = 0
            while True:
                value = input("Number daalo (khatam karne ke liye done): ")
                if value == "done":
                    break
                total += float(value)
            print("-" * 30)
            print("Total:", total)
            print("-" * 30)
            count += 1

        elif sub == "5":
            print("Main menu pe wapas ja rahe hain...")

        else:
            print("Galat sub-option!")

    elif choice == "2":
        print("Dhanyavaad", name, "! Tumne", count, "calculations ki.")
        break

    else:
        print("Galat option! 1 ya 2 chuno.")

# substraction


print("=" * 30)
print("   ANKIT'S substraction calc")
print("=" * 30)

name = input("enter your name ")
print("Namaste", name, "!")

count = 0

while True:
    print("\n1. Subtract (-)")
    print("2. Exit")
    choice = input("Option chuno: ")

    if choice == "1":
        print("\n--- SUBTRACT ---")
        print("1. Do numbers")
        print("2. Teen numbers")
        print("3. Kai numbers (n baar)")
        print("4. Kai numbers (done likhne tak)")
        print("5. Wapas jao")
        sub = input("Sub-option chuno: ")

        if sub == "1":
            x = float(input("Pehla number: "))
            y = float(input("Doosra number: "))
            print("-" * 30)
            print(x, "-", y, "=", x - y)
            print("-" * 30)
            count += 1

        elif sub == "2":
            a = float(input("Pehla number: "))
            b = float(input("Doosra number: "))
            c = float(input("Teesra number: "))
            print("-" * 30)
            print("Result:", a - b - c)
            print("-" * 30)
            count += 1

        elif sub == "3":
            n = int(input("Kitne numbers subtract karne hain? "))
            total = float(input("Pehla number: "))
            for i in range(n - 1):
                num = float(input("Number daalo: "))
                total -= num
            print("-" * 30)
            print("Result:", total)
            print("-" * 30)
            count += 1

        elif sub == "4":
            total = float(input("Pehla number: "))
            while True:
                value = input("Number daalo (khatam karne ke liye done): ")
                if value == "done":
                    break
                total -= float(value)
            print("-" * 30)
            print("Result:", total)
            print("-" * 30)
            count += 1

        elif sub == "5":
            print("Main menu pe wapas ja rahe hain...")

        else:
            print("Galat sub-option!")

    elif choice == "2":
        print("Dhanyavaad", name, "! Tumne", count, "calculations ki.")
        break

    else:
        print("Galat option! 1 ya 2 chuno.")

#multiplyf

print("-"*30)
print("    Ankit Multiply calc")
print("-"*30)

name = input("enter your name : ")
print("namaste ", name,"!")

count = 0

while True :
    print("|n1 . multiply (*)")
    print("2 . exit . ")
    choice = input ("option chuno : ")

    if choice == "1" :
        print("|n1 . ------multiply-------")
        print("1 . do numbers ")
        print("2 . teen numbers ")
        print("3 . multiply karo (n barr)")
        print("4 . multiply karo janb tak (done na like )")
        print(" 5 . wapas jao ")
        sub = input ("sub option chuno :  ")

        if sub == "1":
            a = float(input("enter first numbers : "))
            b = float(input("enter second  numbers : "))
            print("-"*30)
            print(a,"*",b,"=",a*b)
            print("-"*30)
            count +=1

        elif sub == "2":
            a =  float(input("enter first numbers : "))
            b = float(input("enter second  numbers : "))
            c = float(input("enter tisra   numbers : "))
            print("-"*30)
            print("Result:", a * b * c)
            print("-"*30)
            count+=1

        elif sub == "3":
            n = int(input("kitne number multiply karne hai : "))
            total = float(input("first number : "))
            for i in range (n-1):
                 num = float(input(f"Number {i + 2} daalo: "))
                 total*=num
                 print("-"*30)
                 print("Result : ", total)
                 print("-"*30)
                 count +=1
        elif sub == "4" :
            while True :
                value = input("number dalo(done likne tak) : ")       
                if value == "done":
                    break
                total *= float(value)
                print("-"*30)
                print("result : ", total)
                print("-"*30)
                count+=1

        elif sub == "5":
            print("mai wapas ja raha hu...") 
        else:
            print("galat option..  try again ") 
    elif choice == "2":
        print("danyavadd",name,"!tumne",count,"calculation ki" )    
        break
    else:
        print(" galat option! , 1 ya 2 chune ")           





            


