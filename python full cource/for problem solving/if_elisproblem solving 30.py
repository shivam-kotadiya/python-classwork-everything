# number = int(input("enter your number:"))
# if number > 0:
#     print("positive")
# elif number < 0:
#         print("negative")
# else:
#         print("zero")

#2

# num = int(input("Enter a number: "))

# if num == 0:
#     print("Zero")

# elif num > 0:
#     if num % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")

# else:
#     if num % 2 == 0:
#         print("Negative Even")
#     else:
#         print("Negative Odd")

#3
# number1 = int(input("enter your  first number:"))
# number2 = int(input("enter your  second number:"))
# if number1>number2:
#     print("number 1 is largest")
# elif number2>number1:
#     print("number 2 is largest")
# else:print("both are equal")

#4
# a = int(input("enter your first number:"))
# b = int(input("enter your second number:"))
# c = int(input("enter your third number:"))

# if a>=b and b>=c:
#     print("c")
# elif a>=b and c>=b:
#     print("b")
# else:print("a")

#5

# a = int(input("enter your first number:"))
# b = int(input("enter your second number:"))
# c = int(input("enter your third number:"))

# if a<=b and b<=c:
#     print(c,"is the largest")
# elif a<=b and c<=b:
#     print(b,"is the largest")
# else:print(a,"is the largest")


#6

# num = int(input("enter your number :"))
# if num % 5== 0 and num % 11== 0:
#     print("number num devided by both 5 and 11")
# elif num%5==0:
#     print("only by 5")
# elif num%11==0:
#     print("only by 11")
# else:
#     ("print neither")

#7

# num = int(input("enter your number :"))
# if num % 3== 0 and num % 7== 0:
#     print("number num devided by both 5 and 11")
# elif num%3==0:
#     print("only by 3")
# elif num%7==0:
#     print("only by 7")
# else:
#     ("print neither")

#8
# marks = int(input("enter your marks:"))
# if marks <0 :
#     print("invalid marks")
# elif marks >100:
#         print("invalid marks")
# elif marks >=40:
#             print("pass")
# else:
#        print("fail")


 
#9
# marks = int(input("Enter your marks: "))

# if marks < 0 or marks > 100:
#     print("Invalid marks")
# elif marks >= 90:
#     print("A")
# elif marks >= 80:
#     print("B")
# elif marks >= 70:
#     print("C")
# elif marks >= 60:
#     print("D")
# elif marks >= 40:
#     print("E")
# else:
#     print("Fail")/

#10
# age = int(input("enter your age:"))
# if age > 18:
#     print("can vote")
# elif age < 18:
#     print("can not vote")
# else: print("invalid age")
# 
# 11


#year=int(input("enter your age"))
#if year%400 == 0:
#    print("leep year")
#elif year % 4 == 0 and year % 100 != 0:
#    print("leep year")
#else:print("not a leep year")
 
#12
# cha = input("enter one character:")
# if  "A"<  cha < "z":
#     print("upper case")
# elif "0"<cha<"9":
#     print("number")
# elif "a"<cha<"b":                                         #wrong#
#     print("lower case")
# else:print("special character")

#13



#didnt make logick#




#14
# costprice=int(input("cost price"))
# sellingprice=int(input("selling price"))
# if sellingprice > costprice:
#     profit = sellingprice-costprice
#     print("profit =",profit)

# elif sellingprice<costprice:
#     loss=costprice-sellingprice
#     print("loss=",loss)

# else:
#     print("none")


#15
# costprice=int(input("cost price"))
# sellingprice=int(input("sellingprice"))
# if sellingprice > costprice:
#      profit = sellingprice-costprice
#      profitpersentage = profit/costprice*100
#      print(f"frofit is {profit} and profit persentage is {profitpersentage}" )

# elif sellingprice < costprice:
#      loss = sellingprice-costprice
#      losstpersentage = loss/costprice*100
#      print(f"loss is {loss} and loss persentage is {losstpersentage}" )

#16
#units = int(input("Enter units: "))

#if units <= 100:
 #   bill = units * 5

#elif units <= 200:
 #   bill = (100 * 5) + (units - 100) * 7

#else:
 #   bill = (100 * 5) + (100 * 7) + (units - 200) * 10

#print("Bill =", bill)

#17


# a=int(input("enter your first number"))

# b=int(input("enter your second number"))

# print(f"1.addition\n2.subtaration\n3.multiplication\n4.division\n5.flor division\n choose your opretion")

# aop=int(input("eneter your opretion number"))

# if aop == 1:

#     print(a+b)

# elif aop == 2:

#     print(a-b)

# elif aop == 3:

#     print(a*b)

# elif aop == 4:

#     print(a/b)

# elif aop == 5:

#     print(a//b)
# else:
#     print("you choose other number")





#18

# temperature=int(input("enter your temputer"))

# if temperature > 35:
#     print("hot")
# elif temperature >26 :
#     print("normal")
# elif temperature >16 :
#     print("cold")
# elif temperature >0:
#     print("very cold")
# else: print("freezing")


#19
# num = int(input("Enter a number: "))

# if num < 0:
#     print("Number is Negative")

# elif num <= 10:
#     print("Number is between 0 and 10")

