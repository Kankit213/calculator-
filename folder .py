# string and conditional statement

print("hello world")
print("hello world","this is my first code")
a = 10
b = 2.6
c = "hello world"
print(type(a))
print(type(b))
print(type(c))

#data type and numeric and variables
a = 10
print(a) #variables
print(type(a))
b = 3.8
print(b)
print(type(b))
c = "hello print"
print(c)
print(type(c))
#boolean data type
a = True
print(a)
print(type(a))
b = False
print(b)
print(type(b))

#set data type
a = {"a","b","c"}
print(a)
print(type(a))

#sequence data type
#list
a = [1,2,3,4,5]
print(a)
print(type(a))

#tuple
a = (1,2,3,4,5)
print(a)
print(type(a))

#string

a = "python program"
print(a)
print(type(a))

#dictionary data type

a = {"key" : "value"}
print(a)
print(type(a))

#operators

a = 10
b = 20
sum = a+b
print(sum)

a = 30
b = 10
diff = a-b
print(diff)

a = 20
b = 5
multi = a*b
print(multi)

a = 50
b = 5
divide  = a/b
print(divide)

a = 30
b = 7
modules = a%b
print(modules)

a = 38
a += 1
print(a)

a = 45
a -= 2
print(a)

#assignment operator
#equal to operator
x = 25
print("x : ",x)

#add and equal to operator

a = 25
a+=5
print("a : ",a)

#substation and equal to

a = 300
a-=5
print("a : ",a)

#multi and equal to

a = 30
a*=5
print("a : ",a)

#decide and equal to

a = 500
a/=5
print("a = ",a)

#left shift assignment operator
a = 10
a<<=2
print("a : ",a)

#right shift assignment operator

a = 50
a>>= 3
print("a : ",a)

a = 50
b = 10
c = a&b
print("a : ",c)
print("b : ",b)

a = 20
b = 10
a^=b
print("a : ", a)

a = 50
b = 10
a /= b
print("a : ", a)

#comparison operator
#greater than
a = 30
b = 20
c = a>b
print(c)

#less than
x = 60
y = 50
xy = x<y
print(xy)

#greater than or equal to
a = 200
b = 40
x = a>=b
print(x)

#less than aur equal to

a = 40
b = 35
x = a>b
print(x)

#equal to

a = 40
b = 40
x = a==b
print(x)

#not equal to

a = 20
b = 30
x = a!=b
print(x)


#logical operator
#and operator

a = 20
print(a > 15 and a < 10)

#or operator
a = 15
print(a>12 or a<8)

#not operator
a = 15
print(a>10 and not a<12)

#identity operator
x = ["apple","mango"]
y = ["apple","mango"]
z = x
print(x is z) #that obj is matching that's why it returns true

print(x is y) #that obj is not matching that's why it has given false

#membership operator
x = ["apple","mango"]
print("banana" in x)

#not in operator
y = ["apple","mango"]
print("guava" not in y)



str1 = "This is the first string.\nWe are my own coding."
str2 = "This is the first string.  \t  we are my own coding."
print(str1)
str1 = "This is the first string.\nWe are my own coding."
print(str1)

str1 = "This is the first string.\nWe are my own coding."
print(str1)

str1 = "Apnea"
str2: str = "collage"
final_str = str1 + str2
print(final_str)

#indexing

str1 = "hello world"
len1 = len(str1)
print(len1)

a = "hello " + "" + "world"
print(a)
print(len(a))

str = "apnea collage"
ch = str[2]
print(ch)

str = "hello world"
bc = str[8]
print(bc)

#slicing
str = "helloworld"
print(str[0:11])
print(str[0 :])
print(str[0:5])
print(str[:5])

#slicing negative index

str = "hello world"
print(str[-8:-2])

#string function

str = "i am studying coding with apnea collage"
print(str.endswith ("age"))

str = "apnea collage"
print(str.endswith ("col"))

#capitalize
print(str.capitalize())
print(str)

#replace

print(str.replace("apnea" , "user"))

