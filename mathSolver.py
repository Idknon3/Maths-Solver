import math
from os import *
from time import *

pi = 22/7
valuetofind = 0
power = 0

class Cylinder:
    def cylinderVolume():
        global volume
        Cylinder.inputsCylinder()
        volume = float(pi*math.pow(radius, 2)*height)

    def inputsCylinder():
        global height, radius
        radius = 0
        height = 0
        height = float(input("Enter Height(in cm): "))
        radius = float(input("Enter Radius(in cm): "))

    def tsaCylinder():
        global tsa
        Cylinder.inputsCylinder()
        tsa = float(2*pi*radius*(height+radius))

    def csaCylinder():
        global csa
        Cylinder.inputsCylinder()
        csa = float(2*pi*radius*height)
        
    def printCylinderOP():
        global cylinderOP
        print("\n1. Total Surface Area"
            "\n2. Curved Surface Area"
            "\n3. Volume")
        cylinderOP = int(input("Enter Option: "))

class Cube:
    def inputsCube():
        global side
        side = float(input("Enter Side(in cm): "))

    def printCubeOP():
        global cubeOP
        print("\n1. Total Surface Area"
            "\n2. Lateral Surface Area"
            "\n3. Volume")
        cubeOP = int(input("Enter Option: "))

    def cubeTotalSurfaceArea():
        global tsa
        Cube.inputsCube()
        tsa = float(6*math.pow(side, 2))

    def cubeVolume():
        global volume
        Cube.inputsCube()
        volume = float(math.pow(side, 2))
    
    def cubeLateral():
        global lateral
        Cube.inputsCube()
        lateral = float(4*math.pow(side, 2))

class Cuboid:
    def inputsCuboid():
        global height, breadth, length
        height = float(input("Enter Side(in cm): "))
        breadth = float(input("Enter The Breadth(in cm): "))
        length = float(input("Enter The Length(in cm): "))

    def printCuboidOP():
        global cuboidOP
        print("\n1. Total Surface Area"
            "\n2. Lateral Surface Area"
            "\n3. Volume")
        cuboidOP = int(input("Enter Option: "))

    def cuboidTotalSurfaceArea():
        global tsa
        Cuboid.inputsCuboid()
        tsa = float(2*(length*breadth + breadth*height + height*length))

    def cuboidVolume():
        global volume
        Cuboid.inputsCuboid()
        volume = float(length * breadth * height)
    
    def cuboidLateral():
        global lateral
        Cube.inputsCube()
        lateral = float(2*(length+breadth)*height)

class Square:
    def inputsSquare():
        global side
        side = float(input("Enter Side(in cm): "))

    def printSquareOP():
        global squareOP
        print("\n1. Perimeter"
            "\n2. Area")
        squareOP = int(input("Enter Option: "))

    def squareArea():
        global area
        Square.inputsSquare()
        area = float(math.pow(side, 2))

    def squarePerimeter():
        global perimeter
        Square.inputsSquare()
        perimeter = float(4*side)

class Circle:
    def inputsCircleValue():
        global radius
        radius = float(input("Enter Radius(in cm): "))

    def printCircleOP():
        global circleOP
        print("\n1. Circumference"
            "\n2. Area"
            "\n3. Find Radius From Circumference"
            "\n4. Find Radius From Area")
        circleOP = int(input("Enter Option: "))

    def findRadiusCircumferneceInput():
        global circumference
        circumference = float(input("Enter Circumference: "))

    def findRadiusCircumference():
        global radius
        Circle.findRadiusCircumferneceInput()
        radius = float(circumference/(2*pi))

    def findRadiusAreaInput():
        global area
        area = float(input("Enter Area: "))

    def findRadiusArea():
        global radius
        Circle.findRadiusAreaInput()
        radius = float(math.sqrt(area)/(2*pi))

    def circleArea():
        global area
        Circle.inputsCircleValue()
        area = float(pi*math.pow(radius, 2))

    def circleCircumference():
        global circumference
        Circle.inputsCircleValue()
        circumference = float(2*pi*radius)

class Rectangle:
    def inputsRectangle():
        global length, breadth
        length = float(input("Enter Length(in cm): "))
        breadth = float(input("Enter Breadth(in cm): "))

    def printRectangleOP():
        global rectangleOP
        print("\n1. Perimeter"
            "\n2. Area")
        rectangleOP = int(input("Enter Option: "))

    def rectangleArea():
        global area
        Rectangle.inputsRectangle()
        area = float(length*breadth)

    def rectanglePerimeter():
        global perimeter
        Rectangle.inputsRectangle()
        perimeter = float(2*(length+breadth))

class Triangle:
    def areaInputsTriangle():
        global base, height
        height = float(input("Enter Height(in cm): "))
        base = float(input("Enter Base(in cm): "))

    def hypotenuseFindInputsTriangle():
        global perpendicular, base
        perpendicular = float(input("Enter Perpendicular(in cm): "))
        base = float(input("Enter Base(in cm): "))

    def perpendicularFindInputsTriangle():
        global hypotenuse, base
        hypotenuse = float(input("Enter Hypotenuse(in cm): "))
        base = float(input("Enter Base(in cm): "))

    def baseFindInputsTriangle():
        global hypotenuse, perpendicular
        hypotenuse = float(input("Enter Hypotenuse(in cm): "))
        perpendicular = float(input("Enter Perpendicular(in cm): "))

    def baseTriangle():
        global base
        Triangle.baseFindInputsTriangle()
        base = float(math.sqrt(math.pow(hypotenuse, 2)-math.pow(perpendicular, 2)))

    def perpendicularTriangle():
        global perpendicular
        Triangle.perpendicularFindInputsTriangle()
        perpendicular = float(math.sqrt(math.pow(hypotenuse, 2)-math.pow(base, 2)))

    def hypotenuseTriangle():
        global hypotenuse
        Triangle.hypotenuseFindInputsTriangle()
        hypotenuse = float(math.sqrt(math.pow(perpendicular, 2)+math.pow(base, 2)))

    def printTriangleOP():
        global triangleOP
        print("\n1. Area"
            "\n================================"
            "\n2. Find Hypotenuse"
            "\n3. Find Perpendicular"
            "\n4. Find Base")
        triangleOP = int(input("Enter Option: "))

    def triangleArea():
        global area
        Triangle.areaInputsTriangle()
        area = float(1/2*base*height)