# elif num <= 50:
#     print("Number is between 11 and 50")

# elif num <= 100:
#     print("Number is between 51 and 100")

# else:
#     print("Number is Above 100")





#20

# a = int(input("enter your first side"))
# b = int(input("enter your second side"))
# c = int(input("enter your third side"))

# if a+b>c:
#     print("valid")

# elif a+c>b:
#     print("valid")

# elif b+c>a:
#     print("valid")

# else:
#     print("in valid")


#21


# a = int(input("enter your first side"))
# b = int(input("enter your second side"))
# c = int(input("enter your third side"))

# if a+b<=c or a+c<=b or b+c<=a:
#     print("invalid")

# elif a>0 or b>0 or c>0:
#     print("valid")

# elif a==b and b==c and c==b:
#     print("equal")

# elif  a==b and b==c:
#     print("isosceles")

# else:
#     print("all ides diffrent")



    
#22
# balance = int(input("Enter account balance: "))
# withdrawal = int(input("Enter withdrawal amount: "))

# if withdrawal<balance:
#     print("in valid witrol amount")

# elif withdrawal %100 !=0:
#     print("invalid")                                        #use chat gpt#


# elif withdrawal > balance:
#     print("Insufficient balance")

# elif balance - withdrawal < 500:
#     print("At least ₹500 must remain")

# else:
#     balance = balance - withdrawal
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)


#23

# A_username = input("enter your name")
# A_password = input("enter your password")

# A_username == "shivam"
# A_password == 123

# if A_username != A_username:
#     print("invalid user name")
# elif A_password != A_password:
#     print("invalid password")

# elif A_username ==A_username and  A_password ==A_password:
#     print("login sucessful")


#24
# purchase = int(input("Enter purchase amount: "))

# if purchase < 500:
#     discount_percent = 0

# elif purchase < 1000:
#     discount_percent = 5

# elif purchase < 2000:
#     discount_percent = 10

# elif purchase < 5000:
#     discount_percent = 15

# else:
#     discount_percent = 20

# discount_amount = purchase * discount_percent / 100
# final_amount = purchase - discount_amount

# print("Original amount:", purchase)
# print("Discount percentage:", discount_percent, "%")
# print("Discount amount:", discount_amount)
# print("Final amount:", final_amount)



#25
# sub1 =int(input("enter marks of 1 subjest"))
# sub2 =int(input("enter marks of 2 subjest"))
# sub3 =int(input("enter marks of 3 subjest"))

# if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
#      print("Invalid marks! Marks must be between 0 and 100.")
 
# elif sub1 < 35 or sub2 < 35 or sub3 < 35:
#     print("Result: FAIL (Failed in one or more subjects)")
# else:
#      avg=(sub1 + sub2 + sub3)/3
#      print(avg)

#      if avg >= 75:
#           print("distinction")
#      elif avg >= 60:
#           print("first class")
#      elif avg >= 50:
#           print("second class")
#      else:
#           print("pass")


#26


# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))

# if month < 1 or month > 12:
#     print("Invalid")

# elif day < 1:
#     print("Invalid")

# elif month == 2:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         if day <= 29:
#             print("Valid")
#         else:
#             print("Invalid")
#     else:
#         if day <= 28:
#             print("Valid")
#         else:
#             print("Invalid")

# elif month == 4 or month == 6 or month == 9 or month == 11:
#     if day <= 30:
#         print("Valid")
#     else:
#         print("Invalid")

# else:
#     if day <= 31:
#         print("Valid")
#     else:
#         print("Invalid")








#27

# hours = int(input("Enter hours: "))
# minutes = int(input("Enter minutes: "))
# seconds = int(input("Enter seconds: "))

# if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
#     print("Valid time")
# else:
#     print("Invalid time")


#28

# name1 = input("Enter name of person 1: ")
# age1 = int(input("Enter age of person 1: "))

# name2 = input("Enter name of person 2: ")
# age2 = int(input("Enter age of person 2: "))

# name3 = input("Enter name of person 3: ")
# age3 = int(input("Enter age of person 3: "))

# if age1 == age2 and age2 == age3:
#     print("All three people are the same age")

# elif age1 == age2 and age1 < age3:
#     print(name1 + " and " + name2 + " are the youngest")

# elif age1 == age3 and age1 < age2:
#     print(name1 + " and " + name3 + " are the youngest")

# elif age2 == age3 and age2 < age1:
#     print(name2 + " and " + name3 + " are the youngest")

# elif age1 < age2 and age1 < age3:
#     print(name1 + " is the youngest")

# elif age2 < age1 and age2 < age3:
#     print(name2 + " is the youngest")

# else:
#     print(name3 + " is the youngest")



#29

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if (a > b and a < c) or (a < b and a > c):
#     print(a)

# elif (b > a and b < c) or (b < a and b > c):
#     print(b)

# else:
#     print(c)

#30
# age = int(input("Enter student age: "))
# marks = int(input("Enter marks: "))
# income = int(input("Enter family income: "))
# attendance = float(input("Enter attendance percentage: "))

# if age >= 18 and age <= 25 and marks >= 85 and attendance >= 75 and income <= 300000:
#     print("Scholarship Approved")
# else:
#     print("Scholarship Rejected")
