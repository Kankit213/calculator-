#1 : fixed number addition
# a = 12
# b = 10
# c = a+b
# print(c)
#
# #verity 2 : #addition using float input
# #
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
#
# result  = x+y
# print("result", result )
#
# #verity 3 : ##addition using integer input
#
# x = int(input("Enter first  number: "))
# y = int(input("Enter second  number: "))
#
# result = x +y
# print("result : ", result)
#
# #verity 4 : addition using +=
#
# total = 0
# total += 10
# total +=20
# total += 30
# result = total
# print("total = ", result)
#
# #verity 5 : addition using a for loops
#
# n = int(input("how meny numbers add : ", ))
# total = 0
# for i in range(2):
#     num = float(input("enter number: "))
#     total += num
# print("Total:", total)
#
# n = int(input("how meny numbers add :   ", ))
# total = 0
# for i in range(3):
#     num = float(input("enter number: "))
#     total += num
# print("total:", total)
#
#
# #verity 6 : addition using a while loops
#
# total = 0
# count = 0
#
# while True:
#     user_input = input("number dalo (katam karne ke lie done like: ")
#     if user_input == "done":
#         break
#     total += float(user_input)
#     count += 1
# print("total = ", total)
# print("count = ", count)
#
# total = 0
# count = 0
#
# while type:
#     marks = input("Enter marks(end ke lie hello like: ")
#     if marks == "hello":
#         break
#     total += float(marks)
#     count += 1
# print("total = ", total)
# print("count = ", count)
#
# total = 0 # agar hum total ke gajah 1 karenge toh 1 add ho jayega new data me
# count = 1 # hum dono data ko same nahi kar skte  alag _ alag karenge tab hi output ayega
#
# while True:
#     value = input("Number dijiye (ya 'stop' like): ")
#     if value == "stop":
#         break
#     total += float(value)
#     count += 1
#
# print("Total result :", total)
# print(" total Count:", count)
#
# #all in one : ( using all in one add , subst , multiple , devide )
# #add + subtraction + multiple + devide
# choice = input("chose one number (1_5) : ")
#
# if choice =="5":
#     print(" dhanyavaad!  calculator band ho rha hai ")
#
#
# if choice in ["1","2","3","4"]:
#     num1 = float(input("enter first number: "))
#     num2 = float(input("enter second number: "))
#
#     if choice == "1":
#         print("result : ",num1 + num2)
#     elif choice == "2":
#         print("result : ",num1 - num2)
#     elif choice == "3":
#         print("result : ",num1 * num2)
#     elif choice == "4":
#
#         if num2 == 0:
#             print("error : 0 se devide nahi kar skte! ")
#         else:
#             print("result : ", num1 / num2)
#     else:
#         print("galat option! 1se 5 kr bich chuno.")
#
# #
# # substraction method

