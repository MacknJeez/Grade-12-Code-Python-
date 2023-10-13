# Importing Modules here
import tkinter
import math
import derivatives


# Main functions :-
def quad():
    guiq = tkinter.Tk()
    guiq.Title = "Quadratic Equation solver"
    guiq.geometry('200x250')
    l1 = tkinter.Label(guiq, text="Enter coefficent of x^2")
    l1.pack()
    t1 = tkinter.Entry(guiq)
    t1.pack()
    #
    l2 = tkinter.Label(guiq, text="Enter coefficent of x")
    l2.pack()
    t2 = tkinter.Entry(guiq)
    t2.pack()
    #
    l3 = tkinter.Label(guiq, text="Enter constant")
    l3.pack()
    t3 = tkinter.Entry(guiq)
    t3.pack()
    #
    t4 = tkinter.Entry(guiq, text="SOLUTION WILL COME HERE :)")
    t4.pack()

    def getquad():
        if len(t1.get()) > 0 and len(t2.get()) > 0 and len(t3.get()) > 0:
            a = float(str(t1.get()))
            b = float(str(t2.get()))
            c = float(str(t3.get()))
            d = b ** 2 - 4 * a * c
            if d > 0:
                x = (-b + (d ** 0.5)) / (2 * a)
                y = (-b - (d ** 0.5)) / (2 * a)
                t4.delete(0, 999)
                t4.insert(0, ("The solutions:", x, "or", y, "."))
            else:
                if d == 0:
                    z = (-b) / 2 * a
                    t4.delete(0, 999)
                    t4.insert(0, ("There exist one solution that is", z, "."))
                else:
                    t4.delete(0, 999)
                    t4.insert(0, "There are no solutions")

    b1 = tkinter.Button(guiq, text="Get Solutions", command=getquad)
    b1.pack()


def prime():
    pgui = tkinter.Tk()
    pgui.Title = "Prime Number checker"
    l1 = tkinter.Label(pgui, text="Enter positive integer:")
    l1.pack()
    t1 = tkinter.Entry(pgui)
    t1.pack()

    def checkprime():
        if len(t1.get()) > 0:
            n = int(str(t1.get()))
            i = 2
            flag = 1
            while flag == 1 and (i < n):
                if n % i == 0:
                    flag = 0
                    break
                flag = 1
                i = i + 1
            t1.delete(0, 999)
            if flag == 0:
                t1.insert(0, (n, "is not prime"))
            if flag == 1:
                t1.insert(0, (n, "is prime"))

    b1 = tkinter.Button(pgui, text="Check if prime", command=checkprime)
    b1.pack()


def getlog():
    guilog = tkinter.Tk()
    l1 = tkinter.Label(guilog, text="Enter Value:")
    l1.pack()
    t1 = tkinter.Entry(guilog)
    t1.pack()

    def tolog():
        if len(t1.get()) > 0:
            x = float(str(t1.get()))
            t1.delete(0, 999)
            t1.insert(0, math.log10(x))

    b1 = tkinter.Button(guilog, text="Get Log", command=tolog)
    b1.pack()


def guifact():
    fact = tkinter.Tk()
    fact.title("Factorial value: ")
    label1 = tkinter.Label(fact, text="Enter which factorial value you want:")
    label1.pack()
    text1 = tkinter.Entry(fact)
    text1.pack()

    def getfact():
        if len(text1.get()) > 0:
            n = int(str(text1.get()))
            f = 1
            for i in range(1, n + 1):
                f = f * i
            text1.delete(0, 99999999)
            text1.insert(0, f)

    button1 = tkinter.Button(fact, text="Get factorial", command=getfact)
    button1.pack()


def exponent():
    print("\n--------------------------------------------------------")
    print("             [EXPONENT CALCULATOR]                    ")
    q = input("\nDo you want to get exponent value or root value?[E/R]: ")
    if q == "E":
        x = int(input("Enter number: "))
        e = int(input("Enter power: "))
        print(x, "raised to", e, "=", x ** e)
    if q == "R":
        x = int(input("Enter number: "))
        e = int(input("Enter root: "))
        print(x, "to the root of", e, "=", x ** (1 / float(e)))


