def area():
    while True:
        askShape = int(input('Enter choice [1 = Triangle, 2 = Rectangle, 3 = Circle, 4 = Quit]:'))
        if askShape == 1:
            b = float(input('Enter Base length of triangle:'))
            h = float(input('Enter height of triangle:'))
            print('Area of Triangle =', 0.5 * b * h)
        elif askShape == 2:
            b = float(input('Enter Base of Rectangle:'))
            l = float(input('Enter Length of Rectangle:'))
            print('Area of Rectangle =', l * b)
        elif askShape == 3:
            r = float(input('Enter Radius:'))
            print('Area of Circle =', 3.14 * (r ** 2))
        elif askShape == 4:
            print('Exited Loop')
            break


def factor(numb):
    list_val = []
    for i in range(numb):
        if numb % i == 0:
            list_val.append(i)
    print('The factors of the number', numb, 'are:')
    for i in list_val:
        print(i)


def arms(val):
    valSum = 0
    for i in str(val):
        valSum += (int(i) ** 3)
    if valSum == val:
        print('Input is an Armstrong Number')
    else:
        print('Not an Armstrong number')


def prime(lower, upper):
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
        else:
            print('Enter lower limit greater than 1')


def shift():
    list_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list_val2 = []
    for i in range(len(list_val), 0, -1):
        list_val2.append(list_val[i - 1])
    print(list_val2)
