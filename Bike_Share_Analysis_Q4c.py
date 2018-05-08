## Use this and additional cells to answer Question 4c. If you have    ##
## not done so yet, consider revising some of your previous code to    ##
## make use of functions for reusability.                              ##
##                                                                     ##
## TIP: For the Bay Area example data, you should find the average     ##
## Subscriber trip duration to be 9.5 minutes and the average Customer ##
## trip duration to be 54.6 minutes. Do the other cities have this     ##
## level of difference?                                                ##

## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.

from Bike_Share_Analysis_Q4b import get_average

def trip_average_by_ridertype(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """    
    
    with open(filename, 'r') as f_in:
        # set up csv reader object
        trip_reader = csv.DictReader(f_in)
        
        # initialize count variables
        n_subscriber_durations = []
        n_customer_durations = []
        
        # tally up ride types
        for row in trip_reader:
            trip_duration = float(row ['duration'])
            if row['user_type'] == 'Subscriber':
                n_subscriber_durations.append(trip_duration)
            else:
                n_customer_durations.append(trip_duration)
        
        
        n_subscribers, n_subscriber_average = get_average(n_subscriber_durations)
        n_customers, n_customer_average = get_average(n_customer_durations)
        
        return(n_subscribers, n_subscriber_average, n_customers, n_customer_average)
        

city_info = {'Washington':'./data/Washington-2016-Summary.csv',
             'Chicago': './data/Chicago-2016-Summary.csv',
             'NYC': './data/NYC-2016-Summary.csv'}
for city, data_file in city_info.items():    
    n_subscribers, n_subscriber_average, n_customers, n_customer_average = trip_average_by_ridertype(data_file)
    print ("City: {0} ".format(city))
    print ("Subscribers: {0}".format(n_subscribers))
    print ("Average trip length - Subscribers: {0}".format(n_subscriber_average))
    print ("Customers: {0}".format(n_customers))
    print ("Average trip length - Customers: {0}".format(n_customer_average))
    print ()
    
