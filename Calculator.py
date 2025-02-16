import math

print("Math Calculator")

print("Choose 1 for Addition")

print("Choose 2 for Subtraction")

print("Choose 3 for Multiplication")

print("Choose 4 for Division")

print("Choose 5 for Comparing numbers")

print("Choose 6 for finding area or perimeter")

print("Choose 7 for finding powers")

print("Choose 8 for finding square roots")

print("Choose 9 for finding cube roots")

print("Choose 10 for finding any roots")

print("Choose 11 for using the pythagoras theorem")

print("Choose 12 for reading the rules for factorials")

print("Choose 13 for finding simple interest")

print("Choose 14 to find percentage")

print("Choose 15 to find diagonal of a square")

print("Choose 16 for finding logarithms")


print("Choose 17 for finding factorials")

print("Choose 18 for finding LCM")

print("Choose 19 for triogonometry")

print("Choose 20 for HCF")

print("Choose 21 for pi value")

print("Choose 22 for e value")

n = int(input("Choose a Number: "))

if (n == 1):
    print("Welcome to Addition")
    a = float(input("Enter a Number: "))
    b = float(input("Enter a Number: "))
    print("If Answer is Yes then enter 1.")
    print("If Answer is No then enter 2.")
    yes_no = int(input("Want to enter one more number? "))

    if (yes_no == 1):
        c = float(input("Enter a Number:"))

    else:
        c = 0
    print("The Sum is : ", a+b+c)

elif (n == 2):
    print("Welcome to Subtraction")
    a = float(input("Enter a Number: "))
    b = float(input("Enter a Number: "))
    print("The Difference is : ", a-b)

elif (n == 3):
    print("Welcome to Multiplication")
    a = float(input("Enter a Number: "))
    b = float(input("Enter a Number: "))
    print("If Answer is Yes then enter 1.")
    print("If Answer is No then enter 2.")
    yes_no = int(input("Want to enter one more number? "))

    if (yes_no == 1):
        c = float(input("Enter a Number:"))
        print("The Product is : ", a*b*c)

    else:
        print("The Product is : ", a*b)

elif (n == 4):
    print("Welcome to Division")
    a = float(input("Enter a number: "))
    b = float(input("Enter a Number: "))
    print("The Answer is ", a/b)

elif (n == 5):
    print("Welcome to Comparing Numbers")
    a = float(input("Enter a number: "))
    b = float(input("Enter a Number: "))

    if (a < b):
        print(a, "is smaller than", b)

    elif(a > b):
         print(a, "is bigger than", b)

    else:
         print(a, "is equal to", b)

