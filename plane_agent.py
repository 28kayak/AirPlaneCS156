__author__ = 'kaya'
import sys

argvs = sys.argv
argc = len(argvs) # length will return the number of arguments
#including the python file.
# store information from arguments "python plane_agent.py weather.txt euclidean 7"
weatherInfo = argvs[1]
heuristic = argvs[2]
fuel = argvs[3]


def buildMap(weatherInfo):
    #read input file and build approriate multi-dimentional array
    f = open(weatherInfo)
    line = f.readline()
    #column = len(line)
    #print 'length = ' + str(column)
    while line:
        print line, "\nlength = " + str(len(line))
        line = f.readline()
    f.close()
    map= [[0 for x in range(5)] for x in range(5)]


print "heuristic = " + heuristic
print "fuel = " + fuel
print "weatherInfo = " + weatherInfo
buildMap(weatherInfo)