# Add method
# Calculator - look ka demo (Add + Exit)

print("=" * 30)
print("   ANKIT'S CALCULATOR")
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
print("   ANKIT'S CALCULATOR")
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
print("   ANKIT'S CALCULATOR")
print("=" * 30)

name = input("Tumhara naam kya hai?  ")
print("Namaste", name, "!")

count = 0   # kitni calculations hui

while True:
    print("\n1. Add (+)")
    print("2. Subtract (-)")
    print("3. Exit")
    choice = input("Option chuno: ")

    if choice == "1":
        x = float(input("Pehla number: "))
        y = float(input("Doosra number: "))
        print("-" * 30)                       # divider line
        print(x, "+", y, "=", x + y)          # saaf format
        print("-" * 30)
        count += 1

    elif choice == "2":
        x = float(input("Pehla number: "))
        y = float(input("Doosra number: "))
        print("-" * 30)
        print(x, "-", y, "=", x - y)
        print("-" * 30)
        count += 1

    elif choice == "3":
        print("Dhanyavaad", name, "! Tumne", count, "calculations ki.")
        break

    else:
        print("Galat option! 1 se 3 ke beech chuno.")

        print("Galat option! 1 ya 2 chuno.")

