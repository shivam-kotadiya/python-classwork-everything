
# day = 6
# match day:
#     case 1 | 2 | 3 | 4 | 5 :
#         print("weekday")
#     case 6|7:
#         print("weekend")



# marks = 87
# match marks:
#     case X if X >=90:
#         print("A")
#     case X if X >=75:
#         print("B")
#     case X if X >=60:
#         print("C")
#     case X if X >=50:
#         print("D")
#     case X if X >=40:
#         print("E")


# account = input("enter your account")      #"student"  # "teacher" # "admin"
# account2 = input("enter your account")      #"student"  # "teacher" # "admin"
# choice =  int(input("enter your choice"))   #1 #2 #3 #4

# match account:
#     case "student":
#         match choice:
#             case 1 :
#                 print("view attendence")
#             case 2 :
#                 print("Apply for leave")
#             case 3 :
#                 print("for dealy sechudel")
#             case 4 :
#                 print("contack to teacher")
#             case _:
#                 print("invalid")

#     case "teacher":
#         match choice:
#             case 1:
#                 print("apply for leave")
#             case 2:
#                 print("contack student parents")
#             case 3:
#                 print("see exam schedul")
#             case 4:
#                 print("see studenrt result")
#             case _:
#                 print("invalid")

#     case "admin":
#         match choice:
#             case 1:
#                 print("apply for leave (admin)")
#             case 2:
#                 print("contack student parents(admin)")
#             case 3:
#                 print("see exam schedul(admin)")
#             case 4:
#                 print("see studenrt result(admin)")
#             case _:
#                 print("invalid")



# match account2:
#     case "student":
#         match choice:
#             case 1 :
#                 print("view attendence")
#             case 2 :
#                 print("Apply for leave")
#             case 3 :
#                 print("for dealy sechudel")
#             case 4 :
#                 print("contack to teacher")
#             case _:
#                 print("invalid")

#     case "teacher":
#         match choice:
#             case 1:
#                 print("apply for leave")
#             case 2:
#                 print("contack student parents")
#             case 3:
#                 print("see exam schedul")
#             case 4:
#                 print("see studenrt result")
#             case _:
#                 print("invalid")

#     case "admin":
#         match choice:
#             case 1:
#                 print("apply for leave (admin)")
#             case 2:
#                 print("contack student parents(admin)")
#             case 3:
#                 print("see exam schedul(admin)")
#             case 4:
#                 print("see studenrt result(admin)")
#             case _:
#                 print("invalid")
            

# str = input("enter your str").strip()
# flag=True
# count = 0
# for ch in str:
#     if ch=="o":
#         count +=1
#         flag=False
#         print("found")
#         print(count)
#         break
#     flag = True
#     print("not found")



# str=input("enter your string").strip()
# count =0
# flag = True
# for i in range (0,len(str)):
#     if str[i] == "o":
#         count += 1
#         flag = False
#         print("found")
#         print(count)
#         break
# if flag == True:
#     print("Not found")




# str=input("enter your string").strip()
# count =0
# flag = True
# while i in range (0,len(str)):
#     if str[i] == "o":
#         count += 1
#         flag = False
#         print("found")
#         print(count)
#         break
# if flag == True:
#     print("Not found")


# number = int(input("enter your number 1.last 2.mid 3.first" ))
# match number:
#     case 1 :
#         print("you are now at  first number ")
#     case 2 :
#         print("you are now at last number ")
#     case 3 :
#         print("you are now at  second number ")


for i in range(1,6):
    if i == 4:
        break
    print(i)