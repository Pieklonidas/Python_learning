import random
import pylab
import numpy as np
random.seed(0)


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Drunk(object):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self.name != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)


def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass):
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def drunkTest(walkLength, numTrials, dClass):
    mean = []
    length = []
    for numSteps in walkLength:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print('Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))
        mean.append(round(sum(distances) / len(distances), 4))
        length.append(numSteps)
    return mean, length

# drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)


def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        means, lengths = drunkTest(walkLengths, numTrials, dClass)
        pylab.plot(lengths, means, label=dClass.__name__)


simAll((UsualDrunk, MasochistDrunk), (1, 10, 100, 1000, 10000, 100000), 100)

pylab.grid()
pylab.title('Mean Distances from Origin (100 trials)')
pylab.xlabel('Numbers of steps')
pylab.ylabel('Distance from origin')

steps = np.array([1, 10, 100, 1000, 10000, 100000])
nSmzdz5 = steps*0.05
Sros = steps**0.5
pylab.plot(steps, nSmzdz5, 'm--', label='numSteps*0.05')
pylab.plot(steps, Sros, 'c--', label='Square roots of steps')
pylab.legend()
pylab.show()
