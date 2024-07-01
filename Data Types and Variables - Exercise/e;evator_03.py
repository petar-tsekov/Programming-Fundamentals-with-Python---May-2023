from math import ceil
people_qty = int(input())
elevator_capacity = int(input())

courses = people_qty / elevator_capacity


print(ceil(courses))