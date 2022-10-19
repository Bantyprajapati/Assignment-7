age=int(input("enter user age: "))
match age:
    case age if age<10:
        print("kid")
    case age if age<20:
        print("Teen")
    case age if age<40:
        print("young")
    case age if age<60:
        print("Exprienced")
    case age if age>=60:
        print("Senior Citizen")
print()    
        