def mainStarter():
    global option
    system("cls")
    print("\n========MATH SOLVER========"
          "\n"
          "\n1. Cylinder"
        "\n2. Cube"
        "\n3. Cuboid"
        "\n4. Square"
        "\n5. Circle"
        "\n6. Rectangle"
        "\n7. Triangle")
    option = int(input("Enter Value: "))

while True:
    mainStarter()
    if option == 1:
        option = 0
        system("cls")
        shape = "Cylinder"
        Cylinder.printCylinderOP()
        if cylinderOP == 1:
            Cylinder.tsaCylinder()
            valuetofind = tsa
            value = "TSA"
            power = "cm sq"
        elif cylinderOP == 2:
            Cylinder.csaCylinder()
            valuetofind = csa
            value = "CSA"
            power = "cm sq"
        elif cylinderOP == 3:
            Cylinder.cylinderVolume()
            valuetofind = volume
            value = "Volume"
            power = "cub. cm"
        else:
            print("Option Not Available!")
            sleep(1)
            continue
    
    elif option == 2:
        system("cls")
        shape = "Cube"
        Cube.printCubeOP()
        if cubeOP == 1:
           Cube.cubeTotalSurfaceArea()
           valuetofind = tsa
           value = "TSA"
           power = "cm sq"
        elif cubeOP == 2:
           Cube.cubeLateral()
           valuetofind = lateral
           value = "LSA"
           power = "cm sq"
        elif cubeOP == 3:
           Cube.cubeVolume()
           valuetofind = volume
           value = "Volume"
           power = "cub. cm"
        else:
            print("Option Not Available!")
            sleep(1.5)
            continue

    elif option == 3:
        system("cls")
        shape = "Cuboid"
        Cuboid.printCuboidOP()
        if cuboidOP == 1:
           Cuboid.cuboidTotalSurfaceArea()
           valuetofind = tsa
           value = "TSA"
           power = "cm sq"
        elif cuboidOP == 2:
           Cuboid.cuboidLateral()
           valuetofind = lateral
           value = "LSA"
           power = "cm sq"
        elif cuboidOP == 3:
           Cuboid.cuboidVolume()
           valuetofind = volume
           value = "Volume"
           power = "cub. cm"
        else:
            print("Option Not Available!")
            sleep(1.5)
            continue

    elif option == 4:
        system("cls")
        Square.printSquareOP()
        shape = "Square"
        if squareOP == 1:
            Square.squarePerimeter()
            valuetofind = perimeter
            value = "Perimeter"
            power = "cm"
        if squareOP == 2:
            Square.squareArea()
            valuetofind = area
            value = "Area"
            power = "cm sq"
        else:
            print("Option Not Available!")
            sleep(1.5)
            continue

    elif option == 5:
        system("cls")
        shape = "Circle"
        Circle.printCircleOP()
        if circleOP == 1:
            Circle.circleCircumference()
            valuetofind = circumference
            value = "Circumference"
            power = "cm"
        elif circleOP == 2:
            Circle.circleArea()
            valuetofind = area
            value = "Area"
            power = "cm sq"
        elif circleOP == 3:
            Circle.findRadiusCircumference()
            valuetofind = radius
            value = "Radius"
            power = "cm"
        elif option == 4:
            Circle.findRadiusArea()
            valuetofind = radius
            value = "Radius"
            power = "cm"
        else:
            print("Option Not Available!")
            sleep(1.5)
            continue

    elif option == 6:
        system("cls")
        shape = "Rectangle"
        Rectangle.printRectangleOP()
        if rectangleOP == 1:
            Rectangle.rectanglePerimeter()
            valuetofind = perimeter
            value = "Perimeter"
            power = "cm"
        elif rectangleOP == 2:
            Rectangle.rectangleArea()
            valuetofind = area
            value = "Area"
            power = "cm sq"
        else:
            print("Option Not Available!")
            sleep(1.5)
            continue
    
    elif option == 7:
        system("cls")
        shape = "Triangle"
        Triangle.printTriangleOP()
        if triangleOP == 1:
            Triangle.triangleArea()
            valuetofind = area
            value = "Area"
            power =  "cm sq"
        elif triangleOP == 2:
            Triangle.hypotenuseTriangle()
            valuetofind = hypotenuse
            value = "Hypotenuse"
            power =  "cm"
        elif triangleOP == 3:
            Triangle.perpendicularTriangle()
            valuetofind = perpendicular
            value = "Perpendicular"
            power =  "cm"
        elif triangleOP == 4:
            Triangle.baseTriangle()
            valuetofind = base
            value = "Base"
            power =  "cm"
        else:
            print("Option Not Available!")
            sleep(1.5)
            continue
    else:
        print("Option Not Available!")
        sleep(1.5)
        continue

    roundValue = round(valuetofind, 2)
    print("(Rounded Off to 2) "+value+" Of "+shape+" = "+str(roundValue)+" ",end=power)
