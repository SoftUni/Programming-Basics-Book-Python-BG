import math

#02.Pipes-in-pool-01
volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

#02.Pipes-in-pool-02
water = (pipe1+pipe2) * hours

#02.Pipes-in-pool-03
if water <= volume:
    print('The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.' . format(
        math.trunc(water/volume * 100),
        math.trunc(pipe1*hours/water * 100),
        math.trunc(pipe2*hours/ water * 100)
    ))
else:
    print('For {0} hours the pool overflows with {1} liters.' . format(
        hours,
        water - volume
    ))
