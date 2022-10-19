s= input("What is your favourite colour:")
l=["yellow","bluue","orange","white","black","red"]
for colour in l:
    if colour in s:
        c=colour
        break
else:
    c="other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")
print()        
