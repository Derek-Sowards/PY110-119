'''
Understand the problem:
input = string in 24 hour format '12:37'
output = integer
explicit: return an integer of minutes before/after midnight. two functions

Examples/Test Cases
Data structure
Algorithm

after_midnight(string)
hours = int(str[:2])
minutes = int(str[3:])
return hours + minutes

before_midngith(string)
find hours
find minutes
return total hours in a day - (hour + minutes)

'''

MINUTES_PER_DAY = 1440

def after_midnight(string):
    hours = int(string[:2]) * 60
    minutes = int(string[3:])
    total_minutes = hours + minutes
    if total_minutes == MINUTES_PER_DAY:
        return 0
    return total_minutes

def before_midnight(string):
    hours = int(string[:2]) * 60
    minutes = int(string[3:])
    total_minutes = hours + minutes
    if total_minutes > 0:
        return MINUTES_PER_DAY - total_minutes
    return total_minutes


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True