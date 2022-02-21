import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITY_KEY = {'chicago':'Chicago',
            'new york city':'New York City',
            'washington':'Washington'}

CITY_DATA=dict((CITY_KEY[key], value) for (key, value) in CITY_DATA.items())


def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    cities = ['Chicago','New York City','Washington']

    while city not in cities:
        city = str(input('Which of these cities do you like to explore? Chicago, New York City or Washington \n \n')).title()
        if city not in cities:
            print ('\nWrong city, please try again entering one of these cities: Chicago, New York City or Washington')
        print('You have chosen: {}'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month=0
    months=[1,2,3,4,5,6,7]
    months_dict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'All': 7}

    list_of_key = list(months_dict.keys())
    list_of_value = list(months_dict.values())

    while month not in months:
        try:
            month = int(input('\n What month do you like to explore? Enter the integer according to the month:\n January = 1 \n February = 2 \n March = 3 \n April = 4 \n May = 5 \n June = 6 \n All = 7 \n \n'))
            if month not in months:
                print('Wrong month, please try again entering one of these months: 1,2,3,4,5,6,7')
        except:
            if month not in months:
                print ('Wrong month, please try again entering one of these months: 1,2,3,4,5,6,7')
    print('You have chosen: {}'.format(list_of_key[list_of_value.index(month)]))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    day_dict = {'Mond': 'Monday', 'Tues': 'Tuesday', 'Wed': 'Wednesday', 'Thurs': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday', 'All':'All'}
    
    while day not in day_dict.keys():
        day = str(input('Which day would you like to explore: Mond, Tues, Wed, Thurs, Fri, Sat, Sun, All \n')).title()
        if day not in day_dict.keys():
            print ('Wrong day, please try again entering one of these days: Mond, Tues, Wed, Thurs, Fri, Sat, Sun, All')
    day = day_dict[day]
    print('You have chosen: {}'.format(day))

    print('Filter done')
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_week'] = df['Start Time'].dt.weekday_name
    if month != 7:
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_week'] == day]

    return df

def see_lines(df):
    lines = ['Yes', 'No']
    response = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    row = 0
    while response not in lines:
        print("\nDo you like to view the structure of the data? Answer Yes or No\n")
        response = input().title()
        if response not in lines:
            print('\nIncorrect input, enter Yes or No\n')
        elif response == 'Yes':
            print(df.head(5))
            while True:
                response_yes = input('Do yo like to view more data? Answer Yes or No\n').title()
                if response_yes not in lines:
                    print('\nIncorrect input, enter Yes or No')
                elif response_yes == 'Yes':
                    row += 5
                    print(df[row:row+5])
                elif response_yes == 'No':
                    print('\nLets see statistics ...')
                    return
        elif response == 'No':
            print('\nLets see statistics ...')
            return
    return

            
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    print('Most common month:{}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_week'].mode()[0]

    print('\nMost Popular Day:{}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]

    print('\nMost common Start Hour: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:{}'.format(most_common_start_station))
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    print('\nThe most common end station is:{}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'].str.cat(df['End Station'], sep=' / ')
    Combination_trip = df['Start_End'].mode()[0]

    print('\nThe most frequent combination of trips is: {}'.format(Combination_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time: {}'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean(),2)
    print('The mean travel time: {}'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()

    print('The types of users are:\n {}'.format(counts_user_types))

    # TO DO: Display counts of gender
    try:
        counts_gender = df['Gender'].value_counts()
        print('\nThe types of gender are:\n {}'.format(counts_gender))
    except:
        print('The data for this city has no column GENDER')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('\nThe earliest year of birth is: {}'.format(earliest_year), '\nThe most recent year of birth is: {}'.format(recent_year),'\nThe most common year of birth is: {}'.format(common_year))
    except:
        print('The data for this city has no Birth Year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        see_lines(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
