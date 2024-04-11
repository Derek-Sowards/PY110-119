'''
Understand the Problem
    input - floating point number representing angle (0 - 360) (40.53)
    output - string representing angle in degrees, minutes, seconds ("30°00'00\"")
    explicit - degrees use °, minutes use ', seconds use "
        60 minutes in a degree, 60 seconds in a minute
    implicit -
    questions - What if degree is 0? 1 degree is 1 hour

Examples/test cases
whole number before decimal is degrees
number after decimal is num / 60 is minutes
remainder after that is num / 60 is seconds

Data structure
    function
    string concatenation

algorithm
    create an empty string to return
    use floor division to find degrees and append to empty string
    use num % 1 to find number after decimal
        take that number and divide it by 60 to find minutes
            take the remainder and divide it by 60 to find the seconds

'''
def dms(num):
    if num == 0:
        degrees = num
        minutes = 0
        seconds = 0
    else:
        degrees = num // 1
        minutes = (num - degrees) * 60
        seconds = (minutes - int(minutes)) * 60
    return f"{int(degrees)}°{pad_float(int(minutes))}'{pad_float(int(seconds))}\""

def pad_float(num):
    num_string = str(num)
    if len(num_string) < 2:
        return '0' + num_string
    else:
        return num_string


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")