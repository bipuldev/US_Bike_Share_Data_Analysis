## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.
import matplotlib.pyplot as plt

def get_days():
    """
    This function returns dictionary of days
    """    
    days = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7}
    return days

def get_average(data_list):
    """
    This function calculates the average from a list of values
    """
    return len(data_list),round(sum(data_list) / len(data_list), 4)

def get_overtime_proportion(data_list):
    """
    This funtion calculate proportion of durtions greater than 30 minutes
    """
    n_total_30 = 0
    for duration in data_list:
        if duration > 30:
            n_total_30 += 1
    return round(n_total_30/len(data_list), 4)
    

def trip_day_stats(filename, usertype=None):
    """
    This function reads in a file with trip data and reports average duration
    and proportion of trip longer than 30 mins.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        trip_reader = csv.DictReader(f_in)
        n_durations_weekend =[]
        n_durations_weekday =[]
        days= get_days()
                
        for row in trip_reader:
            trip_duration = float(row ['duration'])
            if usertype:                
                if row['user_type'] == usertype:                    
                    if row['day_of_week'] in list(days.keys())[-2:]:
                        n_durations_weekend.append(trip_duration)
                    else:
                        n_durations_weekday.append(trip_duration)                                
            else:
                if row['day_of_week'] in list(days.keys())[-2:]:
                    n_durations_weekend.append(trip_duration)
                else:
                    n_durations_weekday.append(trip_duration)
        
        n_total_weekend, n_average_weekend = get_average(n_durations_weekend)
        n_total_weekday, n_average_weekday = get_average(n_durations_weekday)

        n_proportion_30_weekend = get_overtime_proportion(n_durations_weekend)
        n_proportion_30_weekday = get_overtime_proportion(n_durations_weekday)

        return n_total_weekend,n_average_weekend, n_proportion_30_weekend, n_total_weekday, \
            n_average_weekday, n_proportion_30_weekday

def trip_day_durations(filename, usertype=None):
    """
    This function reads in a file with trip data and reports average duration
    and proportion of trip longer than 30 mins.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        trip_reader = csv.DictReader(f_in)
        n_durations_weekend =[]
        n_durations_weekday =[]
        days= get_days()
                
        for row in trip_reader:
            trip_duration = float(row ['duration'])
            if usertype:                
                if row['user_type'] == usertype:                    
                    if row['day_of_week'] in list(days.keys())[-2:]:
                        n_durations_weekend.append(trip_duration)
                    else:
                        n_durations_weekday.append(trip_duration)                                
            else:
                if row['day_of_week'] in list(days.keys())[-2:]:
                    n_durations_weekend.append(trip_duration)
                else:
                    n_durations_weekday.append(trip_duration)
        
    return n_durations_weekend, n_durations_weekday


city_info = {'Washington':'./data/Washington-2016-Summary.csv',
             'Chicago': './data/Chicago-2016-Summary.csv',
             'NYC': './data/NYC-2016-Summary.csv'}

   
n_total_weekend,n_average_weekend, n_proportion_30_weekend, n_total_weekday, n_average_weekday, n_proportion_30_weekday \
    = trip_day_stats(city_info['Chicago'])

print ("City: {0} - Weekend Stats ".format('Chicago'))
print ("Total trips: {0}".format(n_total_weekend))
print ("Average trip length: {0}".format(n_average_weekend))
print ("Proportion over 30 mins: {0}".format(n_proportion_30_weekend))
print ()

print ("City: {0} - Weekdays Stats ".format('Chicago'))
print ("Total trips: {0}".format(n_total_weekday))
print ("Average trip length: {0}".format(n_average_weekday))
print ("Proportion over 30 mins: {0}".format(n_proportion_30_weekday))
print ()


n_total_weekend,n_average_weekend, n_proportion_30_weekend, n_total_weekday, n_average_weekday, n_proportion_30_weekday \
    = trip_day_stats(city_info['Chicago'], 'Subscriber')

print ("City: {0} - Weekend Stats (Subscribers)".format('Chicago'))
print ("Total trips: {0}".format(n_total_weekend))
print ("Average trip length: {0}".format(n_average_weekend))
print ("Proportion over 30 mins: {0}".format(n_proportion_30_weekend))
print ()

print ("City: {0} - Weekdays Stats (Subscribers)".format('Chicago'))
print ("Total trips: {0}".format(n_total_weekday))
print ("Average trip length: {0}".format(n_average_weekday))
print ("Proportion over 30 mins: {0}".format(n_proportion_30_weekday))
print ()

n_total_weekend,n_average_weekend, n_proportion_30_weekend, n_total_weekday, n_average_weekday, n_proportion_30_weekday \
    = trip_day_stats(city_info['Chicago'], 'Customer')

print ("City: {0} - Weekend Stats (Customers) ".format('Chicago'))
print ("Total trips: {0}".format(n_total_weekend))
print ("Average trip length: {0}".format(n_average_weekend))
print ("Proportion over 30 mins: {0}".format(n_proportion_30_weekend))
print ()

print ("City: {0} - Weekdays Stats ".format('Chicago'))
print ("Total trips: {0}".format(n_total_weekday))
print ("Average trip length: {0}".format(n_average_weekday))
print ("Proportion over 30 mins: {0}".format(n_proportion_30_weekday))
print ()


n_durations_weekend, n_durations_weekday = trip_day_durations (city_info ['Chicago'])

plt.hist(n_durations_weekend, bins=20, range=[0,100], density=False,facecolor='g',alpha=0.75)
plt.title('Distribution of Trip Durations on Weekends')
plt.xlabel('Duration (m)')
plt.ylabel('No of Trips')
plt.grid(True)
plt.show()

plt.hist(n_durations_weekday, bins=20, range=[0,100], density=False,facecolor='r',alpha=0.75)
plt.title('Distribution of Trip Durations on Weekdays')
plt.xlabel('Duration (m)')
plt.ylabel('No of Trips')
plt.grid(True)
plt.show()
