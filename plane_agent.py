__author__ = 'kaya'
import sys
import math
argvs = sys.argv
argc = len(argvs) # length will return the number of arguments
#including the python file.
# store information from arguments "python plane_agent.py weather.txt euclidean 7"
weatherInfo = argvs[1]
heuristic = argvs[2]
fuel = argvs[3]


def buildMap(weatherInfo):
    """
    read input file and build a corresponding map

    :param weatherInfo:
    """
    f = open(weatherInfo)
    line = f.readline()
    weatherMap = []
    while line:
        temp = []
        print "line = " + line
        print "len(line) = " + str(len(line))
        for i in range(0,len(line)-1):
            temp.append(line[i])
        weatherMap.append(temp)
        #print "len =" , len(weatherMap) can obtain num of w
        line = f.readline()
    f.close()

    print "weather Map", weatherMap
    return weatherMap

def drawMap(map):
    """
    draw a map info
    :param map:
    """

    print map
def euclidean(i1,j1,i2,j2):
    """
    if point1 = (i1,j1) and point2 = (i2,j2) are given,
    then the euclidean(i.e. straight line) distance is obtained by:
    sqrt((i1-i2)^2 + (j1-j2)^2 )
    :param i1:horizontal value for point1
    :param j1:vertical value for point1
    :param i2:horizontal value for point2
    :param j2:vertical value for point2
    """
    euclideanDist = math.sqrt((i1-i2)^2 + (j1-j2)^2)
    return euclideanDist
def manhattan(i1,j1,i2,j2):
    manhattanDis = abs(i1+i2) + abs(j1+j2)
    return manhattanDis
def fuelDistance():
    pass

def getUsedDistance(fuel):
    pass
def findAirPlane(map):
    row = len(map)
    for i in range(0,row):
        column = len(map[row])
        for j in range(column):
            if map[row][column] == 'A':
                Neededfuel = 1
                location = (row, column, Neededfuel)
            elif map[row][column] == 'B':
                Neededfuel = 2
                location = (row, column, Neededfuel)
            elif map[row][column] == 'C':
                Neededfuel = 3
                location = (row, column,Neededfuel)
            elif map[row][column] == 'D':
                Neededfuel = 4
                location = (row, column,Neededfuel)
            elif map[row][column] == 'E':
                Neededfuel = 5
                location = (row, column,Neededfuel)
            elif map[row][column] == 'F':
                Neededfuel = 6
                location = (row, column,Neededfuel)
            elif map[row][column] == 'G':
                Neededfuel = 7
                location = (row, column,Neededfuel)
            elif map[row][column] == 'H':
                Neededfuel = 8
                location = (row, column,Neededfuel)
            elif map[row][column] == 'I':
                Neededfuel = 9
                location = (row, column,Neededfuel)
            else:
                print "Can not find an airplane!"
    return location








print "heuristic = " + heuristic
print "fuel = " + fuel
print "weatherInfo = " + weatherInfo
map = buildMap(weatherInfo)
print "Lenmap", len(map)
print "Len map[row = 0]", len(map[0])
print findAirPlane(map)
''''
str = "2"
print str.isdigit()
str1 = 'A'
print str1.isdigit()
'''
print "end"