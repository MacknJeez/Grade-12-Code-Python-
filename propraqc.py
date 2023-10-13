def isEmpty(stk):
    if(len(stk)==0):
        return 'True'
    else:
        return 'False'

def Push(stk):
    item = input("Enter item to add: ")
    stk.append(item)
    top = stk[len(stk)-1]

def Pop(stk):
    if(isEmpty(stk)=='True'):
        print("Stack is Empty")
    else:
        print("Item being removed is: ",stk[len(stk)-1])
        stk.pop()
        top = stk[len(stk)-1]

def Display(stk):
    if(isEmpty(stk)=='True'):
        print("Stack is Empty")
    else:
        for i in stk:
            print(i)
        print("Top is: ",stk[len(stk)-1])

#main

stk = []

while true:
    print("Main Menu")
    print("1.ADD")
    print("2.Delete")
    print("3.Display")
    print("4.Exit")
    ch = input("Enter a choice: ")
    if(ch==1):
        Push(stk)
        Display(stk)
    elif(ch==2):
        Pop(stk)
        Display(stk)
    elif(ch==3):
        Display(stk)
    elif(ch==4):
        print("Thank YOU")
        break
    else:
        print("Enter correct choice")
    
