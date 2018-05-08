# load library
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function
import matplotlib.pyplot as plt

# this is a 'magic word' that allows for plots to be displayed
# inline with the notebook. If you want to know more, see:
# http://ipython.readthedocs.io/en/stable/interactive/magics.html
#%matplotlib inline 

# example histogram, data taken from bay area sample
#data = [ 7.65,  8.92,  7.42,  5.50, 16.17,  4.20,  8.98,  9.62, 11.48, 14.33,
#        19.02, 21.53,  3.90,  7.97,  2.62,  2.67,  3.08, 14.40, 12.90,  7.83,
#        25.12,  8.30,  4.93, 12.43, 10.60,  6.17, 10.88,  4.78, 15.15,  3.53,
#         9.43, 13.32, 11.72,  9.85,  5.22, 15.10,  3.95,  3.17,  8.78,  1.88,
#         4.55, 12.68, 12.38,  9.78,  7.63,  6.45, 17.38, 11.90, 11.52,  8.63,]
#plt.hist(data)
#plt.title('Distribution of Trip Durations')
#plt.xlabel('Duration (m)')
#plt.show()

def trip_durations(filename, usertype=None, limit =None):
    """
    This function reads in a file with trip data and returns durations in list
    """    
    n_durations = []
    with open(filename, 'r') as f_in:
        # set up csv reader object
        trip_reader = csv.DictReader(f_in)
                 
        for row in trip_reader:
            trip_duration = float(row ['duration'])
            if usertype:
                if row['user_type'] == usertype:
                    if limit:
                        if trip_duration <= limit:
                            n_durations.append(trip_duration)
                    else:
                         n_durations.append(trip_duration)
            else:
                if limit:
                    if trip_duration <= limit:
                        n_durations.append(trip_duration)
                else:
                    n_durations.append(trip_duration)
    return n_durations

city_info = {'Washington':'./data/Washington-2016-Summary.csv',
             'Chicago': './data/Chicago-2016-Summary.csv',
             'NYC': './data/NYC-2016-Summary.csv'}

n_durations = trip_durations(city_info ['Washington'])
plt.hist(n_durations, bins=20, range=[0,100], density=False,facecolor='g',alpha=0.75)
plt.title('Distribution of Trip Durations (Washington)')
plt.xlabel('Duration (m)')
plt.ylabel('No of Trips')
plt.grid(True)
plt.show()


