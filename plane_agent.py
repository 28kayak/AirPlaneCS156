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
    manhattanDis = abs(i1-i2) + abs(j1-j2)
    return manhattanDis
def fuelDistance():
    pass



def findAirPlane(mapm):
    """
    Find a starting point and return its location
    :param mapm:
    :return location: location contains (x,y,fuel needed to go to the next box)
    """
    row = len(mapm)

    for i in range(0,row):

        print mapm[i]
        column = len(mapm[i])
        for j in range(0, column):
            if mapm[i][j] == 'A':
                Neededfuel = 1
                location = (i, j, Neededfuel)
                return location
            elif mapm[i][j] == 'B':
                Neededfuel = 2
                location = (i, j, Neededfuel)
                return location
            elif mapm[i][j] == 'C':
                Neededfuel = 3
                location = (i, j,Neededfuel)
                return location
            elif mapm[i][j] == 'D':
                Neededfuel = 4
                location = (i, j,Neededfuel)
                return location
            elif mapm[i][j] == 'E':
                Neededfuel = 5
                location = (i, j,Neededfuel)
                return location
            elif mapm[i][j] == 'F':
                Neededfuel = 6
                location = (i, j,Neededfuel)
                return location
            elif mapm[i][j] == 'G':
                Neededfuel = 7
                location = (i, j,Neededfuel)
                return location
            elif mapm[i][j] == 'H':
                Neededfuel = 8
                location = (i, j,Neededfuel)
                return location
            elif mapm[i][j] == 'I':
                Neededfuel = 9
                location = (i, j,Neededfuel)
                return location
            else:
                print "Can not find an airplane!"
            #return location
def findGoal(mapm):
    row = len(mapm)
    for i in range(0,row):
        for j in range(0,len(mapm[i])):
            if mapm[i][j] == 'P':
                goalLoc = (i,j)
                return goalLoc



def getNext(mapm,dist,cI,cJ,gI,gJ, sI, sJ):

    minv=10000
    upI=cI-1
    upJ=cJ
    downI=cI+1
    downJ=cJ
    rightI=cI
    rightJ=cJ+1
    leftI=cI
    leftJ=cJ-1

    # measure h(n) = distance between next location and goal, plus c(n) = distance between starting point and goal.
    #Form here, start A*search such that A*search = h(n) + c(n)
    upD=dist(upI,upJ,goalI,goalJ) + dist(sI, sJ, gI, gJ)
    downD=dist(downI,downJ,goalI,goalJ) + dist(sI, sJ, gI, gJ)
    rightD=dist(rightI,rightJ,goalI,goalJ) + dist(sI, sJ, gI, gJ)
    leftD=dist(leftI,leftJ,goalI,goalJ) + dist(sI, sJ, gI, gJ)

    fuelUpD = mapm[upI][upJ]
    fuelDownD = mapm[downI][downJ]
    fuelRightD = mapm[rightI][rightJ]
    fuelLeftD = mapm[leftI][leftJ]
    upD += fuelUpD
    downD += fuelDownD
    rightD += fuelRightD
    leftD += fuelLeftD



    if (upD < minv):
        minv=upD
        nextI=upI
        nextJ=upJ

    if (downD<minv):
        minv=downD
        nextI=downI
        nextJ=downJ
    if (rightD<minv):
        minv=rightD
        nextI=rightI
        nextJ=rightJ
    if (leftD<minv):
        minv=leftD
        nextI=leftI
        nextJ=leftJ
    print "NEXT", nextI,nextJ
    return (nextI,nextJ,minv)