def largest():
    print("\n--------------------------------------------------------")
    print("                  [LARGEST OF N NUMBERS]                  ")
    l = 0
    n = int(input("\nEnter Number of Numbers: "))
    print("Enter Numbers:")
    for i in range(n):
        q = int(input())
        if q > l:
            l = q
    print("Largest Number is", l)


def deriv():
    guide = tkinter.Tk()
    guide.text = "Derivative"
    l1 = tkinter.Label(guide, text="Enter equation:")
    l1.pack()
    t1 = tkinter.Entry(guide)
    t1.pack()

    def getderiv():
        y = str(t1.get())
        print(y)
        t1.delete(0, 999)
        t1.insert(0, derivatives.differentiate(y))

    derive = tkinter.Button(guide, text="Differentiate Equation", command=getderiv)
    derive.pack()


def trigo():
    guitrig = tkinter.Tk()
    guitrig.text = "Trigonometric Conversion"
    l1 = tkinter.Label(guitrig, text="Enter angle value in degrees:")
    l1.pack()
    t1 = tkinter.Entry(guitrig)
    t1.pack()

    def getsin():
        if len(t1.get()) > 0:
            x = float(str(t1.get()))
            t1.delete(0)
            t1.insert(0, math.sin(x * math.pi / 180))

    def getcos():
        if len(t1.get()) > 0:
            x = float(str(t1.get()))
            y = x * math.pi / 180
            t1.delete(0)
            t1.insert(0, math.cos(y))

    def gettan():
        if len(t1.get()) > 0:
            x = float(str(t1.get()))
            y = x * math.pi / 180
            t1.delete(0)
            t1.insert(0, math.tan(y))

    def getcosec():
        if len(t1.get()) > 0:
            x = float(str(t1.get()))
            y = x * math.pi / 180
            t1.delete(0)
            t1.insert(0, 1 / math.sin(y))

    def getsec():
        if len(t1.get()) > 0:
            x = float(str(t1.get()))
            y = x * math.pi / 180
            t1.delete(0)
            t1.insert(0, 1 / math.cos(y))

    def getcot():
        if len(t1.get()) > 0:
            x = float(str(t1.get()))
            y = x * math.pi / 180
            t1.delete(0)
            t1.insert(0, 1 / math.tan(y))

    Sin = tkinter.Button(guitrig, text="sin value", command=getsin)
    Sin.pack()
    Cos = tkinter.Button(guitrig, text="cos value", command=getcos)
    Cos.pack()
    Tan = tkinter.Button(guitrig, text="tan value", command=gettan)
    Tan.pack()
    cosec = tkinter.Button(guitrig, text="cosec value", command=getcosec)
    cosec.pack()
    sec = tkinter.Button(guitrig, text="sec value", command=getsec)
    sec.pack()
    cot = tkinter.Button(guitrig, text="cot value", command=getcot)
    cot.pack()


def le():
    guile = tkinter.Tk()
    guile.Title = "Linear equation solver"

    l1 = tkinter.Label(guile, text="Enter coefficent of variable:")
    l1.pack()
    t1 = tkinter.Entry(guile)
    t1.pack()

    l2 = tkinter.Label(guile, text="Enter operation value of equation:")
    l2.pack()
    t2 = tkinter.Entry(guile)
    t2.pack()

    l3 = tkinter.Label(guile, text="Enter RHS of equation:")
    l3.pack()
    t3 = tkinter.Entry(guile)
    t3.pack()

    t4 = tkinter.Entry(guile)
    t4.insert(0, "Solution=")
    t4.pack()

    def getx():
        if len(t1.get()) > 0 and len(t2.get()) > 0 and len(t3.get()) > 0:
            a = int(str(t1.get()))
            b = int(str(t2.get()))
            c = int(str(t2.get()))

            if len(t4.get()) > 9:
                t4.delete(0, 999)
                t4.insert(0, "Solution=")
            t4.insert(9, (c - b) / a)

    b1 = tkinter.Button(guile, text="Get x", command=getx)
    b1.pack()


