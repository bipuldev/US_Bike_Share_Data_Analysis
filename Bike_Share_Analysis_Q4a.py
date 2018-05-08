## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.
def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """    
    
    with open(filename, 'r') as f_in:
        # set up csv reader object
        trip_reader = csv.DictReader(f_in)
        
        # initialize count variables
        n_subscribers = 0
        n_customers = 0
        
        # tally up ride types
        for row in trip_reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
            else:
                n_customers += 1
        
        # compute total number of rides
        n_total = n_subscribers + n_customers
        
        # return tallies as a tuple
        return(n_subscribers, n_customers, n_total)
        

## Modify this and the previous cell to answer Question 4a. Remember to run ##
## the function on the cleaned data files you created from Question 3.      ##

#data_file = './data/NYC-2016-Summary.csv'
city_info = {'Washington':'./data/Washington-2016-Summary.csv',
             'Chicago': './data/Chicago-2016-Summary.csv',
             'NYC': './data/NYC-2016-Summary.csv'}
for city, data_file in city_info.items():    
    n_subscribers, n_customers, n_total = number_of_trips(data_file)
    n_proportion_subscribers = round(n_subscribers/n_total, 4)
    n_proportion_customers = round(n_customers/n_total,4)
    print ("City: {0} ".format(city))
    print ("Subscribers: {0}".format(n_subscribers))
    print ("Customers: {0}".format(n_customers))
    print ("Total Trips: {0}".format(n_total))
    print ("Subscriber proportion: {0}".format(n_proportion_subscribers))
    print ("Customer proportion: {0}".format(n_proportion_customers))
    print ()
    