# #verity 1 : fixed number substitution
#
# a = 20
# b = 10
# subst = a-b
# print(subst)
#
# #verity 2 : substitution using integer input
#
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
#
# subs = x-y
# print("result = ", subs)
#
# #verity 3 : : substitution using float  input
#
# x = float(input("Enter a number: "))
# y = float(input("Enter another number: "))
#
# subs = x-y
# print("result = ", subs)
#
# #verity 4 : : substitution using -=
#
# total = 100
# total-=10
# total-=20
# total-=30
# print("total = ", total)
#
# #verity 5 : : substitution using a for loop
#
# n = int(input("how meny number subst: "))
# total = float(input("Enter first number: "))
#
# for i in range(n-1):
#     num = float(input("Enter number: "))
#     total -= num
#
# print("total = ", total)
#
# n = int(input("how meny number subs: "))
# total = float(input("Enter first number: "))
# for i in range(n-1):
#     num = float(input("Enter number: "))
#     total -= num
# print("total = ", total)
#
#
# #verity 6 : : substitution using a while loop
#
# total = 0
# count = 0
# first_number = True
#
# while True:
#     marks = input("Enter marks(band Carne ke lie stop like: ")
#     if marks == "stop":
#         break
#     num = float(marks)
#     if first_number:
#         total = num
#         first_number = False
#     else:
#         total -= num
#
#     count += 1
#
# print("total = ", total)
# print("count = ", count)
#
# total = 0
# count  = 0
# first_number = True
# while True:
#     marks = input("Enter a number(stop Carne ke lie hello like: ")
#     if marks == "hello":
#         break
#     num = int(marks)
#     if first_number:
#         total = num
#         first_number = False
#     else:
#         total -= num
#     count += 1
# print("total : ", total)
# print("count : ", count)
#
#
# # multiple method
#
# #verity 1 : fixed value multiple
#
# a = 20
# b = 10
# c = a*b
# print(c)
#
# # verity 2 : multiple using integer value
# #
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
#
# multiple = x*y
# print("result = ", multiple)
#
# # verity 3 : multiple using float value
#
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
#
# multiple = x*y
# print("result of multiple = ", multiple)
#
# #verity 4 : multiple using *=
#
# total = 10
# total*=2
# total*=5
# print("total = ", total)
#
# #verity 5 : using for a loop
# result = 1
# n = int(input("kitne numbers ko multiple Carne hai : "))
#
# for i in range(n):
#     num = float(input(" number daloo: "))
#     result = result * num
# print("final multiplication result : ", result)
#
# # #verity 6 : using awhile loop
#
# result = 1
#
# while True:
#     val = input("Number daalo (rukne ke liye 'stop' likho): ")
#
#     if val == "stop":
#         break
#
#     num = float(val)
#     result *= num
#
# print("Final Multiplication Result =", result)
#
#
# # result = 1
# while True:
#      marks = input("Marks dalo (rukne ke liye bye like: ")
#      if marks == "bye":
#         break
#      marks = float(marks)
#      result *= marks
# print("Final Multiplication Result =", result)
#
# #division method
# #verity 1 : fixed value divide
# a = 200
# b = 40
# c = a/b
# print(c)
#
# #verity 2 : divide using integer value
#
# x = int(input("Enter  first number : "))
# y = int(input("Enter  second number : "))
#
# divide = x/y
# print("result of division : ",divide)
#
# # #verity 3 : divide using float input
#
# x = float(input("Enter  first number : "))
# y = float(input("Enter  second number : "))
#
# divide = x/y
# print("result of division : ",divide)
#
# #verity 4 : divide using /=
#
# total = 500
# total /=100
# print("result of division : ",total)
#
# # #verity 5 :divide using  average (a+b)/2
#
# a = float(input("enter  avg first number : "))
# b = float(input("enter  avg second number : "))
#
# print("average of  : ",(a+b)/2)
#
#
# #verity 6 "divide using a for loop
#
#
# n = int(input("Kitten numbers divide Carne hai: "))
#
# result = float(input("Paula number dale: "))
#
# for i in range(n - 1):
#     num = float(input("Agla number dale: "))
#
#     if num == 0:
#         print("0 se divide nah kar skate.")
#         break
#
#     result /= num
#
# print("Current Result =", result)
# #
# n = int(input("Kitten numbers divide Carne hai: "))
# result = float(input("Pahla number dale: "))
# for i in range(n - 1):
#     num = float(input("Agla number dale: "))
#     if num == 0:
#         print("0 se divide nah kar skate.")
#         break
#     result /= num
# print("division  Result =", result)
#
# #verity 7 : division using awhile loop
#
#
# result = None
#
# while True:
#     value = input("Number dale (band Carne ke lie bye like): ")
#
#     if value == "bye":
#         break
#
#     num = float(value)
#
#     if result is None:
#         result = num
#     else:
#         if num == 0:
#             print("0 se divide nah kar skate.")
#             break
#
#         result = result / num
#
# if result is not None:
#     print("Final Division Result =", result)
#
#

#
# result =    None # abhi result nahi hai yaha kuch
#
# while True: # niche ka kmm kro
#     marks = input("enter marks(Rockne ke lie done like) : ")
#     if marks == "done": # agar divide ko Rockne hao to done liko
#         break # eska matlab ab age nah bodega
#     num = float(marks)
#     if result is None:
#         result = num
#     else:
#         if num == 0:
#             print("you can't divide by zero")
#         else:
#             result /= num
#
# if result is not None:
#         print("final division result : ", result)
#
# result = None
# while True:
#     marks = input("enter marks(Rockne ke lie bye like) : ")
#     if marks == "bye":
#         break
#     marks = float(marks)
#     if result is None:
#         result = marks
#     else:
#         if marks == 0:
#             print("you can't divide by zero")
#         else:
#             result /= marks
#
# if result is not None:
#     print("final division result : ", result)
#
#
# result = None
# while True:
#     marks = input("enter marks(Rockne ke lie hello liko) : ")
#     if marks == "hello":
#         break
#     marks = float(marks)
#     if result is None:
#         result = marks
#     else:
#         if marks == 0:
#             print("you can't divide by zero")
#         else:
#             result  /= marks
#
#
# if result is not None:
#     print("final division result : ", result)

#method 2

# print("-"  * 30)
# print("     ANKIT,S CALCULATOR")
# print("-" * 30)


