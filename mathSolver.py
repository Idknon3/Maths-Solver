import math
from os import *
from time import *

pi = 22/7

class Cylinder:
    def cylinderVolume():
        global volume
        Cylinder.inputsCylinder()
        volume = float(pi*math.pow(radius, 2)*height)

    def inputsCylinder():
        global height, radius
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

    def toFindHeightOfCylinderCSA():
        global lateral, height, radius
        radius = float(input("Enter The Radius: "))
        lateral = float(input("Enter The CSA: "))
        lateral = float(lateral/2)
        lateral = float(lateral/radius)
        height = float(lateral/pi)

    def toFindRadiusOfCylinderCSA():
        global lateral, height, radius
        height = float(input("Enter The Height: "))
        lateral = float(input("Enter The CSA: "))
        lateral = float(lateral/2)
        lateral = lateral/height
        radius = lateral/pi

    def toFindHeightOfCylinderVolume():
        global height, radius, volume
        volume = float(input("Enter Volume: "))
        radius = float(input("Enter Radius: "))
        height = float(volume/(math.pow(radius, 2)*pi))

    def toFindRadiusOfCylinderVolume():
        global height, radius, volume
        volume = float(input("Enter TSA: "))
        height = float(input("Enter Height: "))
        radius = float(math.sqrt(volume/(pi*height)))

    def toFindHeightOfCylinderTsa():
        global height, radius, tsa
        tsa = float(input("Enter TSA: "))
        radius = float(input("Enter Radius: "))
        tsa = float(tsa/2)
        tsa = float(tsa/pi)
        tsa = float(tsa/radius)
        height = float(tsa-radius)

    def toFindRadiusOfCylinderTsa():
        global height, radius, tsa
        tsa = float(input("Enter TSA: "))
        height = float(input("Enter Height: "))
        tsa = float(tsa/2)
        tsa = float(tsa/pi*height)
        tsa = float(math.sqrt(tsa))
        radius = float(tsa/2)

    def printCylinderOP():
        global cylinderOP
        print("==================Normal-Options==============="
            "\n1. Total Surface Area"
            "\n2. Curved Surface Area"
            "\n3. Volume"
            "\n===================To-Find-From:====================="
            "\n4. Total Surface Area (Height, Radius)"
            "\n5. Curved Surface Area (Height, Radius)"
            "\n6. Volume (Height, Radius)")
        cylinderOP = int(input("Enter Option: "))

    def printToFindCylinderOP():
        global toFindCylinderOP
        print("1. Height"
              "\n2. Radius")
        toFindCylinderOP = int(input("Enter Option:"))

