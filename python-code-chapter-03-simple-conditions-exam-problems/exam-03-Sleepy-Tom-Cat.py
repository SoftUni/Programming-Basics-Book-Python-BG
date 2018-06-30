import math

holidays = int(input())

workingDays = 365 - holidays
totalPlayMinutes = workingDays*63 + holidays*127
difference = math.fabs(totalPlayMinutes-30000)
hours = int(difference // 60)
minutes = int(difference % 60)

if totalPlayMinutes > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')



