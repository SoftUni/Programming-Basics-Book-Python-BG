import math

#03.Sleepy-tom-cat-01
holidays = int(input())

#03.Sleepy-tom-cat-02
workingDays = 365 - holidays

#03.Sleepy-tom-cat-03
totalPlayMinutes = workingDays*63 + holidays*127

#03.Sleepy-tom-cat-04
difference = math.fabs(totalPlayMinutes-30000)
hours = int(difference // 60)
minutes = int(difference % 60)

#03.Sleepy-tom-cat-05
if totalPlayMinutes > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')



