# importing the dateteime module to display the date and the time
from datetime import datetime

#.now() returns the present date and time
at_the_moment = datetime.now()
print(at_the_moment)

#we can use strftime to set the format of the time
dt_string = at_the_moment.strftime("%Y/%m/%d %H:%M:%S")