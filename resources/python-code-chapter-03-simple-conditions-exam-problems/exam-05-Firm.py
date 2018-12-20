import math

project_hours = int(input())
available_days = int(input())
overtime_workers = int(input())

work_days = available_days * 0.90
overtime_hours = work_days * 2 * overtime_workers
work_hours = work_days * 8 * overtime_workers
total_hours = math.floor(work_hours + overtime_hours)

if project_hours <= total_hours:
    print('Yes!{0} hours left.' . format(
        total_hours - project_hours))
else:
    print('Not enough time!{0} hours needed.' . format(
        project_hours - total_hours))