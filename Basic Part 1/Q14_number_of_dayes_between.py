# Q. To calculate the number of days between 2 dates

# importing the datetime module
from datetime import date

#converting the tuple to date date(yyyy, mm, dd)
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

#Calculating the days between
days_between = date2 - date1
print(days_between)
