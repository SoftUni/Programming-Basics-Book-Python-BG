import math

#04.Harvest-01
vineyardArea = int(input())
grapePerSquare = float(input())
neededLiters = int(input())
workers = int(input())

#04.Harvest-02
harvestPerVine = (vineyardArea * grapePerSquare) * 0.4
vine = harvestPerVine / 2.5

#04.Harvest-03
if vine >= neededLiters:
    vineLeft = vine - neededLiters
    print('Good harvest this year! Total wine: {0} liters.' . format(
        math.floor((vine))))
    print('{0} liters left -> {1} liters per person.' . format(
        math.ceil(vineLeft), math.ceil(vineLeft/workers)))
#04.Harvest-04
else:
    print('It will be a tough winter! More {0} liters wine needed.'.format(
        math.floor((neededLiters - vine))))

