#1

# num = int(input("eneter menu number:-"))
# match num:
#     case 1:
#         print("Pizza")
#     case 2:
#         print("Burger")
#     case 3:
#         print("pasta")
#     case 4:
#         print("sandwich")num = int(input("eneter menu number:-"))

#2
# num = int(input("enter setting number:-"))
# match num:
#     case 1:
#         print("wi-fi")
#     case 2:
#         print("Bluetooth")
#     case 3:
#         print("Mobile data")
#     case 4:
#         print("Airplane Mode")
#     case 5:
#         print("exit")
#     case _:
#         print("enter valid number:-")

#3

# num = int(input("enter atm menu number:-"))
# match num:
#     case 1:
#         print("check balance")
#     case 2:
#         print("Withdraw money")
#     case 3:
#         print("Deposite money")
#     case 4:
#         print("Change money")
#     case 5:
#         print("exit")
#     case _:
#         print("enter valid number:-")

#4

# col = input("enter light colour:-")
# match col:
#     case "red":
#         print("stop")
#     case "yello":
#         print("wait")
#     case "green":
#         print("Go")
#     case _:
#         print("not in signal")

#5

# num = int(input("enter student portal number:-"))
# match num:
#     case 1:
#         print("View Profile")
#     case 2:
#         print("View Courses")
#     case 3:
#         print("View Marks")
#     case 4:
#         print("View Attendance")
#     case 5:
#         print("Logout")
#     case _:
#         print("enter valid number:-")

#6

# num = int(input("eneter shopping menu number:-"))
# match num:
#     case 1:
#         print("Electronics")
#     case 2:
#         print("Clothing")
#     case 3:
#         print("Books")
#     case 4:
#         print("Grocery")
#     case 5:
#         print("Exit")
#     case _:
#         print("enter valid number:-")

#7

# num = int(input("eneter Banking menu number:-"))
# match num:
#     case 1:
#         print("Account Balance")
#     case 2:
#         print("Mini Statement")
#     case 3:
#         print("Fund Transfer")
#     case 4:
#         print("Bill Payment")
#     case 5:
#         print("Customer Support")
#     case _:
#         print("enter valid number:-")

#8

# num = int(input("eneter movie Ticket menu number:-"))
# match num:
#     case 1:
#         print("Morning Show")
#     case 2:
#         print("Afternoon Show")
#     case 3:
#         print("Evening Show")
#     case 4:
#         print("Night Show")
#     case _:
#         print("enter valid number:-")

#9

# weather = input("Enter weather: ")

# match weather:
#     case "sunny":
#         print("Wear sunglasses")

#     case "rainy":
#         print("Carry an umbrella")

#     case "cloudy":
#         print("Weather may change")

#     case "snowy":
#         print("Wear warm clothes")

#     case _:
#         print("Unknown Weather")

#10

# payment = input("Enter payment method: ")

# match payment:
#     case "upi":
#         print("UPI Payment Selected")

#     case "card":
#         print("Card Payment Selected")

#     case "cash":
#         print("Cash Payment Selected")

#     case "wallet":
#         print("Wallet Payment Selected")

#     case _:
#         print("Invalid Payment Method")

#11

# extension = input("Enter extension: ")

# match extension:
#     case "pdf":
#         print("Document File")

#     case "jpg":
#         print("Image File")

#     case "png":
#         print("Image File")

#     case "mp3":
#         print("Audio File")

#     case "mp4":
#         print("Video File")

#     case _:
#         print("Unknown File Type")

#12

# role = input("Enter role: ")

# match role:
#     case "admin":
#         print("Full Access")

#     case "teacher":
#         print("Teacher Dashboard")

#     case "student":
#         print("Student Dashboard")

#     case "guest":
#         print("Limited Access")

#     case _:
#         print("Invalid Role")

#13

# day = int(input("enter umber:-"))
# match day:
#     case 1 | 2 | 3 | 4 | 5 :
#         print("weekday")
#     case 6 | 7:
#         print("weekend day")
#     case _:
#         print("invalid number")

#14

# priority = int(input("Enter priority number: "))

# match priority:
#     case 1 | 2:
#         print("Normal Priority")
#     case 3 | 4:
#         print("Urgent Priority")
#     case _:
#         print("Invalid Priority")

#15