class Cube:
    def inputsCube():
        global side
        side = float(input("Enter Side(in cm): "))

    def findSideOfCubeVolume():
        global side, volume
        volume = float(input("Enter Volume: "))
        side = float(math.cbrt(volume))

    def findSideOfCubeLateral():
        global side, lateral
        lateral = float(input("Enter Lateral Surface Area: "))
        side = float(math.sqrt(lateral/4))

    def findSideOfCubeTotal():
        global side, tsa
        tsa = float(input("Enter Lateral Surface Area: "))
        side = float(math.sqrt(tsa/6))

    def printCubeOP():
        global cubeOP
        print("================Normal-Options=============="
            "\n1. Total Surface Area"
            "\n2. Lateral Surface Area"
            "\n3. Volume"
            "\n==================Find-Side=================="
            "\n4. From Volume"
            "\n5. From Lateral Surface Area"
            "\n6. From Total Surface Area")
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

    def findlengthOfCuboidTsa():
        global breadth, tsa, height, length
        breadth = float(input("Enter Breadth: "))
        height = float(input("Enter Height: "))
        tsa = float(input("Enter TSA: "))
        tsa = float(tsa/2)
        tsa = float(tsa-(height*breadth))
        length = float(tsa/(height+breadth))

    def findbreadthOfCuboidTsa():
        global breadth, tsa, height, length
        length = float(input("Enter Length: "))
        height = float(input("Enter Height: "))
        tsa = float(input("Enter TSA: "))
        tsa = float(tsa/2)
        tsa = float(tsa-(height*length))
        breadth = float(tsa/(height+length))

    def findheightOfCuboidTsa():
        global breadth, tsa, height, length
        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))
        tsa = float(input("Enter TSA: "))
        tsa = float(tsa/2)
        tsa = float(tsa-(breadth*length))
        height = float(tsa/(breadth+length))

    def findlengthOfCuboidLsa():
        global breadth, lateral, height, length
        breadth = float(input("Enter Breadth: "))
        height = float(input("Enter Height: "))
        lateral = float(input("Enter TSA: "))
        lateral = float(lateral/2)
        lateral = float(lateral-(height*breadth))
        length = float(lateral/height)

    def findbreadthOfCuboidLsa():
        global breadth, tsa, height, length
        length = float(input("Enter Length: "))
        height = float(input("Enter Height: "))
        lateral = float(input("Enter TSA: "))
        lateral = float(lateral/2)
        lateral = float(lateral-(height*length))
        breadth = float(lateral/height)

    def findheightOfCuboidLsa():
        global breadth, lateral, height, length
        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))
        lateral = float(input("Enter TSA: "))
        lateral = float(lateral/2)
        height = float(lateral/(length+breadth))

    def findheightOfCuboidVolume():
        global breadth, volume, height, length
        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))
        volume = float(input("Enter Volume: "))
        height = float(volume/(length*breadth))

    def findlengthOfCuboidVolume():
        global breadth, volume, height, length
        length = float(input("Enter Height: "))
        breadth = float(input("Enter Breadth: "))
        volume = float(input("Enter Volume: "))
        height = float(volume/(height*breadth))

    def findbreadthOfCuboidVolume():
        global breadth, volume, height, length
        length = float(input("Enter Length: "))
        breadth = float(input("Enter Height: "))
        volume = float(input("Enter Volume: "))
        height = float(volume/(length*height))

    def printCuboidOP():
        global cuboidOP
        print("================Normal-Options:============="
            "\n1. Total Surface Area"
            "\n2. Lateral Surface Area"
            "\n3. Volume"
            "\n=================Find-Side:==============="
            "\n4. From Total Surface Area:(Height / Breadth / Length)"
            "\n5. From Lateral Surface Area:(Height / Breadth / Length)"
            "\n6. From Volume:(Height / Breadth / Length)")
        cuboidOP = int(input("Enter Option: "))

    def printToFindCuboidOP():
        global toFindCuboidOP
        print("1. Height"
              "\n2. Breadth"
              "\n3. Length")
        toFindCuboidOP = int(input("Enter Option:"))

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

    def sideFindSquareArea():
        global area, side
        area = float(input("Enter Area:"))
        side = float(math.sqrt(area))

    def sideFindSquarePerimeter():
        global perimeter, side
        perimeter = float(input("Enter Perimeter: "))
        side = float(perimeter/4)

    def printSquareOP():
        global squareOP
        print("====================Normal-Options==============="
            "\n1. Find Perimeter"
            "\n2. Find Area"
            "\n=====================Find-Side:================="
            "\n3. From Perimeter"
            "\n4. From Area")
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

    def lengthFindInputRectanglePerimeter():
        global breadth, perimeter
        breadth = float(input("Enter Breadth: "))
        perimeter = float(input("Enter Perimeter: "))

    def breadthFindInputRectanglePerimeter():
        global length, perimeter
        length = float(input("Enter length: "))
        perimeter = float(input("Enter Perimeter: "))

    def breadthFindInputRectangleArea():
        global area, breadth
        area = float(input("Enter Area: "))
        breadth = float(input("Enter Breadth: "))

    def lengthFindInputRectangleArea():
        global area, length
        area = float(input("Enter Area: "))
        length = float(input("Enter Length: "))

    def printRectangleOP():
        global rectangleOP
        print("============Normal-Options===================="
            "\n1. Perimeter"
            "\n2. Area"
            "==============Perimeter-Options================="
            "\n3. Find length"
            "\n4. Find breadth"
            "==============Area-Options======================"
            "\n5. Find length"
            "\n6. Find breadth")
        rectangleOP = int(input("Enter Option: "))

    def rectangleArea():
        global area
        Rectangle.inputsRectangle()
        area = float(length*breadth)

    def lengthFindRectanglePerimeter():
        global length
        Rectangle.lengthFindInputRectanglePerimeter()
        length = float(perimeter-breadth/2)
    
    def breadthFindRectanglePerimeter():
        global breadth
        Rectangle.breadthFindInputRectanglePerimeter()
        breadth = float(perimeter-length/2)

    def breadthFindRectangleArea():
        global breadth
        Rectangle.breadthFindInputRectangleArea()
        breadth = float(area/length)

    def lengthFindRectangleArea():
        global length
        Rectangle.lengthFindInputRectangleArea()
        length = float(area/breadth)

    def rectanglePerimeter():
        global perimeter
        Rectangle.inputsRectangle()
        perimeter = float(2*(length+breadth))

