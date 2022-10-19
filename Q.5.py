n=int(input("enter a number: "))
match n:
    case n if n%2==0:
        print("Saurabh shukla")
    case n if n<0 and n%2:
        print("Prateek Jain")
    case n if n>0 and n%2:
        print("Aditya Choudhary")
        
    
