"""
Linear Regression Calculator
Creator: Paul Norton

Built for Python 3

"""


import math
from turtle import Turtle

# Define a class to perform operations on a set of points
class LinearRegression():
    # Initialize the object
    def __init__(self, points):
        # Create lists of all x and y values
        self.x = []
        self.y = []
        for i in points:
            self.x.append(i[0])
            self.y.append(i[1])

        # Perform linear regression and calculate the correlation coefficient
        self.lin_reg()
        self.calc_cor_coef()

    # Estimate a line based on the set of points
    def lin_reg(self):
        x = self.x
        y = self.y

        # Calculate the average x and y values
        avgx = sum(x)/len(x)
        avgy = sum(y)/len(y)

        # Numerator
        bnum = 0
        for i in range(len(x)):
            bnum += x[i] * y[i]
        bnum -= len(x) * avgx *avgy

        # Denominator
        bdem = 0
        for i in x:
            bdem += i**2
        bdem -= len(x) * avgx**2

        # Prevent division by zero error
        if bdem != 0:
            # Calculate the slope and the y-intercept
            self.slope = bnum/bdem
            self.yint = avgy - self.slope*avgx
            self.isVertical = False
        else:
            # If the line is vertical, calculate the x-intercept
            self.isVertical = True
            self.xint = x[0]

    # Calculate the accuracy of the estimated line
    def calc_cor_coef(self):
        x = self.x
        y = self.y

        # Numerator
        rnum = 0
        for i in range(len(x)):
            rnum += x[i] * y[i]
        rnum *= len(x)
        rnum -= sum(x)*sum(y)

        # Denominator
        rdemx = 0
        for i in x:
            rdemx += i**2
        rdemx *= len(x)
        rdemx -= sum(x)**2

        rdemy = 0
        for i in y:
            rdemy += i**2
        rdemy *= len(y)
        rdemy -= sum(y)**2

        rdem = rdemx*rdemy
        rdem = math.sqrt(rdem)

        # Prevent division by zero error
        if rdem != 0:
            # Calculate the correlation coefficient
            self.cor_coef = rnum/rdem
        else:
            # If the denominator = 0, the correlation coefficient is undefined
            self.cor_coef = "undefined"

# Define a function to determine whether a string is numeric
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Define a function to determine whether all the items in a list are equal
def is_equal(items):
    for item in items:
        if items[0] != item:
            return False
    return True

# Introduce the program
print()
print("Norton Linear Regression Calculator")
print("Creator: Paul Norton")
print()
print("Enter each point as x and y coordinates separated by a comma: --> 3,5")
print("Press enter again when you are finished")
print()
print("=====================================================================")
print()

# Initialize the variables
points = []
error = True

while error or entry != "":
    error = False

    # Allow user to enter a point
    entry = input("--> ")

    # Check that user entered a valid input
    if entry != "":
        if "," in entry:
            point = entry.split(",")
            if len(point) == 2:
                if is_number(point[0]) and is_number(point[1]):
                    point = [float(point[0]), float(point[1])]
                    points.append(point)
                else:
                    error = True
                    print("Error: non-numeric value detected")
            else:
                print("Error: too many values in one point")
        else:
            error = True
            print("Error: no comma detected")
    else:
        if len(points) < 2 or is_equal(points):
            error = True
            print("Error: not enough points")

print()
print("=====================================================================")
print()

# Instantiate a LinearRegression object
linReg = LinearRegression(points)

# Determine how to display the equation of the line
if linReg.isVertical:
    print("x = " + str(linReg.xint))
else:
    if linReg.yint < 0:
        print("y = " + str(linReg.slope) + "x - " + str(abs(linReg.yint)))
    else:
        print("y = " + str(linReg.slope) + "x + " + str(abs(linReg.yint)))

# Display the correlation coefficient       
print("r = " + str(linReg.cor_coef))
print()

# Graphing portion
if input("Graph the line? (y/n): ") == "y":
    # Instantiate a Turtle object
    turtle = Turtle()
    font = ("Arial", 12, "normal")
    turtle.width(3)

    # Determine how to graph the line
    if not linReg.isVertical:
        slope = linReg.slope
        yint = linReg.yint
        
        # Draw the estimated line

        if slope > 2:
            turtle.goto(200/slope, 200)
            turtle.goto(-200/slope, -200)
        else:
            turtle.goto(100, slope*100)
            turtle.goto(-100, slope*-100)
        turtle.home()

        # Draw the y-axis
        turtle.width(1)
        turtle.goto(0, min(max(abs(slope*110), 110), 210))
        turtle.write("y", font=font)
        turtle.goto(0, max(min(-abs(slope*110), -110), -210))
        turtle.home()
        if linReg.slope > 0:
            turtle.write(str(yint) + " ", align='right', font=font)
        else:
            turtle.write(" " + str(yint), align='left', font=font)   

        # Determine the scale of the y-intercept
        if yint > 0:
            while yint < 10:
                yint *= 10
            while yint > 100:
                yint /= 10
        elif yint < 0:
            while yint > -10:
                yint *= 10
            while yint < -100:
                yint /= 10

        # Draw the x-axis
        turtle.goto(0, -yint)
        turtle.goto(110, -yint)
        turtle.write("x", font=font)
        turtle.goto(-110, -yint)
    
    else:
        xint = linReg.xint
        
        # Determine the scale of the x-intercept
        if xint > 0:
            while xint < 10:
                xint *= 10
            while xint > 100:
                xint /= 10
        elif xint < 0:
            while xint > -10:
                xint *= 10
            while xint < -100:
                xint /= 10

        # Draw the estimated line
        turtle.penup()
        turtle.goto(xint, 100)
        turtle.pendown()
        turtle.goto(xint, -100)
        turtle.goto(xint, 0)

        # Write orginal value of the x-intercept    
        turtle.write(" " + str(linReg.xint), align='left', font=font)
        
        turtle.penup()

        # Draw the y-axis
        turtle.width(1)
        turtle.goto(0, -110)
        turtle.pendown()
        turtle.goto(0, 110)
        turtle.write("y", font=font)
        turtle.penup()
        
        # Draw the x-axis
        turtle.goto(-110, 0)
        turtle.pendown()
        turtle.goto(110, 0)
        turtle.write("x", font=font)
    
    # Hide the pointer
    turtle.hideturtle()

    input("Press enter to complete: ")
