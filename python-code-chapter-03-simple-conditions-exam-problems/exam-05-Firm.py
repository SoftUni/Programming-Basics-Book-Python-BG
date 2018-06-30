import math

projectHours = int(input())
availableDays = int(input())
overtimeWorkers = int(input())

workDays = availableDays * 0.90
overtimeHours = workDays * 2 * overtimeWorkers
workHours = workDays * 8 * overtimeWorkers
totalHours = math.floor(workHours + overtimeHours)

if projectHours <= totalHours:
    print('Yes!{0} hours left.' . format(
        totalHours - projectHours))
else:
    print('Not enough time!{0} hours needed.' . format(
        projectHours - totalHours))