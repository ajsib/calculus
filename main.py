import math

def f(x):
    cube = x ** 3
    square = x ** 2
    sqrt = x ** 1/2
    cbrt = x ** 1/3
    e = 2.71828
  #  ln = math.log(x)
   # log10 = math.log(x, 10)
    pi = 3.1415926535
    sine = math.sin(x)
    cosine = math.cos(x)
    tangent = (sine / cosine)
    csc = 1 / sine
    sec = 1 / cosine
    cot = (cosine/sine)
    # ----------------------------
    global g
    # Input Function Here
    #-----------------------------
    g = 2 ** (- x ** 2)
    #-----------------------------
    return g


def derviative(x):
    h = 0.000001
    numerator = f(x + h) - f(x)
    denominator = h
    global m
    m = numerator / denominator
#--------------------------------------------
    split_m = str(m).split('.')
    int_m = int(split_m[0])
    dec_m = float('0.' + split_m[1])
    if dec_m < 0.0000001 or dec_m < 0.9999999:
        m = round(m, 2)
    elif dec_m < 0.1 or dec_m < 0.9:
        m = round(m, 3)
    if m == 0:
        print("-------Slope--of--Tangent------")
        print( "\033[91m\033[1m" + "-Max/Min/Vertex-located-at-(x)-" + "\033[0m")
    elif m != 0:
        print("\n")
        print("-------Slope--of--Tangent------")
    print(m)
def slope(x):
    y = g
    if 0.99999999999999999 > y > -0.99999999999999999:
        print("--------Value--of--f(x)--------")
        print(y)
    else:
        split_y = str(y).split('.')
        int_y = int(split_y[0])
        dec_y = float('0.' + split_y[1])
        if dec_y < 0.000000001 or dec_y < 0.99999999999:
            y = round(y, 3)
        elif dec_y < 0.1 or dec_y < 0.9:
            y = round(y, 2)
        print("--------Value--of--f(x)--------")
        print(y)

    b = y - (m * x)
    print("----------y intercept----------")
    if 0.9999999999999999 > b > -0.99999999999999999:
        print(b)
    else:
        split_b = str(b).split('.')
        int_b = int(split_b[0])
        dec_b = float('0.' + split_b[1])
        if dec_b < 0.00000001 or dec_b < 0.99999999999:
            b = round(b, 3)
        elif dec_b < 0.01 or dec_b < 0.9:
            b = round(b, 2)
        print(b)
    print("-----Equation--of--Tangent-----")
    if b < 0:
          print(("y = "),(m),("x"),(b))
    elif b >= 0:
        print(("y = "),(m),("x +"),(b))
    print("-------------------------------")
    print("\n\n\n")

def integral(lbx, ubx):
    dx = 1000000
    width = (float(ubx) - float(lbx)) / dx
    sum = 0
    for i in range(dx):
        height = f(lbx + i * width)
        area = height * width
        sum += area
    split_sum = str(sum).split('.')
    int_sum = int(split_sum[0])
    dec_sum = float('0.' + split_sum[1])
    if dec_sum < 0.00000001 or dec_sum < 0.99999999999:
        sum = round(sum, 3)
    elif dec_sum < 0.01 or dec_sum < 0.9:
        sum = round(sum, 2)
    print("\n---Area--Under--f(x)---")
    print(sum)
    print("-----------------------")


    return sum

#main
exit = 1
while exit == 1:
    print("Would You Like to " + "\033[1m" + "Differentiate" + "\033[0m" + " or " + "\033[1m" + "Integrate?" +"\033[0m")
    print("For Differentiation Enter" "\033[91m"+ " 'd' " + "\033[0m")
    print("for Integration Enter" "\033[91m"+ " 'i' " + "\033[0m")
    task = input("-------Input--Here------>")
    task = task.lower()
    if task == "d":
        x = float(input("\033[92m\033[1m" + "Enter (x) Value to Evaluate: " + "\033[0m"))
        if x != 0:
            derviative(x)
            slope(x)
        else:
            print("to find dy/dx @ x = 0 , ")
            print("let x = lim ")
            print("        x-->0")
            print("\n")
            print("Ex: x = 0.001")
            print("If 'slope' ??? true value, round to limiting decimal")
            print("\n\n\n")

    elif task == "i":
        print("\n")
        lbx = float(input("\033[92m\033[1m" + "Enter Lower Bound" + "\033[0m"))
        if lbx != 0:
            ubx = float(input("\033[92m\033[1m" + "Enter Upper Bound" + "\033[0m"))
            integral(lbx, ubx)
            print("\n\n\n")
        else:
            print("to set lower bound @ 0, ")
            print("Let 0 = 0.0001 ")
            print("\n\n")

    elif task == "e":
        exit = 0

    else:
        print("Enter 'd' to Differentiate")
        print("Enter 'i' to Integrate")
        print("Enter 'e' to Exit")



