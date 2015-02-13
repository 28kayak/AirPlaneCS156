__author__ = 'kaya'
import sys
import math
argvs = sys.argv
argc = len(argvs) # length will return the number of arguments
#including the python file.
#store information from arguments "python plane_agent.py weather.txt euclidean 7"
weatherInfo = argvs[1]
heuristic = argvs[2]
fuel = argvs[3]


def buildMap(weatherInfo):
    """
    read input file and build a corresponding map

    :param weatherInfo:
    """
    f = open(weatherInfo)
    line = f.readline()#include a new line char
    weatherMap = []
    while line:
        temp = []
        print "line = " + line
        print "len(line) = " + str(len(line))
        for i in range(0, len(line) -1):
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
    print "Draw Current Map"
    rowInfo = ''
    for i in range(0,len(map)):
        for j in range(0, len(map[i])):

            sys.stdout.write(map[i][j])
        print ""

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
    """
    Find a starting point and return its location
    :param map:
    :return location: location contains (x,y,fuel needed to go to the next box)
    """
    row = len(map)
    print row
    for i in range(0,row):
        print i
        print map[row]
        column = len(map[i])
        for j in range(0, column):
            if map[i][j] == 'A':
                Neededfuel = 1
                location = (row, column, Neededfuel)
                return location
            elif map[i][j] == 'B':
                Neededfuel = 2
                location = (row, column, Neededfuel)
                return location
            elif map[i][j] == 'C':
                Neededfuel = 3
                location = (row, column,Neededfuel)
                return location
            elif map[i][j] == 'D':
                Neededfuel = 4
                location = (row, column,Neededfuel)
                return location
            elif map[i][j] == 'E':
                Neededfuel = 5
                location = (row, column,Neededfuel)
                return location
            elif map[i][j] == 'F':
                Neededfuel = 6
                location = (row, column,Neededfuel)
                return location
            elif map[i][j] == 'G':
                Neededfuel = 7
                location = (row, column,Neededfuel)
                return location
            elif map[i][j] == 'H':
                Neededfuel = 8
                location = (row, column,Neededfuel)
                return location
            elif map[i][j] == 'I':
                Neededfuel = 9
                location = (row, column,Neededfuel)
                return location
            else:
                print "Can not find an airplane!"
            #return location
def findGoal(map):
    row = len(map)
    for i in range(0,row):
        for j in range(0,len(map[i])):
            if map[i][j] == 'P':
                goalLoc = (i,j)
                print goalLoc
                return goalLoc

def getCurrentLocation():
    pass

def goUp(currentLocation):
    pass




def A_starSearch():
    pass











print "heuristic = " + heuristic
print "fuel = " + fuel
print "weatherInfo = " + weatherInfo
weather = buildMap(weatherInfo)
row = 0
print "map[row]\n" ,weather[row]
print weather[1]

drawMap(weather)
goal = findGoal(weather)


print "Len map", len(map)
print "Len map[row = 0]", len(map[1])
#location = findAirPlane(map)

''''
str = "2"
print str.isdigit()
str1 = 'A'
print str1.isdigit()
'''
print "end"