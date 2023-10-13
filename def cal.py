def SUM(x,y):
    s=int(x)+int(y)
    return s

def PRO(x,y):
    p=int(x)*int(y)
    return p

def DIF(x,y):
    d=int(x)-int(y)
    return d
def QUO(x,y):
    q=int(x)/int(y)
    return q
a=0
x=0
y=0
while a!="#":
    y=(raw_input("enter first number here"))
    x=(raw_input("enter second number here"))
    a=raw_input("enter '+' for addition, '-' for subtraction,'*'for multiplication , / for division or # to stop")
    if a=="#":
        break
    
    elif a=="+":
        print SUM(x,y)
        
    elif a=="*":
        print PRO(x,y)
        
    elif a=="-":
        print DIF(x,y)
        
    elif a=="/":
        print QUO(x,y)
    else:
        print"error"