elif (n == 6):
    print("Welcome to Perimeter and Area")
    print("Choose 1 for Perimeter")
    print("Choose 2 for Area")
    p_a = int(input("Choose : "))

    if (p_a == 1):
        print("Choose 1 for Circle")
        print("Choose 2 for Triangle")
        print("Choose 3 for Square")
        print("Choose 4 for Rectangle")
        print("Choose 5 for Parallelogram")
        shape = int(input("Choose: "))

        if (shape == 1):
            print("Welcome to find circumference of circle.")
            r = float(input("Enter radius of circle: "))
            h = math.pi
            a = 2
            print("The circumference of circle is ", a*h*r, "cm")
        
        elif (shape == 2):
            print("Welcome to find perimeter of triangle.")
            a = float(input("Enter first side: "))
            b = float(input("Enter second side: "))
            c = float(input("Enter third side: "))

            if ((a+b) > c):

                if ((b+c) > a):

                    if ((c+a) > b):
                        print("The perimeter of triangle is ", a+b+c, "cm")
                    else:
                        print("Error! The triangle with these sides cannot be formed.")
                else:
                    print("Error! The triangle with these sides cannot be formed.")
            else:
                print("Error! The triangle with these sides cannot be formed.")


        elif (shape == 3):
            print("Welcome to find perimeter of square.")
            s = float(input("Enter side of square: "))
            a = 4
            print("The perimeter of square is ", a*s, "cm")

        elif (shape == 4):
            print("Welcome to find the perimeter of Rectangle.")
            l = float(input("Enter the length: "))
            b = float(input("Enter the breadth: "))
            a = 2
            print("The perimeter of rectangle is ", a*(l + b), "cm")
        
        elif (shape == 5):
            print("Welcome to find the perimeter of parallelogram.")
            l = float(input("Enter the height: "))
            b = float(input("Enter the base: "))
            a = 2 
            print("The perimeter of rectangle is ", a*(l + b), "cm")

        else:
            print("Error! You have entered a wrong number.")

    elif (p_a == 2):

        print("Choose 1 for Circle")
        
        print("Choose 2 for Triangle")
        
        print("Choose 3 for Square")
        
        print("Choose 4 for Rectangle")
        
        print("Choose 5 for Parallelogram")
        shape = int(input("Choose: "))

        if (shape == 1):
            print("Welcome to find Area of circle.")
            r = float(input("Enter radius of circle: "))
            h = math.pi
            print("The circumference of circle is ", h*r*r, "sq. cm")
        
        elif (shape == 2):

            print("Welcome to find area of triangle.")

            a = float(input("Enter first side: "))

            b = float(input("Enter second side: "))

            c = float(input("Enter third side: "))

            if ((a+b) > c):

                if ((b+c) > a):

                    if ((c+a) > b):

                        s = (a+b+c)/2
                        print("The area of triangle is ", (s*(s-a)*(s-b)*(s-c))**0.5 ,"sq. cm")
                    else:
                        print("Error! The triangle with these sides cannot be formed.")
                else:
                    print("Error! The triangle with these sides cannot be formed.")
            else:
                print("Error! The triangle with these sides cannot be formed.")

        elif (shape == 3):
            print("Welcome to find area of square.")
            s = float(input("Enter side of square: "))
            print("The area of square is ", s**2)

        elif (shape == 4):
            print("Welcome to find the area of Rectangle.")
            l = float(input("Enter the length: "))
            b = float(input("Enter the breadth: "))
            print("The area of rectangle is ", l*b, "sq. cm")
        
        elif (shape == 5):
            print("Welcome to find the area of parallelogram.")
            l = float(input("Enter the height: "))
            b = float(input("Enter the base: "))
            print("The area of parallelogram is ", l*b, "sq. cm")

        else:
            print("Error! You have entered a wrong number.")

elif (n == 7):
    print("Welcome to find powers")
    b = float(input("Enter base: "))
    p = float(input("Enter power: "))
    print("The power is ", b**p)

elif (n == 8):
    print("Welcome to find square roots")
    b = float(input("Enter number: "))
    a = 0.5
    print("The square root is ", b**a)

elif (n == 9):

    print("Welcome to find cube roots")

    b = float(input("Enter number: "))

    a = 1/3
    print("The cube root is ", b**a)

elif (n == 10):

    print("Welcome to find any roots")

    r = float(input("Enter root: "))
    
    b = float(input("Enter number: "))
    
    a = 1
    
    print("The root is ", b**(a/r))

elif (n == 11):

    print("Welcome to use pythagoras theorem")

    a = float(input("Enter base: "))

    b = float(input("Enter perpendicular: "))

    s = 2

    c = ((a**s)+(b**s))**(1/s)

    print("The hypotenuse is ", c, "cm")

elif (n == 12):

    print("Welcome to read rules about factorials")
    
    print("The factorial is denoted by the sign !")
    
    print("To find a factorial follow the rules:")
    
    print("Take that we have to find n!.  [n is a whole number.]")
    
    print("[n is a whole number.]")
    
    print("n! = n(n-1)(n-2)....(n-a)")
    
    print("(n-a) = 1")
    
    print("Take that we have to find 5!.  [5 is a whole number.]")
    
    print("[5 is a whole number.]")
    
    print("5! = 5(5-1)(5-2)....(5-a)  [a = 4 in this case because 5 - 4 = 1]")
    
    print("[a = 4 in this case because 5 - 4 = 1]")
    
    print("(5-4) = 1")
    
    print("5! = 5 x 4 x 3 x 2 x 1")
    
    print("5! = 120")
    
    print("All done !")


elif (n == 13):

    print("Welcome to find simple interest")

    p = float(input("Enter Principal Ammount: "))

    t = float(input("Enter time in years: "))

    r = float(input("Enter rate in % : "))

    print("The interest is", (p*r*t)/100)