# name = input("your nam kya hai : ")
# print("namaste :",name)
#
# count = 0
# while True:
#     print("|n1. Add(+)")
#     print("2. exit")
#     choice = input("option chunoo : ")
#
#     if choice == "1":
#         x = float(input("first number"))
#         y = float(input("second number"))
#         print("-" * 30)
#         print(x, "x", y, "=", x*y)
#         print("-" * 30)
#         count = count + 1
#     elif choice == "2":
#         print("danayvada", name,"!tumne",count,"calculation ki")
#         break
#     else:
#         print("galat option! 1 ya 2 chuno.")


# print("=" * 30)
# print("    ANKIT,S CALCULATOR : ")
# print("=" * 30)
#
# name = input("enter your name : ")
# print("namaste",name, "!")
#
# count = 0
#
# while True:
#     print("|n1. Add(+)")
#     print("2 . exit")
#     choice = input("your choice : ")
#     if choice == "1":
#         x = float(input("enter first number : "))
#         y = float(input("enter second number : "))
#         print("-" * 30)
#         print(x,"+",y,"=",x+y)
#         print("-" * 30)
#         count = count + 1
#     elif choice == "2":
#         print("Danayavad",name, "!tumne",count,"calculation ki.")
#         break
#
#
#     else:
#         print("Galat option! 1 ya 2 chuno.")


# print("=" * 30)
# print("    ANKIT,S CALCULATOR")
# print("=" * 30)
#
# name = input("enter your name : ")
# print("namaste : ",name, "!")
# count = 0
#
# while True:
#     print("|n1 . add(+)")
#     print("2 = exit")
#     choice = input("your choice : ")
#     if choice == "1":
#         x = float(input("enter first number : "))
#         y = float(input("enter second number : "))
#         print("-" * 30)
#         print(x,"+",y,"=",x+y)
#         print("-" * 30)
#         count = count  + 1
#         print("-" * 30)
#     elif choice == "2":
#         print("danyavad ",name, "!tune",count,"calculation ki.")
#         break
#     else:
#         print("-" * 30)

# print("=" * 30)
# print("    substraction ,s calculator : ")
# print("=" * 30)
# name = input("apnea name like : ")
# print("welcome", name,"!")
# count = 0
#
# while True:
#     print("|n1 , add(+)")
#     print(2 , exit)
#     choice = input("your choice : ")
#     if choice == "1":
#         x = float(input("enter first number : "))
#         y = float(input("enter second number : "))
#
#         print("-" * 30)
#         print("sum =",x+y)
#         print("-" * 30)
#     elif choice == "2":
#         print("danayvadd",name,"!tune",count,"calculation ki")
#         break
#     else:
#         print("-" * 30)

# print("-"*30)
# print("   ANKIT'S CALCULATOR")
# print("-"*30)
#
# name = input("Please enter your name: ")
# print("namaste : ", name)
#
# count = 0
#
# while True :
#     print("\n1. add(+)")
#     print("2. exit")
#     choice = input ("option chuno : ")
#     if choice == "1":
#         print("\n------- ADD--------")
#         print("1 do numbers")
#         print("2. teen numbers")
#         print("3. kai numbers (n barr)")
#         print("4. kai numbers done likhne tak: ")
#         print("5. wapas jao : ")
#         sub = input("sub_option chuno")
#         if sub == "1":
#             x = float(input("Please first number: "))
#             y = float(input("Please second number: "))
#             print("-" * 30)
#             print(x,"+",y,"=",x+y)
#             print("-" * 30)
#             count+=1
#         elif sub == "2":
#             x = float(input("Please first number: "))
#             y = float(input("Please second number: "))
#             z = float(input("Please third number: "))
#             print("-" * 30)
#             print("total: ", x+y+z )
#             print("-" * 30)
#             count+=1
#         elif sub == "3":
#             n = int(input("kitne numbers add karne hai : "))
#             total = 0
#             for i in range(n):
#                 num = float(input("Please number dale: "))
#                 total += num
#             print("-" * 30)
#             print("total: ", total)
#             print("-" * 30)
#             count+=1
#         elif sub ==  "4":
#             total = 0
#             while True:
#                 value = input("numbers dalo (katam karne ke liye done : ")
#                 if value == "done":
#                     break
#                 total += float(value)
#             print("-" * 30)
#             print("total: ", total)
#             print("-" * 30)
#             count+=1
#         elif sub == "5":
#             print("mai menun pe wapas ja raha hu : ")
#         else:
#             print("galat sub option : ")
#     elif choice == "2":
#         print("danyavadd", name,"!tune",count,"calculator ki.")
#         break
#     else:
#         print("galat option ! 1 ya 2 chuno ")



# print("-"*30)
# print("    ankit calculator")
# print("-" * 30)


# now = ("addition : ")
# print("now : ",now)

# count = 0

