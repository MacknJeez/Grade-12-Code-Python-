a=[]
c='y'
while c=='y':
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    n=int(input("Enter choice:"))
    if n==1:
        b=input("Enter element:")
        a.append(b)
    elif n==2:
        if a==[]:
            print("Stack empty:")
        else:
            print("Deleted element is:",a.pop())
    elif n==3:
        l=len(a)
        while l>0:
            print (a[l-1])
            l=l-1
    else:
        print("Wrong input")
    c=input("Do you want to continue?[y/n]")
