print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("enter your choice")
choice=int(input())
match choice:
    case 1:
        print("enter two number")
        a,b=int(iput()),int(input())
        c=a+b
        print("sum is c")
    case 2:
        print("enter two number")
        a,b=int(iput()),int(input())
        c=a-b
        print("subtraction is c")
    case 3:
        print("enter two number")
        a,b=int(iput()),int(input())
        c=a*b
        print("Multiplication is c")
    case 2:
        print("enter two number")
        a,b=int(iput()),int(input())
        c=a/b
        print("Division is c")
    
        
