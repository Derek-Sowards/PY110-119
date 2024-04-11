'''
Understand the problem
input- integer (year)
output- integer (# of friday the 13ths in the input year)
explicit:
-year will always be greater than 1972
-assume gregorian calendar will remain in use indefinitely
implicit:

examples/ test cases:

data structure
counter
for loops

algorithm:
Iterate over all the months of the given year.
For each month, get the day that falls on the 13th.
Count the 13ths that fall on a Friday.
Return the count.
'''
import datetime

def friday_the_13ths(year):
    thirteenths = [datetime.date(year, month, 13) for month in range(1, 13)]

    count = 0
    for day in thirteenths:
        if day.weekday() == 4:
            count += 1
    return count


print(friday_the_13ths(1986))      # 1
print(friday_the_13ths(2015))     # 3
print(friday_the_13ths(2017))     # 2