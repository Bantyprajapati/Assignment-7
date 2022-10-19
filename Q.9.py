s1=input("Enter a string: ")
s2=input("Enter a string: ")

match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical strings")
    case (s1,s2) if s1>s2:
        print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} comes after {}".format(s1,s2))