# membership = int(input("Enter membership level: "))
# match membership:
#     case 1 | 2:
#         print("Basic Membership")
#     case 3 | 4:
#         print("Premium Membership")
#     case _:
#         print("Invalid Membership")

#16

# user_type = int(input("Enter user type: "))
# match user_type:
#     case 1:
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print(" Student Courses")
#             case 2:
#                 print(" Student Marks")
#             case 3:
#                 print(" Student Attendance")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         option = int(input("Enter option: "))
#         match option:
#             case 1:
#                 print(" Teacher Students")
#             case 2:
#                 print(" Teacher Marks")
#             case 3:
#                 print(" Teacher Attendance")
#             case _:
#                 print("Invalid Option")
#     case _:
#         print("Invalid User Type")

#17

# account = int(input("Enter account type: "))

# match account:
#     case 1:
#         print("Savings Account")

#         operation = int(input("Enter operation: "))

#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case 2:
#         print("Current Account")

#         operation = int(input("Enter operation: "))

#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case _:
#         print("Invalid Account Type")

#18

# category = int(input("Enter category: "))

# match category:
#     case 1:
#         product = int(input("Enter product: "))

#         match product:
#             case 1:
#                 print("Mobile Selected")
#             case 2:
#                 print("Laptop Selected")
#             case 3:
#                 print("Headphones Selected")
#             case _:
#                 print("Invalid Product")

#     case 2:
#         product = int(input("Enter product: "))

#         match product:
#             case 1:
#                 print("Shirt Selected")
#             case 2:
#                 print("Jeans Selected")
#             case 3:
#                 print("Shoes Selected")
#             case _:
#                 print("Invalid Product")

#     case _:
#         print("Invalid Category")

#19

# category = int(input("Enter category: "))

# match category:
#     case 1:
#         food = int(input("Enter food: "))

#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid Food")

#     case 2:
#         food = int(input("Enter food: "))

#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid Food")

#     case _:
#         print("Invalid Category")

#20

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator: ")

# match operator:
#     case "+":
#         print("Result =", num1 + num2)

#     case "-":
#         print("Result =", num1 - num2)

#     case "*":
#         print("Result =", num1 * num2)

#     case "/":
#         if num2 == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Result =", num1 / num2)

#     case _:
#         print("Invalid Operator")

#21

# choice = int(input("Enter choice: "))
# temperature = float(input("Enter temperature: "))

# match choice:
#     case 1:
#         fahrenheit = (temperature * 9 / 5) + 32
#         print("Temperature =", fahrenheit, "F")

#     case 2:
#         celsius = (temperature - 32) * 5 / 9
#         print("Temperature =", celsius, "C")

#     case _:
#         print("Invalid Choice")

#22

# choice = int(input("Enter choice: "))
# value = float(input("Enter value: "))

# match choice:
#     case 1:
#         print(value * 1000, "meters")

#     case 2:
#         print(value / 1000, "kilometers")

#     case 3:
#         print(value * 1000, "grams")

#     case 4:
#         print(value / 1000, "kilograms")

#     case _:
#         print("Invalid Choice")

#23

# account = int(input("Enter account type: "))
# match account:
#     case 1:
#         print("Savings Account")
#         amount = float(input("Enter amount: "))
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")
#     case 2:
#         print("Current Account")
#         amount = float(input("Enter amount: "))
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")
#     case _:
#         print("Invalid Account Type")


#24

# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         age = int(input("Enter age: "))

#         if age >= 18:
#             print("You can start the exam")
#         else:
#             print("You cannot start the exam")

#     case 2:
#         print("Viewing Result")

#     case 3:
#         print("Exiting...")

#     case _:
#         print("Invalid Choice")

#25

# ticket = int(input("Enter ticket type: "))
# match ticket:
#     case 1:
#         ticket_type = "Regular"

#     case 2:
#         ticket_type = "Premium"

#     case 3:
#         ticket_type = "VIP"

#     case _:
#         ticket_type = "Invalid Ticket Type"

# if ticket_type == "Invalid Ticket Type":
#     print(ticket_type)
# else:
#     age = int(input("Enter age: "))

#     if age < 5:
#         print("Free Entry")
#     else:
#         print(ticket_type)

#26

# instruction = int(input("enter your number"))
# match instruction:
#     case 1:
#        print("light controll open")
#     case 2:
#        print("Fan controll open")
#     case 3:
#        print("Ac controll open")
#     case 4:
#        print("TV controll open")


