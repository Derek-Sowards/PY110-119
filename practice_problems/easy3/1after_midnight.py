'''
Understand the Problem
input: integer representing number of minutes (3)
output: string in time format 'hh:mm' '00:03'
explicit: if number is positive, the time is after midnight
    if number is negative, the time is before midnight
implicit: 60 minutes in an hour
            24 hour time format

Examples/test cases:

Data structure:
function

Algorithm:
    hours per day = 24
    minutes per hour = 60
    minutes per day = hours per day * minutes per hour

    find_hours is taking the absolute value of number and // 60
    find_minutes is taking abs value / 60 subtract find_hours
    if number is negative,
        countdown from 24:00
    if number is positive,
        start at 00:00 and count up to 24:00

    format_number function(hours, minutes)
'''
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def time_of_day(minutes_input):
    remaining_minutes = minutes_input % MINUTES_PER_DAY

    if remaining_minutes < 0:
        remaining_minutes += MINUTES_PER_DAY
    
    hours = remaining_minutes // MINUTES_PER_HOUR
    minutes = remaining_minutes % MINUTES_PER_HOUR

    return format_time(hours, minutes)
def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True