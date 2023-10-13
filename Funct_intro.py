import time
def waiting():
    for i in "Calculating":
        print i,
        time.sleep(0.5)
        
def add():
    a = float(raw_input("Enter First number:"))
    b = float(raw_input("Enter second nuber"))
    s= a+b
    waiting()
    print "Answer:",s
def mult():
    a = float(raw_input("Enter First number:"))
    b = float(raw_input("Enter second nuber"))
    m=a*b
    waiting()
    print "Answer:", m
def sub():
    a = float(raw_input("Enter First number:"))
    b = float(raw_input("Enter second nuber"))
    waiting()
    print "Answer:", sub
def div():
    a = float(raw_input("Enter First number:"))
    b = float(raw_input("Enter second nuber"))
    d=a/b
    waiting()
    print "Answer:", d



while True:
    ask=raw_input(''' cAlCuLaToR
    Addition(+)
    Subtraction(-)
    Division(/)
    Multiplication(*)
    Exit(.):''')
    if ask == "+":
        add()
    elif ask == "-":
        sub()
    elif ask == "/":
        div()
    elif ask== "*":
        mult()
    elif ask==".":
        break
    else:
        print "Invalid"
    print
    print
    print


