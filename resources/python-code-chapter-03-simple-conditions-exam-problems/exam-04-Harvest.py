import math

vineyard_area = int(input())
grape_per_square = float(input())
needed_liters = int(input())
workers = int(input())

harvest_per_vine = (vineyard_area * grape_per_square) * 0.4
vine = harvest_per_vine / 2.5

if vine >= needed_liters:
    vine_left = vine - needed_liters
    print('Good harvest this year! Total wine: {0} liters.' . format(
        math.floor(vine)))
    print('{0} liters left -> {1} liters per person.' . format(
        math.ceil(vine_left), math.ceil(vine_left / workers)))
else:
    print('It will be a tough winter! More {0} liters wine needed.'.format(
        math.floor(needed_liters - vine)))