def le2():
    # Get both EQUATIONS
    # check solutions for equations infinite, solutions, no solutions
    # use cr
    print("\n--------------------------------------------------------")
    print("          [LINEAR EQUATION IN 2 VARIABLES SOLVER]         ")
    print("##########################################################")
    print("       Following is for equations of form ax+by+c=0       ")
    print("##########################################################")
    print("\nEquation 1 Values:- ")
    a1 = int(input("\nEnter coefficient a1 of variable(x) (with +,-): "))
    b1 = int(input("Enter coefficient b1 of variable(y) (with +,-): "))
    c1 = int(input("Enter c1 of equation 1 (with +,-): "))
    print("\nEquation 2 Value:- ")
    a2 = int(input("\nEnter coefficient a2 of variable(x) (with +,-): "))
    b2 = int(input("Enter coefficient b2 of variable(y) (with +,-): "))
    c2 = int(input("Enter c2 of equation 2 (with +,-): "))
    print("\nEquation 1 is:-", a1, "(x)", "+", b1, "(y) +", c1, "= 0")
    print("\nEquation 2 is:-", a2, "(x)", "+", b2, "(y) +", c2, "= 0")

    if (a1 / a2 == b1 / b2) and (a1 / a2 != c1 / c2) and (b1 / b2 != c1 / c2):
        print("\nNO SOLUTION")
    if a1 / a2 != b1 / b2:
        print("\nDefinite Solutions: -")
        print("Variable x =", (b1 * c2 - (b2 * c1)) / (float(a1) * float(b2) - (a2 * b1)))
        print("Variable y =", (c1 * a2 - (c2 * a1)) / (float(a1) * float(b2) - (a2 * b1)))
    if a1 / a2 == b1 / b2 == c1 / c2:
        print("\nThere exists infinite solutions!")


def aandp():
    print("\n--------------------------------------------------------")
    print("              [MENSURATION CALCULATOR]             ")
    q1 = input("Enter type of shape [2D/3D]: ")
    if q1 == "2D":
        d2()
    if q1 == "3D":
        d3()


