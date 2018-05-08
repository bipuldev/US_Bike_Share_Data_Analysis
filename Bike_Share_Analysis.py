## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.

def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
        trip_reader =csv.DictReader(f_in)
        
        start_time =""
        if "starttime" in trip_reader.fieldnames:
            start_time="starttime"
        else:
            start_time="Start date"
        
        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##
        first_trip= None        
        for reader in trip_reader:
            if first_trip == None:
                first_trip = reader
            else:
                first_trip_date=convert_todate(first_trip[start_time])
                current_record_date = convert_todate(reader[start_time])
                if current_record_date < first_trip_date:
                    first_trip = reader
            
        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)
    # output city name and first trip for later testing
    return (city, first_trip)

def convert_todate(str_dt):
    """
    This function takes string and returns date
    """    
    list_dt = str_dt.split(" ")
    list_dt[-1] = (list_dt[-1] + ":00")[:8]
    str_dt = " ".join(list_dt)    
    return datetime.strptime(str_dt, "%m/%d/%Y %H:%M:%S")

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
example_trips = {}

for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    #print (first_trip)

    example_trips[city] = first_trip