# while True:
#     print("|n1 . add(+)")
#     print("2 . exit")
#     choice = input("option chuno : ")
#     if choice=="1":
#         x = float(input("first number : "))
#         y = float(input("second number : "))
#         print("-"* 30)
#         print(x,"+",y,"=",x+y)
#         print("-"* 30)
#         count+=1

#     elif choice == "2":
#         print("danyavadd",now , "!tumne", count,"calculation ki")
#         break
#     else:
#         print("galat option ! 1 ya 2 option chune")
# #method 2

# print("-" * 30)        
# print("     ankit's calculator")
# print("-"*30)

# name = input("your name : ")
# print("namaste", name)

# count = 0
# while True:
#     print("|n1 . add(+)")
#     print("2 . exit")
#     choice = input("option chuno : ")
#     if choice == "1" :
#         print("-----addition------")     
#         print("1. doo number") 
#         print("2 . teen number") 
#         print("3 . kai number (n barr)")
#         print("4 . kai number(done likhne tak)")
#         print("5  . wapas jao ")
#         sub = input("sub option chuno: ")

#         if sub == 1:
#             x = float(input("first number : "))
#             y = float(input("second number : "))
#             print("-"* 30)
#             print(x,"+", y,"=",x+y)
#             print("-"*30)
#             count+=1
#         elif sub == "2":
#             a = float(input("first number : "))    
#             b = float(input("second number : "))
#             c = float(input("thord number : "))
#             print("-"*30)
#             print("total: , a+b+c")
#             print("-"*30)
#             count+=1
#         elif sub == "3":
#             n = int(input("kitne number add karne hai : "))    
#             total = 0
#             for i in range(n):
#                 num = float(input("numbers daloo : "))
#                 total += num
#             print("-"*30)  
#             print("total: ",total) 
#             print("-"*30) 
#             count += 1
#         elif sub == "4":
#             total = 0
#             while True:
#                 value = input("number dalo (katam ke liye done liko : )") 
#                 if value == "done" :
#                     break
#                 total = float(value)  
#             print("-"*30)
#             print("total",total)
#             print("-"*30)
#             count +=1
#         elif sub == "5":
#             print("mai menu pe wapas ja raha hu  ")
#         else:
#             print(" galat option ") 
#     elif choice== "2"  :
#         print("thanks", name,"!tumne", count,"calculation ki")
#         break
#     else:
#         print("galat option 1 ya 2 chunoo ")


        
print("-"*30)
print("    ankit's calculator")
print("-"*30)
        
name = input("enter your name : ")
print(" nmaste", name)

count = 0
while True:
    print("\n1 . substract(-)")
    print("2 . exit ")
    choice = input("option chuno :  ")
    if choice == "1":
        print("\n------substract-------")
        print("1. do numbers ")
        print("2. teen numbers ")
        print("3 . kai numbers (n barr)")
        print("4. kai numbers (done likhne tak )")
        print("5 . wapas jao ")
        sub = input ("sub option chuno :  ")

        if sub == "1":
            x = float(input("first numbers : "))
            y = float(input("second numbers : "))
            print("="*30)
            print(x, "-", y,"=", x-y)
            print("="*30)
            count +=1
        elif sub == "2":
            x = float(input("first number : "))
            y = float(input("second numbers : "))  
            z = float(input("third numbers : "))
            print("="*30)
            print("total", x-y-z)
            print("="*30)
            count+=1
        elif sub == "3":
            n = int(input("kitne numbers addd kar ne hai : "))
            total = 0
            for i in range(n):
                num = float(input("numbers daloo : "))
                total+=1
            print("="*30)
            print("total: ", total) 
            print("="*30)
            count+=1
        elif sub =="4" :
            total = 0
            while True:
                value = input("numbers dalo(rokne ke liye done:  )")  
                if value=="done":
                    break
                total = float(value)
            print("="*30)
            print("total", total) 
            print("="*30)
            count +=1
        elif sub =="5":
            print("mai menu pe wapas ja raha hu ---- ")   
        else:
            print("galat sub option")
    elif choice == "2":
        print("danyavadd",name,"!tumne",count,"calculation ki")
        break
    else:
        print("galat option 1 ya 2 chuno ")         
    
        
       
print("=" * 30)
print("   ANKIT'S substraction CALCULATOR")
print("=" * 30)

name = input("Tumhara naam kya hai?  ")
print("Namaste", name, "!")

count = 0   # kitni calculations hui

while True:
    
    print("2. Subtract (-)")
    print("3. Exit")
    choice = input("Option chuno: ")

    if choice == "1":
        x = float(input("Pehla number: "))
        y = float(input("Doosra number: "))
        z = float(input("tisra numbers : "))
        print("-" * 30)
        print(x, "-", y,"-", z, "=", x - y - z)
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


              
        


