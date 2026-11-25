# str=input=("emter your str:").strip()
# length=len(str)
# for element in range(length-1 ,0 ,-1):
#     print (str(element) 
    






str=input("enter  youu string:").strip()
str2=""
length=len(str)
for element in range(length-1,-1,-1):
    str2=str2+str[element]
    print(str[element])

    if str2==str:
        print("paladrom")

    else:
        print("non paladrom")
                








# str=input("Enter a string :").strip().lower()
# str2=""
# length=len(str)
# for i in range(length-1,-1,-1):
#     print(str[i])
#     str2=str2+str[i]