class Triangle:
    def areaInputsTriangle():
        global base, height
        height = float(input("Enter Height(in cm): "))
        base = float(input("Enter Base(in cm): "))

    def lengthinputTriangle():
        global length1, length2, length3
        length1 = float(input("Enter The First Length: "))
        length2 = float(input("Enter The Second Length: "))
        length3 = float(input("Enter The Third Length: "))

    def findAreaOfEquilateralTriangle():
        global triangleArea, triangleHalf
        Triangle.lengthinputTriangle()
        triangleHalf = float((length1 + length2 + length3)/2)
        triangleArea = float(math.sqrt(triangleHalf*((triangleHalf - length1)*(triangleHalf - length2)*(triangleHalf - length3))))

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
            "\n2. Area Of Equilateral Triangle"
            "\n================================"
            "\n3. Find Hypotenuse"
            "\n4. Find Perpendicular"
            "\n5. Find Base")
        triangleOP = int(input("Enter Option: "))

    def triangleArea():
        global area
        Triangle.areaInputsTriangle()
        area = float(1/2*base*height)

class CIandSICalc:
    def printCISIOp():
        global CISIOP
        print("1. Find Compound Interest & Amount"
            "\n2. Find Simple Interest"
            "\n3. Find CI And Amount At Depreciation"
            "\n4. Find Rate/Time Period/Principal From SI"
            "\n5. Find Rate/Time Period/Principal From CI")
        CISIOP = int(input("Enter Option: "))

    def toFindOP():
        global toFindOPCISI
        print("1. Find Rate Of Interest"
              "\n2. Find Time Period"
              "\n3. Find Principal Amount")
        toFindOPCISI = int(input("Enter Option: "))

    def findRateFromSI():
        global rate, principal, timeperiod, si
        si = float(input("Enter The Simple Interest: "))
        principal = float(input("Enter The Principal Amount: "))
        timeperiod = float(input("Enter The Timeperiod: "))
        si = float(si/principal)
        si = float(si/timeperiod)
        rate = float(si*100)

    def findTimePeriodFromSI():
        global rate, principal, timeperiod, si
        si = float(input("Enter The Simple Interest: "))
        principal = float(input("Enter The Principal Amount: "))
        rate = float(input("Enter The Rate Of Interest: "))
        si = float(si/principal)
        si = float(si/rate)
        timeperiod = float(si*100)

    def findPrincipalFromSI():
        global rate, principal, timeperiod, si
        si = float(input("Enter The Simple Interest: "))
        rate = float(input("Enter The Rate: "))
        timeperiod = float(input("Enter The Timeperiod: "))
        si = float(si/rate)
        si = float(si/timeperiod)
        principal = float(si*100)

    def findRateFromCI():
        global rate, principal, timeperiod, ci, amount, AmOrCI
        principal = float(input("Enter The Principal Amount: "))
        timeperiod = float(input("Enter The Timeperiod: "))
        AmOrCI = int(input("Amount/CI [1/2] "))
        if AmOrCI == 1:
            amount = float(input("Enter The Amount: "))
        else:
            ci = float(input("Enter The CI: "))
            amount = ci+principal
        if timeperiod == 6:
            amount = float(amount/principal)
            amount = float(math.cbrt(math.cbrt(amount)))
            rate = float((100*amount)-100) 
        if timeperiod == 5:
            amount = float(amount/principal)
            amount = float(math.cbrt(math.sqrt(amount)))
            rate = float((100*amount)-100) 
        if timeperiod == 4:
            amount = float(amount/principal)
            amount = float(math.sqrt(math.sqrt(amount)))
            rate = float((100*amount)-100) 
        if timeperiod == 3:
            amount = float(amount/principal)
            amount = float(math.cbrt(amount))
            rate = float((100*amount)-100)
        if timeperiod == 2:
            amount = float(amount/principal)
            amount = float(math.sqrt(amount))
            rate = float((100*amount)-100)
        if timeperiod == 1:
            amount = float(amount/principal)
            rate = float((100*amount)-100)   

    def findTimePeriodFromCI():
        global rate, principal, timeperiod, ci, AmOrCI, amount
        principal = float(input("Enter The Principal Amount: "))
        rate = float(input("Enter The Rate Of Interest: "))
        AmOrCI = int(input("Amount/CI [1/2] "))
        rate = float(1+rate/100)
        if AmOrCI == 1:
            amount = float(input("Enter The Amount: "))
        else:
            ci = float(input("Enter The CI: "))
            amount = ci+principal
        if float(math.sqrt(amount/principal)) != float(rate):
            timeperiod = 3
            system("cls")
        if float(math.sqrt(amount/principal)) == float(rate):
            timeperiod = 2
            system("cls")

    def findPrincipalFromCI():
        global rate, principal, timeperiod, ci, AmOrCI, amount
        timeperiod = float(input("Enter The Time Period: "))
        rate = float(input("Enter The Rate Of Interest: "))
        AmOrCI = int(input("Amount/CI [1/2] "))
        if AmOrCI == 1:
            amount = float(input("Enter The Amount: "))
        else:
            ci = float(input("Enter The CI: "))
            amount = ci+principal
        if timeperiod == 6:
            amount = float(math.cbrt(math.cbrt(amount)))
            amount = float(amount*100)
            amount = float(amount-100)
            principal = float(amount/rate) 
        if timeperiod == 5:
            amount = float(math.cbrt(math.sqrt(amount)))
            amount = float(amount*100)
            amount = float(amount-100)
            principal = float(amount/rate) 
        if timeperiod == 4:
            amount = float(math.sqrt(math.sqrt(amount)))
            amount = float(amount*100)
            amount = float(amount-100)
            principal = float(amount/rate) 
        if timeperiod == 3:
            amount = float(math.cbrt(amount))
            amount = float(amount*100)
            amount = float(amount-100)
            principal = float(amount/rate)
        if timeperiod == 2:
            amount = float(math.sqrt(amount))
            amount = float(amount*100)
            amount = float(amount-100)
            principal = float(amount/rate)
        if timeperiod == 1:
            amount = float(amount*100)
            amount = float(amount-100)
            principal = float(amount/rate)
        
    def CiInputs():
        global rate, principal, timeperiod
        rate = float(input("Enter The Rate Of Interset: "))
        principal = float(input("Enter The Pricipal Amount: "))
        timeperiod = float(input("Enter The Time Period: "))

    def FindAmountAndCI():
        global rate, principal, timeperiod, amount, ci
        CIandSICalc.CiInputs()
        amount = float(principal*(math.pow((1+rate/100), timeperiod)))
        ci = float(amount - principal)

    def FindDepreciatedAmountAndCI():
        global rate, principal, timeperiod, amount, ci
        CIandSICalc.CiInputs()
        amount = float(principal*(math.pow((1-rate/100), timeperiod)))
        ci = float(amount - principal)

    def FindSimpleInterest():
        global rate, principal, timeperiod, amount, si
        CIandSICalc.CiInputs()
        si = float(principal*rate*timeperiod/100)
    
    def printcisivalues(value1, value2):
        system("cls")
        print("(Rounded Off to 2) Compound Interest: "+str(round(value1,2)))
        print("(Rounded Off to 2) Amount: "+str(round(value2,2)))