elif (n == 14):

    print("Welcome to find percentage")

    print("Choose 1 for finding with fractions")

    print("Choose 2 for finding with decimals")

    print("Choose 3 for finding percentage of your marks")

    co = int(input("Enter: "))

    if (co == 1):

        a = float(input("Enter numerator: "))

        b = float(input("Enter denominator: "))

        c = a/b

        print("The percentage is ", c*100, "%")

    elif (co == 2):

        a = float(input("Enter decimal: "))

        print("The percentage is ", a*100, "%")

    elif (co == 3):

        a = float(input("Enter marks you got: "))
        
        b = float(input("Enter marks the paper was: "))
        
        print("Your percentage are ", (a/b)*100, "%")

    else:
        print("Error! you have entered wrong number.")

elif (n == 15):

    print("Welcome to finding a diagonal of a square")
    
    a = float(input("Enter side of square: "))
    
    print("The diagonal is ", ((a**2)+(a**2))**0.5, "cm")

elif (n == 16):

    print("Welcome to find logarithms")
    
    print("Choose 1 for finding logrithm with base 2")
    
    print("Choose 2 for finding logrithm with base 10")
    
    print("Choose 3 for finding logarithms with base e")
    
    al = int(input("Choose: "))
    
    if (al == 1):
    
        a = float(input("Enter number: "))
    
        print("The Answer is ", math.log2(a))
    
    elif (al == 2):

        a = float(input("Enter number: "))
        
        print("The Answer is ", math.log10(a))

    elif (al == 3):

        
        a = float(input("Enter number: "))
        
        print("The Answer is ", math.log(a))

    else:

        print("Error! You have entered a wrong number.")

elif (n == 17):

    
    print("Welcome to find factorials")
    
    a = int(input("Enter a number: "))
    
    print("The factorial is ", math.factorial(a))

elif (n == 18):
    
    print("Welcome to find lcm")
    
    print("Note: Please enter an integer")
    
    a = int(input("Enter Number: "))
    
    b = int(input("Enter Number: "))
    
    c = int(input("Enter Number: "))
    
    d = int(input("Enter Number: "))
    
    print("Want to choose more numbers?")
    
    print("Choose 1 for Yes")
    
    print("Choose 2 for No")
    
    ali = int(input("Choose: "))
    
    if (ali == 1):
    
        e = int(input("Enter number else 1: "))
    
        f = int(input("Enter number else 1: "))
    
        g = int(input("Enter number else 1: "))
    
    else:
        
        e = 1
        
        f = 1
        
        g = 1

    print("The LCM is ", math.lcm(a, b, c, d))

elif (n == 19):

    print("Welcome to triogonometry")

    print("Choose 1 for sine")

    print("Choose 2 for cosine")

    print("Choose 3 for tangent")

    ali = int(input("Choose: "))
    
    if (ali == 1):
    
        a = float(input("Enter number: "))
    
        print("The sine is ", math.sin(a))

    elif (ali == 2):
       
        a = float(input("Enter number: "))
       
        print("The cosine is ", math.cos(a))

    elif (ali == 3):
       
        a = float(input("Enter number: "))
       
        print("The tangent is ", math.tan(a))

    else:
        print("Error! You have entered a wrong number")

elif (n == 20):

    
    print("Welcome to find HCF")
    
    print("If you want to enter less than 4 numbers then enter 1 in blanks.")
    
    a = int(input("Enter number else 1: "))
    
    b = int(input("Enter number else 1: "))
    
    c = int(input("Enter number else 1: "))
    
    d = int(input("Enter number else 1: "))
    
    print("Want to choose more numbers?")
    
    print("Choose 1 for Yes")
    
    print("Choose 2 for No")
    
    ali = int(input("Choose: "))

    if (ali == 1):

        e = int(input("Enter number else 1: "))
        
        f = int(input("Enter number else 1: "))
        
        g = int(input("Enter number else 1: "))
    
    else:

        e = 1
        f = 1
        g = 1
    
    print("The HCF is ", math.gcd(a, b, c, d, e, f, g))


elif (n == 21):

    print("Welcome to find value of pi")

    print("The symbol of pi is")

    print("π")

    print("The value of π is")

    print(math.pi)

elif (n == 22):

    print("Welcome to find th value of e")

    print("The value of e is:")

    print(math.e)

elif (n == 23):

    print("Welcome to find remainder")

    a = float(input("Enter Dividend: "))

    b = float(input("Enter Divisor: "))

    print("The remainder is ", math.fmod(a,b))

else:

    print("Error! You have Entered a wrong number.")

print("Thank You for visiting us")

print("Made by Samar Singh")

print("All rights reserved ® 2025.")

print("Exiting............")