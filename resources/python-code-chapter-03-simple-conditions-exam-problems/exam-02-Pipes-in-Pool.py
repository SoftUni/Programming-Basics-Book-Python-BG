import math

volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

water = (pipe_1 + pipe_2) * hours

if water <= volume:
    print('The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.' . format(
        math.trunc(water/volume * 100),
        math.trunc(pipe_1 * hours / water * 100),
        math.trunc(pipe_2 * hours / water * 100)
    ))
else:
    print('For {0} hours the pool overflows with {1} liters.' . format(
        hours,
        water - volume
    ))
