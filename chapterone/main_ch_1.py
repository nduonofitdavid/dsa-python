import time, datetime

# automatic packing in python

data: tuple = 1, 2, 3, 4, 5
print(type(data))


# get the current time in a unix timestamp format
time_ = time.time()
print(time_)

# convert that unix timestamp to a date, the time in milliseconds or the minutes, any information about the time can be used 
# as a seed for the random number generation.
date = datetime.datetime.fromtimestamp(time_)
print(date.minute)
print(date.second)
print(date.hour)
print(date.microsecond)

