import random


class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail-nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if(totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return result, totalValue


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print('   ', item)


def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, "calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.density)


def testMaxVal(foods, maxUnits, printItems=True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items = ', val)
    if printItems:
        for item in taken:
            print('   ', item)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

# testGreedys(foods, 750)
# print('')
# testMaxVal(foods, 750)


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items


# for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
#     print('Try a menu with', numItems, 'items')
#     items = buildLargeMenu(numItems, 90, 250)
#     testMaxVal(items, 750, False)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# for i in range(121):
#     print('fib(' + str(i) + ') = ', fib(i))


def fastFib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


# for i in range(121):
#     print('fib(' + str(i) + ') = ', fastFib(i))


def fastMaxVal(toConsider, avail, memo={}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[len(toConsider), avail] = result
    return result


def testMaxVal2(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = algorithm(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)


for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal2(items, 750, fastMaxVal, False)