#27
# depratement = int(input("enter your type"))
# match depratement:
#     case 1:
#       print("general medical")
#     case 2:
#       print("cardiology")
#     case 3:
#       print("ortopedics")
#     case 4:
#       print("pediatrics")
#     case 5:
#       print("Emergency")
#     case _:
#       print("invalid")

   
#28
# railwaymenu = int(input("enter your type"))
# match railwaymenu:
#     case 1:
#         print("book ticket")
#     case 2:
#         print("cancel ticket")
#     case 3:
#         print("check PNR")
#     case 4:
#         print("train schudul")
#     case 5:
#         print("Exit")
#     case _:
#         print(" invalid")




# 29

# choice = int(input("Enter your choice: "))
# match choice:
#     case 1:
#         print("Search Book")
#     case 2:
#         print("Issue Book")
#     case 3:
#         print("Return Book")
#     case 4:
#         print("View Issued Books")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid choice")


# 31

# bank = int(input("enter your bank 1.personalbanking , 2.businessbanking"))
# match bank:
#     case 1 :
#         a=int(input("enter your option"))
#         match a:
#             case 1:
#                 print("Personal Balance Selected")
#             case 2:
#                 print("Personal Transfer Selected")
#             case 3:
#                 print("Personal Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         b=int(input("enter your option"))
#         match b:
#             case 1:
#                 print("Business Balance Selected")
#             case 2:
#                 print("Payroll Selected")
#             case 3:
#                 print("Business Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Banking Type")



# 32
# role = int(input("enter your role 1.student , 2.teacher, 3.parent" ))
# option = int(input("enter your work"))
# match role:
#     case 1:
#         match option:
#             case 1:
#                 print("marks")
#             case 2:
#                 print("attendence")
#             case 3:
#                 print("homework")   
#     case 2:
#         match option:
#             case 1:
#                 print("Enter marks")
#             case 2:
#                 print("attendence")
#             case 3:
#                 print("asignt homework")   
#     case 3:
#         match option:
#             case 1:
#                 print("child marks")
#             case 2:
#                 print("child attendence")
#             case 3:
#                 print("childs teacher")             

# #33
# transport = int(input("Enter transport: "))
# option = int(input("Enter option: "))

# match transport:
#     case 1:
#         match option:
#             case 1:
#                 print("Flight Economy Selected")
#             case 2:
#                 print("Flight Business Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         match option:
#             case 1:
#                 print("Train Sleeper Selected")
#             case 2:
#                 print("Train AC Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         match option:
#             case 1:
#                 print("Bus Ordinary Selected")
#             case 2:
#                 print("Bus Volvo Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Transport")


# # 34
# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         print("Start Game Selected")
#     case 2:
#         print("Load Game Selected")
#     case 3:
#         print("Settings")
#         setting = int(input("Enter setting: "))

#         match setting:
#             case 1:
#                 print("Sound Settings")
#             case 2:
#                 print("Graphics Settings")
#             case 3:
#                 print("Controls Settings")
#             case _:
#                 print("Invalid Setting")

#     case 4:
#         print("Exit Selected")
#     case _:
#         print("Invalid Choice")


#35

# choice = int(input("enter you catogary 1.starter 2.maincourcs 3.desserts 4.drinks"))
# item = int(input("enter your food"))
# match choice:
#     case 1:
#         match item:
#             case 1:
#                 print("soup")
#             case 2:
#                 print("spring roll")
#             case 3:
#                 print("garlic bread")   
#     case 2:
#         match item:
#             case 1:
#                 print("Pizza")
#             case 2:
#                 print("pasta")
#             case 3:
#                 print("biryani")        

#     case 3:
#         match item:
#             case 1:
#                 print("ice cream")
#             case 2:
#                 print("cake")
#             case 3:
#                 print("gulab jambun")
#     case 4:
#         match item:
#             case 1:
#                 print("coffee")
#             case 2:
#                 print("tea")
#             case 3:
#                 print("juice")                            