def changemap(mapm,ci,cj,ni,nj):
    if (mapm[ni][nj]=='1'):
        mapm[ni][nj]='A'
    if (mapm[ni][nj]=='2'):
        mapm[ni][nj]='B'
    if (mapm[ni][nj]=='3'):
        mapm[ni][nj]='C'
    if (mapm[ni][nj]=='4'):
        mapm[ni][nj]='D'
    if (mapm[ni][nj]=='5'):
        mapm[ni][nj]='E'
    if (mapm[ni][nj]=='6'):
        mapm[ni][nj]='F'
    if (mapm[ni][nj]=='7'):
        mapm[ni][nj]='G'
    if (mapm[ni][nj]=='8'):
        mapm[ni][nj]='H'
    if (mapm[ni][nj]=='9'):
        mapm[ni][nj]='I'
    if (mapm[ni][nj]=='P'):
        mapm[ni][nj]='J'

    if (mapm[ci][cj]=='A'):
        mapm[ci][cj]='1'
    if (mapm[ci][cj]=='B'):
        mapm[ci][cj]='2'
    if (mapm[ci][cj]=='C'):
        mapm[ci][cj]='3'
    if (mapm[ci][cj]=='D'):
        mapm[ci][cj]='4'
    if (mapm[ci][cj]=='E'):
        mapm[ci][cj]='5'
    if (mapm[ci][cj]=='F'):
        mapm[ci][cj]='6'
    if (mapm[ci][cj]=='G'):
        mapm[ci][cj]='7'
    if (mapm[ci][cj]=='H'):
        mapm[ci][cj]='8'
    if (mapm[ci][cj]=='I'):
        mapm[ci][cj]='9'




def moveLoc(mapm,cI,cJ,nextI,nextJ):
    changemap(mapm,cI,cJ,nextI,nextJ)
    cI=nextI
    cJ=nextJ
    return (cI,cJ)

def isGoal(location):
    if location == 'P':
        return True
    else:
        return False


print "heuristic = " + heuristic
print "fuel = " + fuel
print "weatherInfo = " + weatherInfo
weather = buildMap(weatherInfo)
row = 0
print "map[row]\n" ,weather[row]
print weather[1]

drawMap(weather)
goal = findGoal(weather)
print goal
goalI=goal[0]
goalJ=goal[1]

print weather
print "Len map", len(weather)
print "Len map[row = 0]", len(weather[1])
#location = findAirPlane(map)
startLoc=findAirPlane(weather)
print startLoc

counter=0
currentLoc=startLoc
#caliculate Up,Down,RIght,Left
cI=startLoc[0]
cJ=startLoc[1]

global sI
sI =startLoc[0]
global sJ
sJ = startLoc[1]
print "START", cI,cJ


(nextI,nextJ,fuelneeded)=getNext(manhattan, cI,cJ,goalI,goalJ, sI, sJ)
(cI,cJ)=moveLoc(weather,cI,cJ,nextI,nextJ)
counter=counter+1
print "MAP ",counter, weather


(nextI,nextJ,fuelneeded)=getNext(manhattan, cI,cJ,goalI,goalJ,sI,sJ)
(cI,cJ)=moveLoc(weather,cI,cJ,nextI,nextJ)
counter=counter+1
print "MAP ",counter, weather

(nextI,nextJ,fuelneeded)=getNext(manhattan, cI,cJ,goalI,goalJ, sI,sJ)
(cI,cJ)=moveLoc(weather,cI,cJ,nextI,nextJ)
counter=counter+1
print "MAP ",counter, weather

(nextI,nextJ,fuelneeded)=getNext(manhattan, cI,cJ,goalI,goalJ,sI,sJ)
(cI,cJ)=moveLoc(weather,cI,cJ,nextI,nextJ)
counter=counter+1
print "MAP ",counter, weather

(nextI,nextJ,fuelneeded)=getNext(manhattan, cI,cJ,goalI,goalJ,sI,sJ)
(cI,cJ)=moveLoc(weather,cI,cJ,nextI,nextJ)
counter=counter+1
print "MAP ",counter, weather

while fuel >= 0 and isGoal(currentLoc) != True:
    (nextI,nextJ,fuelneeded)=getNext(manhattan, cI,cJ,goalI,goalJ,sI,sJ)
    (cI,cJ)=moveLoc(weather,cI,cJ,nextI,nextJ)
    counter=counter+1
    print "MAP ",counter, drawMap(weather)











''''
print startLoc
str = "2"
print str.isdigit()
str1 = 'A'
print str1.isdigit()
c(n) = distance between starting point and
'''
print "end"