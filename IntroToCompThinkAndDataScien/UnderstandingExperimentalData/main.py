# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:45:20 2016

@author: johnguttag

Modified: egrimson
"""

import random, pylab, numpy

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers
pylab.rcParams['lines.markersize'] = 10
# set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1


def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)


def labelPlot(title, xlabel, ylabel):
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)


def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label='Measured displacements')


def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81
    pylab.plot(xVals, yVals, 'bo', label='Measured points')
    labelPlot('Measured Displacement of Spring', '|Force| (Newtons)', 'Distance (meters)')
    a, b, temp = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*pylab.array(xVals) + b
    print('a =', a, 'b =', b)
    pylab.plot(xVals, estYVals, 'r', label='Linear fit, k = ' + str(round(1/a, 5)))
    pylab.legend(loc = 'best')


# fitData('springData.txt')
# pylab.show()


def fitData1(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81
    pylab.plot(xVals, yVals, 'bo', label='Measured points')
    labelPlot('Measured Displacement of Spring', '|Force| (Newtons)', 'Distance (meters)')
    model = pylab.polyfit(xVals, yVals, 1)
    estYVals = pylab.polyval(model, xVals)
    pylab.plot(xVals, estYVals, 'r', label='Linear fit, k = ' + str(round(1/model[0], 5)))
    pylab.legend(loc='best')


# fitData1('springData.txt')
# pylab.show()

xVals, yVals = getData('mysteryData.txt')
pylab.plot(xVals, yVals, 'o', label='Data Points')
pylab.title('Mystery Data')

# Linear model
model1 = pylab.polyfit(xVals, yVals, 1)
# pylab.plot(xVals, pylab.polyval(model1, xVals), label='Linear Model')

# Quadratic model
model2 = pylab.polyfit(xVals, yVals, 2)
# pylab.plot(xVals, pylab.polyval(model2, xVals), 'r--', label='Quadratic Model')
# pylab.legend()
# pylab.show()


def aveMeanSquareError(data, predicted):
    error = 0.0
    for i in range(len(data)):
        error += (data[i] - predicted[i])**2
    return error/len(data)


estYVals = pylab.polyval(model1, xVals)
print('Ave. mean square error for linear model =', aveMeanSquareError(yVals, estYVals))
estYVals = pylab.polyval(model2, xVals)
print('Ave. mean square error for quadratic model =', aveMeanSquareError(yVals, estYVals))


def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed))


def genFits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        model = pylab.polyfit(xVals, yVals, d)
        models.append(model)
    return models


def testFits(models, degrees, xVals, yVals, title):
    pylab.plot(xVals, yVals, 'o', label='Data')
    for i in range(len(models)):
        estYVals = pylab.polyval(models[i], xVals)
        error = rSquared(yVals, estYVals)
        pylab.plot(xVals, estYVals, label='Fit of degree '\
                                          + str(degrees[i])\
                                          + ', R2 = '\
                                          + str(round(error, 5)))
        pylab.legend(loc='best')
        pylab.title(title)


xVals, yVals = getData('mysteryData.txt')
# degrees = (1, 2)
# models = genFits(xVals, yVals, degrees)
# testFits(models, degrees, xVals, yVals, 'Mystery Data')

degrees = (2, 4, 8, 16)
models = genFits(xVals, yVals, degrees)
testFits(models, degrees, xVals, yVals, 'Mystery Data')
pylab.show()


