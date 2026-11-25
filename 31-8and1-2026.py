#from os import repla
#a="hello worlda shivam apple"
#="     apple"
#c=(b.lower()in a.lower())
#print(c)
#print(text.find("shivam"))
#print(text.count("a"))
#new = text.replace("shivam","sanjay")
#print(new)
#print(b.strip())
#print(a.replace("shivam","sanjay"))
#print(a.startswith("hello"))
#print(b.lstrip())
#print("shivam \nkotadiya\nsanjay bhai")


#name =  "AAA SSS"
#print(name != "AAA SSS")



# number = int(input("enter your number"))
# while number !=0:
#     print("you enter number is " , number)
#     number = int(input("enter your number"))
# print("loop ended")


# number = int(input("enter your number"))
# totle= 0
# while number != 0:
#     totle = number+totle
#     number = int(input("enter your number"))
# print("sum",totle)




# str1 = input("enter your str ").strip()
# rstr =""
# i = len(str1) -1
# while i >= 0:
#     rstr += str1[i]
#     i-=1
# if str1 == rstr:
#     print("string is paladrom") 
# else:
#     print("string is not paladrom")



# str1 = input("enter your string:")
# i =0
# j = len(str1) -1
# flag = True

# while (i<j):
#     if str1[i] == str1[j]:
#         i+=1
#         j-=1
#     else:
#         flag = False
#         i =j 
# if flag:
#     print("paladrom")
# else:
#     print("not a paladrom")


    

# number = 12345654

# while number >0:
#     digit = number % 10
#     print(digit)
#     number = number // 10




# number = int(input("enter your number "))
# total = 0
# while number >0:
#     digit = number % 10
#     total = total + digit
#     number = number // 10
# print("totel",total)





# number = int(input("enter your number"))
# reverce = 0
# while number >0:
#     digit = number % 10
#     reverce = reverce *10 + digit
#     number = number//10

# print("reverce" , reverce)




# i =1
# while i<10:
#     j =1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

# for i in range(20,5,-4):
#     print(i)


# number = int(input("Enter a number: "))
# reverse = 0
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10

# print("Reverse:", reverse)


# i = 1

# while i <= 5:
#     print(i)


# i = 10

# while i > 0:
#     print(i)
#     i = i - 1


# row = 1
# while row<=3:
#     colum = 1
#     while colum<=3:
#         print("#",end="")
#         colum +=1
#     print()
#     row +=1


row =1 
while row<=5:
    colum =1
    while colum<=row:
        print(colum,end="")
        colum = colum + 1
    print()
    row +=1