def d2():
    q2 = input("""Which 2D shape do you want area and perimeter
 1.Square
 2.Rectangle
 3.Circle
 4.Parallelogram
 5.Triangle
 6.Trapezoid
 7.Rhombus
  """)
    if q2 == "1":
        s = float(input("\nEnter side: "))
        print("Area and perimeter of the square is", s * s, "cm^2 and", 4 * s, "cm.")
    if q2 == "2":
        a = float(input("\nEnter side a: "))
        b = float(input("Enter side b: "))
        print("Area and perimeter of the Rectangle is", a * b, "cm^2 and", 2 * (a + b), "cm.")
    if q2 == "3":
        r = float(input("\nEnter radius: "))
        print("Area and perimeter of the Circle is", math.pi * r * r, "cm^2 and", 2 * math.pi * r, "cm.")
    if q2 == "4":
        a = float(input("\nEnter altitude: "))
        b = float(input("Enter side b: "))
        print("Area and perimeter of the Parallelogram is", a * b, "cm^2 and", 2 * (a + b), "cm.")
    if q2 == "5":
        q = input("Area or perimeter?[A/P]")
        if q == "A":
            a = float(input("\nEnter altitude: "))
            b = float(input("Enter base: "))
            print("Area of the Triangle is", 1 / 2 * a * b, "cm^2.")
        if q == "P":
            a = float(input("\nEnter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))
            print("Perimeter of the Triangle is", a + b + c, "cm.")
    if q2 == "6":
        a = float(input("\nEnter base a: "))
        b = float(input("Enter base b: "))
        d = float(input("Enter slant height 1: "))
        e = float(input("Enter slant height 2: "))
        c = float(input("Enter altitude:"))
        print("Area and Perimeter of the Trapezoid is", (a + b) / 2 * c, "cm^2 and", a + b + d + e, "cm.")
    if q2 == "7":
        s = float(input("\nEnter side s: "))
        a = float(input("Enter diagonal a: "))
        b = float(input("Enter diagonal b: "))
        print("Area and Perimeter of the Trapezoid is", a * b / 2, "cm^2 and", 4 * a, "cm.")


def d3():
    q3 = input("""Which 3D shape do you want Volume, Total Surface area, Curved / Lateral Surface area and Base area of?
 1.Cube
 2.Cuboid
 3.Sphere
 4.Cone
 5.Triangular Pyramid
 6.Square Pyramid
 7.Cylinder
  """)
    if q3 == 1:
        a = float(input("\nEnter side: "))
        print("Total Surface area =", 6 * a * a)
        print("Lateral Surface area =", 4 * a * a)
        print("Base area =", a * a)
        print("Volume =", a ** 3)
    if q3 == 2:
        l = float(input("\nEnter side l: "))
        b = float(input("Enter side b: "))
        h = float(input("Enter side h: "))
        print("Total Surface area =", 2 * (l * b + b * h + h * l))
        print("Lateral Surface area =", 2 * (l * h + b * h))
        print("Base area=", l * b)
        print("Volume=", l * b * h)
    if q3 == 3:
        r = float(input("\nEnter Radius: "))
        print("Curved Surface area =", 4 * math.pi * r * r)
        print("Volume=", (4 / 3) * math.pi * (r ** 3))
    if q3 == 4:
        r = float(input("\nEnter Radius: "))
        h = float(input("Enter Height"))
        print("Volume =", (1 / 3) * (math.pi * (r ** 2) * h))
        print("Total Surface Area =", (math.pi * (r ** 2)) + math.pi * r * h)
        print("Curved/Lateral Surface Area =", math.pi * r * h)
        print("Base Area =", math.pi * (r ** 2))
    if q3 == 5:
        h = float(input("\nEnter Height: "))
        hb = float(input("Enter Height of Base"))
        b = float(input("Enter Length of base: "))
        a = float(input("Enter Altitude from the base: "))
        print("Volume =", (1 / 6) * b * a * h)
        print("Total Surface Area =", 0.5 * (hb * b) + 1.5 * (b * a))
        print("Base Area=", 0.5 * (hb * b))
    if q3 == 6:
        a = float(input("\nEnter Base Edge length:"))
        h = float(input('Enter Height of pyramid:'))
        print('Volume =', (a ** 2) * (h / 3))
        print('Total Surface Area =', (a ** 2) + ((2 * a) * ((((a ** 2) / 4) + (h ** 2)) ** 0.5)))
        print('Lateral Surface =', a * (((a ** 2) + 4 * (h ** 2)) ** 0.5))
        print('Base =', a ** 2)
    if q3 == 7:
        r = float(input('\nEnter Radius:'))
        h = float(input('Enter Height:'))
        print('Volume =', math.pi * (r ** 2) * h)
        print('Total Surface Area =', (2 * math.pi * r * h) + (2 * math.pi * (r ** 2)))
        print('Lateral Surface Area =', 2 * math.pi * r * h)
        print('Base Area =', math.pi * (r ** 2))


def calculator():
    class Calculator:
        calc_value = 0.0
        div_trigger = False
        mult_trigger = False
        add_trigger = False
        sub_trigger = False

        def button_press(self, value):

            entry_val = self.number_entry.get()
            entry_val += value
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, entry_val)

        def isfloat(self, str_val):
            try:
                float(str_val)
                return True
            except ValueError:
                return False

        def math_button_press(self, value):

            if self.isfloat(str(self.number_entry.get())):

                self.add_trigger = False
                self.sub_trigger = False
                self.mult_trigger = False
                self.div_trigger = False

                self.calc_value = float(self.entry_value.get())

                if value == "/":
                    print("/ Pressed")
                    self.div_trigger = True
                elif value == "*":
                    print("* Pressed")
                    self.mult_trigger = True
                elif value == "+":
                    print("+ Pressed")
                    self.add_trigger = True
                else:
                    print("- Pressed")
                    self.sub_trigger = True

                self.number_entry.delete(0, "end")

        def equal_button_press(self):

            # Make sure a math button was clicked
            if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:

                if self.add_trigger:
                    solution = self.calc_value + float(self.entry_value.get())
                elif self.sub_trigger:
                    solution = self.calc_value - float(self.entry_value.get())
                elif self.mult_trigger:
                    solution = self.calc_value * float(self.entry_value.get())
                else:
                    solution = self.calc_value / float(self.entry_value.get())

                print(self.calc_value, " ", float(self.entry_value.get()),
                      " ", solution)

                # Clear the entry box
                self.number_entry.delete(0, "end")

                self.number_entry.insert(0, solution)

        def __init__(self, root):

            self.entry_value = tkinter.StringVar(root, value="")

            root.title("Calculator")

            root.geometry("295x125")

            root.resizable(width=False, height=False)

            self.number_entry = tkinter.Entry(root, textvariable=self.entry_value, width=50)
            self.number_entry.grid(row=0, columnspan=4)

            self.button7 = tkinter.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)

            self.button8 = tkinter.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)

            self.button9 = tkinter.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)

            self.button_div = tkinter.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1,
                                                                                                               column=3)

            self.button4 = tkinter.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)

            self.button5 = tkinter.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)

            self.button6 = tkinter.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)

            self.button_mult = tkinter.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2,
                                                                                                                column=3)

            self.button1 = tkinter.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)

            self.button2 = tkinter.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)

            self.button3 = tkinter.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)

            self.button_add = tkinter.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3,
                                                                                                               column=3)

            self.button_clear = tkinter.Button(root, text="AC", command=lambda: self.button_press('AC')).grid(row=4,
                                                                                                              column=0)

            self.button0 = tkinter.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)

            self.button_equal = tkinter.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4,
                                                                                                               column=2)

            self.button_sub = tkinter.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4,
                                                                                                               column=3)

    root = tkinter.Tk()

    calc = Calculator(root)

    root.mainloop()


