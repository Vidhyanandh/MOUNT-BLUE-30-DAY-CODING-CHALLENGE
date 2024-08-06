#Approach - 1

def timeConversion(s):
    Am_pm = s[-2:]
    hour = s[:2]
    mins = s[2:8]
    hour_time = int(hour)
    
    if Am_pm == "AM":
        if hour_time == 12:
            hour = "00"
    else: 
        if hour_time != 12:
            hour_time += 12
            hour = str(hour_time)
    
    return hour + mins


#Approach - 2
def timeConversion(s):
    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]
    period = s[-2:]
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    hour = str(hour) if hour >= 10 else '0' + str(hour)
    return hour + ':' + minute + ':' + second
