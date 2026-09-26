# 1


# str = input("enter your string")
# uppercase = 0
# lowercase = 0
# digits =0
# space =0
# specialcharacters =0

# for i in str:

#     if i.isupper():
#         uppercase+=1
#     elif i.islower():
#         lowercase+=1
#     elif i.isspace():
#         space+=1
#     elif i.isdigit():
#         digits+=1
#     else: specialcharacters+=1

# print(f" upper casre letters is {uppercase}")
# print(f"lower case letters is{lowercase}")
# print(f"digits is {digits}")
# print(f"space is {space}")
# print(f"special characters is {specialcharacters}")

    # still reaming



#2

# fail = 0
# pass1 = 0
# good = 0
# excellent = 0

# for i in range(1,11):
#     marks= int(input("enter your marks"))
#     if marks > 100:
#      A="enter valid marks"
#     elif marks>75:
#      A="ex"
#      excellent+=1
#     elif marks>50:
#      A="good"
#      good+=1
#     elif marks>35:
#      A="pass"
#      pass1+=1
#     else:
#      A="Fail"
#      fail+=1
#     print(A)

# print(f"fail{fail}")
# print(f"pass{pass1}")
# print(f"good{good}")
# print(f"excellent{excellent}")



#3
# str = input("enter your string")
# vowel = 0
# consonant = 0
# digit = 0
# specialcharacter =0
# score = 0

# for ch in str:
#     if ch.lower()in"aeiou":
#         vowel+=2
#     elif ch.isalpha():
#         consonant+=1
#     elif ch.isdigit():
#         digit+=3
#     else:specialcharacter+=4

# print(f"vowel is{vowel}")
# print(f"consonant is{consonant}")
# print(f"digit is{digit}")
# print(f"special is{specialcharacter}")


# still reaming



#4

# for i in range(1,6):
#     password = input("enter your password")

# length = False
# uppercase = False
# lowercase = False
# digit = False
# specialcharacter = False

# if len(password)>=8:
#     length=True

# for ch in password:
#     if "A"<= ch <="Z":
#         uppercase=True 

#     elif"a"<= ch <="z":
#         lowercase=True
#     elif 0<=ch<=9:
#         digit=True
#     else:
#         specialcharacter=True

# condition = 0
# if length==True:
#     condition+=1
# elif uppercase==True:
#     condition+=1
# elif lowercase==True:
#     condition+=1
# elif digit==True:
#     condition+=1
# else:specialcharacter==True
# condition+=1
# if condition ==5:
#     print("strong")
# elif condition==4:
#     print("med")
# else:print("low")




# still a problem 



#5

# sen = input("enter stetment:-")
# sen = sen.strip()
# word = sen.split()
# for wor in word:
#     print(wor)
#     if len(wor) > 6:
#         print("long")
#     elif len(wor) > 4:
#         print("medium")
#     elif len(wor) > 0:
#         print("short")



#6

#7



#8

# totel =0
# p1=0
# p2=0
# p3=0
# p4=0

# for i in range(8):
#     price=int(input("enter your price"))
#     if price>5000:
#         print("luxury")
#         p1+=1
#     elif price>2000:
#         print("primume")
#         p2+=1
#     elif price>500:
#         price("regular")
#         p3+=1
#     elif price>0:
#         price("budget")
#         p4+=1
#     totel+=price
# print(f"totle amount is {totel}")
# print(f"luxury is {p1}")
# print(f"premium is {p2}")
# print(f"regular is {p3}")
# print(f"budget is {p4}")
# print(f"average product price {totel/8}")



# #9
# text = input("emter a string")
# vowel =0
# consonant =0
# digit =0
# special =0

# for i in range(len(text)):

#     ch=text[i]
    

#     if i%2==0:
#         positiontype="even"
#     else:
#         positiontype="odd"

#     if ch.lower()in"aeiou":
#             chartype ="vowel"
#             vowel+=1

#     elif ch.isalpha():
#             chartype="consonant"
#             consonant+=1
#     elif ch.isdigit():
#             chartype="digit"
#             digit+=1

#     else:
#             chartype="special"
#             special+=1

#     # print(text).split()
#     # print(ch[0,999])


# print(vowel) 
# print(consonant) 
# print(digit) 
# print(special) 
# print(ch)



#10

# still a problem

# n= int(input("enter your number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("@")
# end=""



#11
# length = 0
# character = 0
# digit = 0
# underscore = 0
# invalid = 0

# for i in range (1,2):
#     username = input("enter your username")
#     length = len(username)
#     for char in username:
#         if char.isdigit():
#             digit+=1
#         elif char == "_":
#             underscore+=1
#         elif char.isalpha():
#             character+1        
#         else:
#             invalid+=1
# print("Length:", length)
# print("First character:", character)
# print("Digits:", digit)
# print("Underscores:", underscore)
# print("invalid:",invalid)

# if invalid>1:
#     print("invalid")
# elif length<5 or length>15:
#     print("need improment")
# else:
#     print("valid")


#12
# vowels =0
# consonant =0
# text = input("enter a string")

# for i in text:
#     if i.lower() in "aeiou":
#         vowels+=1
#     elif i.isalpha():
#         consonant+=1

# print("Vowels:", vowels)
# print("Consonants:", consonant)

# if vowels > consonant:
#     print("Vowels Win")
# elif consonant > vowels:
#     print("Consonants Win")
# else:
#     print("Draw")



#13