def gui():
    root = tkinter.Tk()
    root.title("Calculator")

    # functions

    # Gui
    label1 = tkinter.Label(root, text="Which calculator do you want?:")
    label1.pack()

    btn1 = tkinter.Button(root, text="Basic Calculator", command=calculator)
    btn1.pack()

    btn2 = tkinter.Button(root, text="Quadratic equation solver", command=quad)
    btn2.pack()

    btn3 = tkinter.Button(root, text="Prime Number checker", command=prime)
    btn3.pack()

    btn4 = tkinter.Button(root, text="Logarithm Converter", command=getlog)
    btn4.pack()

    btn5 = tkinter.Button(root, text="Factorial value", command=guifact)
    btn5.pack()

    btn6 = tkinter.Button(root, text="Exponent Value", command=exponent)
    btn6.pack()

    btn7 = tkinter.Button(root, text="Trignometric Conversion", command=trigo)
    btn7.pack()

    btn8 = tkinter.Button(root, text="Linear equations", command=le)
    btn8.pack()

    btn9 = tkinter.Button(root, text="Linear Equations in 2 variables", command=le2)
    btn9.pack()

    btn10 = tkinter.Button(root, text="Mensuration Calculator", command=aandp)
    btn10.pack()

    btn11 = tkinter.Button(root, text="Largest of N numbers", command=largest)
    btn11.pack()

    btn12 = tkinter.Button(root, text="Derivatives", command=deriv)
    btn12.pack()

    root.mainloop()


# void main
gui()