#find
str = "i am from studying from coding with apnea collage"
print(str.find("with"))

#count

#list

marks = [45.6,78.9,45.8,98.7]
print(marks)
print(type(marks))
print(marks[1])
print(marks[3])

#2
student = ["decline",123,56.7,"clever"]
print(student)
print(type(student))
print(student[0])
student[0] = "ankit"
print(student)
print(student[0])


#list slicing

marks = [45,67,87,89,54]
print(marks[1:4])
print(marks[:4])
print(marks[0:])
print(marks[1:5])
print(marks[-3:-1])

#list method

list = [2,3,4,5]
list.append(6)
print(list)

list = ["ankit","sonu","suraj"]
list.append("moti")
print(list)

#ascending order
list = [3,4,5,2,1]
print(list.sort())
print(list)

#descending order
list = [1,5,7,4,3,2]
print(list.sort(reverse = True))
print(list)

list = ['a','d','f','c','b','e']
print(list.sort(reverse = True))
print(list)

#reverse order

list = [2,3,4,5,6,7,8,9,2]
list.reverse()
print(list)

#insert

list = [3,4,2,1]
list.insert(2,5)
print(list)


#remove method
list = [2,3,1,4,5]
list.remove(3)
print(list)

#pop

list = [3,4,2,1,5]
list.pop(3)
print(list)

#tuples in python

tup = (2,3,4,5,6)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])

tup = (1,)
print(tup)
print(type(tup))

tup = (2,3,4,5,6)
print(tup[0:])
print(type(tup))

#tuple method

#index method
tup = (1,2,3,4,5,6,)
print(tup.index(6))

#count method
tup = (1,2,3,4,5,6,6)
print(tup.count(4))


#practice

lis = ["Alibaba","here here","yantra"]
print(lis)
print(type(lis))

movies = []
mov1 = input("enter movie name : ")
mov2 = input("enter movie name : ")
mov3 = input("enter movie name : ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()
if copy_list1==list1:
    print("palindrome")
else:
    print("NOT palindrome")

list2 = ["madam","ayah","madam","sir"]

copy_list2 = list2.copy()
copy_list2.reverse()

if copy_list2 == list2 :
    print("palindrome")
else:
    print(" NOT palindrome")


list3 = [2,3,4,5,4,3,2,5]
copy_list3 = list3.copy()
copy_list3.reverse()
if copy_list3 == list3:
    print("palindrome")
else:
    print("NOT palindrome")

grade = ("a","c","d","a","a","c","a")
print(grade.count("a"))

list = ["a","c","d","a","a","c","a"]
print(list.sort())
print(list)

grade = ["C","D","A","A","C","A"]
grade.sort()
print(grade)

#dictionary in python

info = {
    "hello" : "world",
    "good" : "morning"
}
print(info)
print(type(info))

info = {
    "hello" : "world",
    "good" : "morning"
}
print(info)
print(type(info))

info = {
    "hello" : "world",
    "name" : "ankit",
    "learn" : "coding python",
    "learning" : ["python","java","c++","java script"],
    "topics" : ("dict","str"),
    "age" : 35,
    "is adult" : True,
    "marks" : 82.4
}
print(info)
print(type(info))
print(info["name"])
print(info["learn"])
print(info["learning"])
info["name"] = "ankit kumar"
print(info)
info["age"] = 18
print(info)
info["surname"] = "chaurashiya"
print(info)

nul_dict = {"ankit kumar"}
print(nul_dict)
nul_dict = {}
nul_dict["name"] = "ankit kumar"
print(nul_dict)

#nested dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
print(student)
print(student["subject"])

print(student["subject"]["phy"])
print(student["subject"]["math"])

#key method dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}

print(student.keys())
print(student.values())

print(len(student.keys()))

#values method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
print(student.values())
print(student)
print(student.values())

#.items method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
print(student.items())
pairs = (student.items())
print(pairs)

#get method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}

print(student["name"])
print(student.get("name"))
print(student.get("subject"))

#update method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
new_dict = {"city": "new town","age":18}
student.update(new_dict)
print(student)