class SpeedTimeDistanceCalc:
    def printSpeedTimeDistanceOp():
        global timespeeddistanceop
        print("\n===========SPEED-TIME-DISTANCE-CALCULATOR=========="
              "\n1. Find Speed"
              "\n2. Find Distance"
              "\n3. Find Time")
        timespeeddistanceop = int(input("Enter Option: "))

    def printToFindOpSTD():
        global findtdsop
        print("\n1. Find Time"
              "\n2. Find Distance")
        findtdsop = int(input("Enter The Option: "))

    def unitDecide():
        global unitop
        unitop = int(input("Unit in meter/second Or kilometer/hour[1/2]: "))

    def findSpeed():
        global speed, timep, distance
        SpeedTimeDistanceCalc.unitDecide()
        if unitop == 1:
            distance = float(input("Enter The Distance In Meters: "))
            timep = float(input("Enter The Time In Seconds: "))
            speed = float(distance/timep)
            system("cls")
            print("Speed Is: {0}".format(speed),end = ("m/s"))
        if unitop == 2:
            distance = float(input("Enter The Distance In Kilo Meters: "))
            timep = float(input("Enter The Time In Hour: "))
            speed = float(distance/timep)
            system("cls")
            print("Speed Is: {0}".format(speed),end = ("m/s"))

    def findDistance():
        global speed, timep, distance
        SpeedTimeDistanceCalc.unitDecide()
        if unitop == 1:
            speed = float(input("Enter The Speed In m/s: "))
            timep = float(input("Enter The Time In Seconds: "))
            distance = float(speed*timep)
            system("cls")
            print("Distance Is: {0}".format(distance),end = ("m"))
        if unitop == 2:
            speed = float(input("Enter The Speed In Kilo Meters: "))
            timep = float(input("Enter The Time In Hour: "))
            distance = float(speed*timep)
            system("cls")
            print("Distance Is: {0}".format(distance),end = ("km"))
    
    def findTime():
        global speed, timep, distance
        SpeedTimeDistanceCalc.unitDecide()
        if unitop == 1:
            speed = float(input("Enter The Speed In m/s: "))
            distance = float(input("Enter The Distance In Meters: "))
            timep = float(distance/speed)
            system("cls")
            print("Distance Is: {0}".format(timep),end = ("Sec"))
        if unitop == 2:
            speed = float(input("Enter The Speed In km/h: "))
            distance = float(input("Enter The Distance In Kilometers: "))
            timep = float(distance/speed)
            system("cls")
            print("Time Is: {0}".format(timep),end = ("Hrs"))