# revenue = 0
# for i in range(1, 7):
#     units = int(input("Enter electricity units: "))
#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = (100 * 5) + ((units - 100) * 7)
#     elif units <= 400:
#         bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
#     else:
#         bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 15)
#     print("Bill:", bill)
#     if bill < 1000:
#         print("Low")
#     elif bill <= 3000:
#         print("Medium")
#     else:
#         print("High")
#     revenue += bill
# print("Total Revenue:", revenue)


#14

# vowels=0
# consonants=0
# text = input("enter a string")
# for i in text:
#     if i.lower()in"aeiou":
#         vowels+=1
#     elif i. isalpha():
#         consonants+=1
# print("Vowels:", vowels)
# print("Consonants:",consonants )

# if vowels > consonants:
#         print("Vowels heavy")
# elif consonants > vowels:
#          print("Consonants heavy")
# else:
#     print("balance")


#15
# even = 0
# odd =0
# positive =0
# negative =0
# zero =0

# for i in range(3):
#     for j in range(3):
#         num=int(input("enter your number"))

#         if num %2 ==0:
#             even += 1
#         else: 
#             odd += 1 

#         if num>0:
#             positive += 1

#         elif num<0:
#             nagative += 1
#         else:
#             zero += 1


# print("Even count:", even)
# print("Odd count:", odd)
# print("Positive count:", positive)
# print("Negative count:", negative)
# print("Zero count:", zero)


#16
# uppercase =0
# lowercase =0
# digit =0
# specialcharacter =0

# password = input("enter your password")
# for i in password:
#     word =i
#     if word.isupper():
#         uppercase+=1
#     elif word.islower():
#         lowercase+=1
#     elif word.isdigit():
#         digit+=1
#     else:
#         specialcharacter+=1

# total = len(password)
# print(f"uppercase is",{uppercase})
# print(f"lowercase is",{lowercase})
# print(f" is digit",{digit})
# print(f"specialcharacte is",{specialcharacter})


#17

# A =0
# B =0
# C =0
# vowels =0
# consolant=0
# alphabat =0
# highestmarks=0
# highestmarks=0


# for i  in range(1,6):
#     marks = int(input("enter your marks"))
#     name = input("enter your name ")
#     if marks<35:
#         grade="c"
#         C+=1
#     elif marks>=55 and marks<80:
#         grade="B"

#         B+=1
#     else:
#         grade="A"

#         A+=1

#         for i in name:
#             if i.lower()in"aeiou":
#                 vowels+=1
#                 alphabat+=1

#             elif i.isalpha():
#                 alphabat+=1

#             elif i.isalpha():
#                 consolant+=1

#     print("Name:", name)
#     print("Marks:", marks)
#     print("Grade:", grade)
#     print("Vowels:", vowels)
#     print("Consonants:", consolant)
#     print("Characters:", alphabat)

#     if vowels >consolant :
#             print("Name has more vowels")
#     elif consolant > vowels:
#             print("Name has more consonants")
#     else:
#         print("Vowels and consonants are equal")

#     if marks > highestmarks:
#         highestmarks = marks
#         higheststudent = name


# print("Student with highest marks:", higheststudent)
# print("Highest marks:", highestmarks)


#18



# nOT NOW CANT MAKE A LOGICK




#19

# sentence = input("Enter a sentence: ")

# digit = 0
# dot = 0
# @ = 0
# password = 0
# special = 0

# for i in sentence:

#     if i.isdigit():
#         digit += 1

#     elif i == ".":
#         dot += 1

#     elif i == "@":
#         @ += 1

#     elif i in "!#$%^&*":
#         special += 1

# if digit >0 and dot>0 and 1@1>0:
#     print("review")

# elif special>=2:
#     print("specias")

# else:
#     print("safe")



#20



#dont know



#21

# total_discount = 0
# discount_20 = 0
# discount_15 = 0
# discount_10 = 0
# no_discount = 0

# for i in range(1, 3):
#     price = int(input("Enter your bill: "))

#     if price >= 5000:
#         discount = price * 20 / 100
#         discount_20 += 1

#     elif price >= 3000:
#         discount = price * 15 / 100
#         discount_15 += 1

#     elif price >= 1000:
#         discount = price * 10 / 100
#         discount_10 += 1

#     else:
#         discount = 0
#         no_discount += 1

#     final_price = price - discount
#     total_discount += discount

#     print("Discount:", discount)
#     print("Final Price:", final_price)

# print("20% Discount:", discount_20)
# print("15% Discount:", discount_15)
# print("10% Discount:", discount_10)
# print("No Discount:", no_discount)
# print("Total Discount:", total_discount)


#22


# not now out of syllabus


#23

# junior = 0
# mid = 0
# senior = 0
# executive = 0
# totalsalary = 0

# for i in range(8):
#     salary = int(input("Enter salary: "))

#     totalsalary += salary

#     if salary < 25000:
#         junior += 1

#     elif salary <= 50000:
#         mid += 1

#     elif salary <= 100000:
#         senior += 1

#     else:
#         executive += 1

# average = totalsalary / 8

# print("Junior:", junior)
# print("Mid:", mid)
# print("Senior:", senior)
# print("Executive:", executive)
# print("Average Salary:", average)


#24





#25

# E = 0
# O =0 
# T = 0
# F =0

# n = int(input("enter your number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j % 3 == 0 and j % 5 == 0:
#             print("F", end=" ")
#             F += 1

#         elif j % 3 == 0:
#             print("T", end=" ")
#             T += 1

#         elif j % 2 == 0:
#             print("E", end=" ")
#             E += 1

#         else:
#             print("O", end=" ")
#             O += 1

#     print()


# print(f"E = ", E)
# print(f"O = ", O)
# print(f"T = ", T)
# print(f"F = ", F)










       



                


        
    












    


