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