#36
# payment = int(input("Enter payment type: "))
# option = int(input("Enter option: "))
# match payment:
#     case 1:
#         match option:
#             case 1:
#                 print("Scan QR Selected")
#             case 2:
#                 print("Enter UPI ID Selected")
#             case _:
#                 print("Invalid Option")
#     case 2:
#         match option:
#             case 1:
#                 print("Credit Card Selected")
#             case 2:
#                 print("Debit Card Selected")
#             case _:
#                 print("Invalid Option")
#     case 3:
#         match option:
#             case 1:
#                 print("Add Money Selected")
#             case 2:
#                 print("Pay Using Wallet Selected")
#             case _:
#                 print("Invalid Option")
#     case _:
#         print("Invalid Payment Type")


#37

# subject = int(input("Enter subject: "))
# option = int(input("Enter option: "))
# match subject:
#     case 1:
#         match option:
#             case 1:
#                 print("Python Selected")
#             case 2:
#                 print("Java Selected")
#             case 3:
#                 print("C++ Selected")
#             case _:
#                 print("Invalid Option")
#     case 2:
#         match option:
#             case 1:
#                 print("Algebra Selected")
#             case 2:
#                 print("Calculus Selected")
#             case 3:
#                 print("Statistics Selected")
#             case _:
#                 print("Invalid Option")
#     case 3:
#         match option:
#             case 1:
#                 print("English Selected")
#             case 2:
#                 print("Presentation Selected")
#             case 3:
#                 print("Interview Skills Selected")
#             case _:
#                 print("Invalid Option")
#     case _:
#         print("Invalid Subject")


# 38  

# choice = int(input("Enter choice: "))
# match choice:
#     case 1:
#         option = int(input("1 Start, 2 Stop: "))
#         match option:
#             case 1:
#                 print("Engine Started")
#             case 2:
#                 print("Engine Stopped")
#             case _:
#                 print("Invalid Option")
#     case 2:
#         option = int(input("1 Headlights, 2 Indicators, 3 Hazard Lights: "))
#         match option:
#             case 1:
#                 print("Headlights Selected")
#             case 2:
#                 print("Indicators Selected")
#             case 3:
#                 print("Hazard Lights Selected")
#             case _:
#                 print("Invalid Option")
#     case 3:
#         option = int(input("1 Play, 2 Pause, 3 Next, 4 Previous: "))
#         match option:
#             case 1:
#                 print("Music Playing")
#             case 2:
#                 print("Music Paused")
#             case 3:
#                 print("Next Song")
#             case 4:
#                 print("Previous Song")
#             case _:
#                 print("Invalid Option")
#     case 4:
#         option = int(input("1 Start Navigation, 2 Stop Navigation: "))
#         match option:
#             case 1:
#                 print("Navigation Started")
#             case 2:
#                 print("Navigation Stopped")
#             case _:
#                 print("Invalid Option")
#     case _:
#         print("Invalid Choice")


#  3
# role = int(input("Enter role: "))
# option = int(input("Enter option: "))
# match role:
#     case 1:
#         match option:
#             case 1:
#                 print("View Profile Selected")
#             case 2:
#                 days = int(input("Enter leave days: "))
#                 if days > 0:
#                     print("Leave Request Submitted")
#                 else:
#                     print("Invalid Leave Days")
#             case 3:
#                 print("View Salary Selected")
#             case _:
#                 print("Invalid Option")
#     case 2:
#         match option:
#             case 1:
#                 print("View Team Selected")
#             case 2:
#                 print("Approve Leave Selected")
#             case 3:
#                 print("View Reports Selected")
#             case _:
#                 print("Invalid Option")
#     case _:
#         print("Invalid Role")


# 40

role = int(input("Enter role: "))
option = int(input("Enter option: "))
match role:
    case 1:
        match option:
            case 1:
                print("Student Profile")
            case 2:
                print("Student Marks")
            case 3:
                print("Student Attendance")
            case 4:
                print("Student Courses")
            case _:
                print("Invalid Student Option")
    case 2:
        match option:
            case 1:
                print("Teacher Students")
            case 2:
                print("Teacher Enter Marks")
            case 3:
                print("Teacher Attendance")
            case 4:
                print("Teacher Courses")
            case _:
                print("Invalid Teacher Option")
    case 3:
        match option:
            case 1:
                print("Administration Fees")
            case 2:
                print("Administration Admissions")
            case 3:
                print("Administration Notices")
            case 4:
                print("Administration Departments")
            case _:
                print("Invalid Administration Option")
    case _:
        print("Invalid Role")








