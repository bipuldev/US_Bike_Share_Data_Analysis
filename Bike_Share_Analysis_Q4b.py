## Use this and additional cells to answer Question 4b.                 ##
##                                                                      ##
## HINT: The csv module reads in all of the data as strings, including  ##
## numeric values. You will need a function to convert the strings      ##
## into an appropriate numeric type before you aggregate data.          ##
## TIP: For the Bay Area example, the average trip length is 14 minutes ##
## and 3.5% of trips are longer than 30 minutes.                        ##

## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.

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
    
def trip_overtime_proportion(filename):
    """
    This function reads in a file with trip data and reports average duration
    and proportion of trip longer than 30 mins.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        trip_reader = csv.DictReader(f_in)
        n_durations =[]
        n_total_30 = 0
        for row in trip_reader:
            trip_duration = float(row ['duration'])
            n_durations.append(trip_duration)
            if trip_duration > 30:
                n_total_30 += 1       
        
        n_total, n_average = get_average(n_durations)

        n_proportion_30 = get_overtime_proportion(n_durations)

        return n_total,n_average, n_proportion_30
    
city_info = {'Washington':'./data/Washington-2016-Summary.csv',
             'Chicago': './data/Chicago-2016-Summary.csv',
             'NYC': './data/NYC-2016-Summary.csv'}
for city, data_file in city_info.items():    
    n_total, n_average, n_proportion_30 = trip_overtime_proportion(data_file)

    print ("City: {0} ".format(city))
    print ("Total trips: {0}".format(n_total))
    print ("Average trip length: {0}".format(n_average))
    print ("Proportion over 30 mins: {0}".format(n_proportion_30))
    print ()
