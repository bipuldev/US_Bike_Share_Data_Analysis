from Bike_Share_Analysis_Q2 import *

def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    
    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds. 
    
    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """       
    # YOUR CODE HERE
    duration =0    
    if city == 'NYC':
        duration = float(datum['tripduration'])        
    elif city == 'Chicago':
        duration = float(datum['tripduration'])
    elif city == 'Washington':
        duration = float(datum['Duration (ms)'])/1000
    
    duration = round(duration/60,4)
    
    return duration


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}

for city in tests:
    #print(duration_in_mins(example_trips[city], city))
    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001

def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    
    Remember that NYC includes seconds, while Washington and Chicago do not.
    
    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    
    # YOUR CODE HERE
    trip_start_time = None
    month = None
    hour = None
    day_of_week = None
    if city == 'NYC':
        trip_start_time = datetime.strptime(datum['starttime'], '%m/%d/%Y %H:%M:%S')   
    elif city == 'Chicago':
        trip_start_time = trip_start_time = datetime.strptime(datum['starttime'], '%m/%d/%Y %H:%M')
    elif city == 'Washington':
        trip_start_time = datetime.strptime(datum['Start date'], '%m/%d/%Y %H:%M')

    if trip_start_time != None:
        month = trip_start_time.month
        hour = trip_start_time.hour
        day_of_week = trip_start_time.strftime('%A')    

    #print ("city: {0}, month: {1}, hour: {2}, day_of_week: {3}".format(city,month, hour, day_of_week))    
    return (month, hour, day_of_week)


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

for city in tests:
    assert time_of_trip(example_trips[city], city) == tests[city]

def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.
    
    Remember that Washington has different category names compared to Chicago
    and NYC. 
    """
    
    # YOUR CODE HERE    
    user_type =""
    if city != 'Washington':
        user_type = datum['usertype']
    else:
        if datum['Member Type'] == 'Registered':
            user_type = 'Subscriber'
        else:
            user_type = 'Customer'
    #print ("city: {0}, user_type: {1}".format(city, user_type))
            
    return user_type


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 'Customer',
         'Chicago': 'Subscriber',
         'Washington': 'Subscriber'}

for city in tests:
    assert type_of_user(example_trips[city], city) == tests[city]