def shapeStarter():
    global shapeoption
    system("cls")
    print("\n========SHAPES SOLVER========"
          "\n1. Cylinder"
        "\n2. Cube"
        "\n3. Cuboid"
        "\n4. Square"
        "\n5. Circle"
        "\n6. Rectangle"
        "\n7. Triangle")
    shapeoption = int(input("Enter Value: "))

def mainStarter():
    global mainoption
    print("\n========MATH SOLVER========"
          "\n1. Shapes Solver"
          "\n2. Compound And Simple Interest Solver"
          "\n3. Speed, Time And Distance Calculator"
          "\n4. Table Printer")
    mainoption = int(input("Enter Value: "))

def table():
    global num, result
    num = int(input("Enter a Number:"))
    result = 0

    for i in range(1, 11):
        result = num * i
        print(str(num)+"x"+str(i)+"="+str(result))
        sleep(0.1)

while True:
    mainStarter()
    if mainoption == 1:
        shapeStarter()
        if shapeoption == 1:
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
            elif cylinderOP == 4:
                system("cls")
                Cylinder.printToFindCylinderOP()
                if toFindCylinderOP == 1:
                    Cylinder.toFindHeightOfCylinderTsa()
                    valuetofind = height
                    value = "Height"
                    power = "cm"
                if toFindCylinderOP == 2:
                    Cylinder.toFindRadiusOfCylinderTsa()
                    valuetofind = radius
                    value = "radius"
                    power = "cm"
            elif cylinderOP == 5:
                system("cls")
                Cylinder.printToFindCylinderOP()
                if toFindCylinderOP == 1:
                    Cylinder.toFindHeightOfCylinderCSA()
                    valuetofind = height
                    value = "Height"
                    power = "cm"
                if toFindCylinderOP == 2:
                    Cylinder.toFindRadiusOfCylinderCSA()
                    valuetofind = radius
                    value = "radius"
                    power = "cm"
            elif cylinderOP == 6:
                system("cls")
                Cylinder.printToFindCylinderOP()
                if toFindCylinderOP == 1:
                    Cylinder.toFindHeightOfCylinderVolume()
                    valuetofind = height
                    value = "Height"
                    power = "cm"
                if toFindCylinderOP == 2:
                    Cylinder.toFindRadiusOfCylinderVolume()
                    valuetofind = radius
                    value = "radius"
                    power = "cm"
            else:
                print("Option Not Available!")
                sleep(1)
                continue
        
        elif shapeoption == 2:
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
            elif cubeOP == 4:
                Cube.findSideOfCubeVolume()
                valuetofind = side
                value = "Side"
                power = "cm"
            elif cubeOP == 5:
                Cube.findSideOfCubeLateral()
                valuetofind = side
                value = "Side"
                power = "cm"
            elif cubeOP == 6:
                Cube.findSideOfCubeTotal()
                valuetofind = side
                value = "Side"
                power = "cm"
            else:
                print("Option Not Available!")
                sleep(1.5)
                continue

        elif shapeoption == 3:
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
            elif cuboidOP == 4:
                system("cls")
                Cuboid.printToFindCuboidOP()
                if toFindCuboidOP == 1:
                    Cuboid.findheightOfCuboidTsa()
                    valuetofind = height
                    value = "height"
                    power = "cm"
                if toFindCuboidOP == 2:
                    Cuboid.findbreadthOfCuboidTsa()
                    valuetofind = breadth
                    value = "Breadth"
                    power = "cm"
                elif toFindCuboidOP == 3:
                    Cuboid.findlengthOfCuboidTsa()
                    valuetofind = length
                    value = "Length"
                    power = "cm"
            elif cuboidOP == 5:
                system("cls")
                Cuboid.printToFindCuboidOP()
                if toFindCuboidOP == 1:
                    Cuboid.findheightOfCuboidLsa()
                    valuetofind = height
                    value = "height"
                    power = "cm"
                if toFindCuboidOP == 2:
                    Cuboid.findbreadthOfCuboidLsa()
                    valuetofind = breadth
                    value = "Breadth"
                    power = "cm"
                elif toFindCuboidOP == 3:
                    Cuboid.findlengthOfCuboidLsa()
                    valuetofind = length
                    value = "Length"
                    power = "cm"
            elif cuboidOP == 6:
                system("cls")
                Cuboid.printToFindCuboidOP()
                if toFindCuboidOP == 1:
                    Cuboid.findheightOfCuboidVolume()
                    valuetofind = height
                    value = "height"
                    power = "cm"
                if toFindCuboidOP == 2:
                    Cuboid.findbreadthOfCuboidVolume()
                    valuetofind = breadth
                    value = "Breadth"
                    power = "cm"
                elif toFindCuboidOP == 3:
                    Cuboid.findlengthOfCuboidVolume()
                    valuetofind = length
                    value = "Length"
                    power = "cm"
            else:
                print("Option Not Available!")
                sleep(1.5)
                continue

        elif shapeoption == 4:
            system("cls")
            Square.printSquareOP()
            shape = "Square"
            if squareOP == 1:
                Square.squarePerimeter()
                valuetofind = perimeter
                value = "Perimeter"
                power = "cm"
            elif squareOP == 2:
                Square.squareArea()
                valuetofind = area
                value = "Area"
                power = "cm sq"
            elif squareOP == 4:
                Square.sideFindSquareArea()
                valuetofind = side
                value = "Side"
                power = "cm"
            elif squareOP == 3:
                Square.sideFindSquarePerimeter()
                valuetofind = side
                value = "Side"
                power = "cm"
            else:
                print("Option Not Available!")
                sleep(1.5)
                continue

        elif shapeoption == 5:
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

        elif shapeoption == 6:
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
            elif rectangleOP == 3:
                Rectangle.lengthFindRectanglePerimeter()
                valuetofind = length
                value = "Length"
                power = "cm"
            elif rectangleOP == 4:
                Rectangle.breadthFindRectanglePerimeter()
                valuetofind = breadth
                value = "Breadth"
                power = "cm"
            elif rectangleOP == 5:
                Rectangle.lengthFindRectangleArea()
                valuetofind = length
                value = "Length"
                power = "cm"
            elif rectangleOP == 6:
                Rectangle.breadthFindRectangleArea()
                valuetofind = breadth
                value = "Breadth"
                power = "cm"
            else:
                print("Option Not Available!")
                sleep(1.5)
                continue
        
        elif shapeoption == 7:
            system("cls")
            shape = "Triangle"
            Triangle.printTriangleOP()
            if triangleOP == 1:
                Triangle.triangleArea()
                valuetofind = area
                value = "Area"
                power =  "cm sq"
            elif triangleOP == 2:
                Triangle.findAreaOfEquilateralTriangle()
                valuetofind = triangleArea
                value = "Area"
                power =  "cm sq"
            elif triangleOP == 3:
                Triangle.hypotenuseTriangle()
                valuetofind = hypotenuse
                value = "Hypotenuse"
                power =  "cm"
            elif triangleOP == 4:
                Triangle.perpendicularTriangle()
                valuetofind = perpendicular
                value = "Perpendicular"
                power =  "cm"
            elif triangleOP == 5:
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
        system("cls")
        roundValue = round(valuetofind, 2)
        print("(Rounded Off to 2) "+value+" Of "+shape+" = "+str(roundValue)+" ",end=power)

    if mainoption == 2:
        system("cls")
        CIandSICalc.printCISIOp()
        if CISIOP == 1:
            system("cls")
            CIandSICalc.FindAmountAndCI()
            CIandSICalc.printcisivalues(ci, amount)
        if CISIOP == 2:
            system("cls")
            CIandSICalc.FindSimpleInterest()
            system("cls")
            print("Simple Interest: ",str(si))
        if CISIOP == 3:
            system("cls")
            CIandSICalc.FindDepreciatedAmountAndCI()
            CIandSICalc.printcisivalues(ci, amount)
        if CISIOP == 4:
            system("cls")
            CIandSICalc.toFindOP()
            if toFindOPCISI == 1:
                CIandSICalc.findRateFromSI()
                system("cls")
                print("Rate Of Simple Interest: "+str(round(rate, 2)),end="%")
            if toFindOPCISI == 2:
                CIandSICalc.findTimePeriodFromSI()
                system("cls")
                print("Time Period Of Simple Interest: "+str(round(timeperiod, 2)),end="%")
            if toFindOPCISI == 3:
                CIandSICalc.findPrincipalFromSI()
                system("cls")
                print("Principal Of Simple Interest: "+str(round(rate, 2)),end="%")
        if CISIOP == 5:
            system("cls")
            CIandSICalc.toFindOP()
            if toFindOPCISI == 1:
                CIandSICalc.findRateFromCI()
                system("cls")
                print("Rate Of Compound Interest: "+str(round(rate, 2)),end="%")
            if toFindOPCISI == 2:
                CIandSICalc.findTimePeriodFromCI()
                system("cls")
                print("Time Period Of Compound Interest: "+str(int(timeperiod)))
            if toFindOPCISI == 3:
                CIandSICalc.findPrincipalFromCI()
                system("cls")
                print("Principal Of Compound Interest: "+str(round(rate, 2)),end="%")

    if mainoption == 3:
        system("cls")
        SpeedTimeDistanceCalc.printSpeedTimeDistanceOp()
        if timespeeddistanceop == 1:
            SpeedTimeDistanceCalc.findSpeed()
        if timespeeddistanceop == 2:
            SpeedTimeDistanceCalc.findDistance()
        if timespeeddistanceop == 3:
            SpeedTimeDistanceCalc.findTime()
    
    if mainoption == 4:
        table()

#Made By IDK
