import math

#05.Firm-01
projectHours = int(input())
availableDays = int(input())
overtimeWorkers = int(input())

#05.Firm-02
workDays = availableDays * 0.90
overtimeHours = availableDays * 2 * overtimeWorkers
workHours = math.floor(workDays*8 + overtimeHours)

#05.Firm-03
if projectHours <= workHours:
    print('Yes!{0} hours left.' . format(
        workHours - projectHours))
else:
    print('Not enough time!{0} hours needed.' . format(
        projectHours - workHours))