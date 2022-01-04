def add_time(start, duration, day=""):
    [start_time, start_end] = start.split()

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    [start_hour, start_minute] = start_time.split(":")
    [duration_hour, duration_minute] = duration.split(":")

    new_hour = int(start_hour) + int(duration_hour)
    new_minute = int(start_minute) + int(duration_minute)

    new_end = start_end

    if new_minute >= 60:
        new_hour = new_hour + 1
        new_minute = new_minute - 60

    day_counter = 0
    while new_hour >= 12:
        new_hour = new_hour - 12
        if new_end == "AM":
            new_end = "PM"
        else:
            new_end = "AM"
            day_counter = day_counter + 1
    
    if new_hour == 0:
        new_hour = 12

    new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + new_end

    count = 0
    num = 0
    if day != "":
        for days in weekdays:
            if day.lower() == days.lower():
                num = count
            count = count + 1

        num = num + day_counter

        while num >= 7:
            num = num - 7

        new_time = new_time + ", " + weekdays[num]

    if day_counter == 1:
        new_time = new_time + " (next day)"
    if day_counter > 1:
        new_time = new_time + " (" + str(day_counter) + " days later) "

    return new_time