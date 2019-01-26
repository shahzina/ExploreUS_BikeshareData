import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Enter your city: ').lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month=''
    while month not in ['all', 'january', 'february','march', 'april', 'may' , 'june']:
        month = input('Enter your month: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']:
        day = input('Enter your day of week: ').lower()

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['Day'] = df['Start Time'].dt.strftime('%A').str.lower()
    df['Hour'] = df['Start Time'].dt.strftime('%H')
    if day != 'all':
        df = df[df['Day'] == day]
        
    if month != 'all':
        df = df[df['Month'] == month]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df.groupby('Month').size().idxmax())

    # TO DO: display the most common day of week
    print(df.groupby('Day').size().idxmax())

    # TO DO: display the most common start hour
    print(df.groupby('Hour').size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df.groupby('Start Station').size().idxmax())

    # TO DO: display most commonly used end station
    print(df.groupby('End Station').size().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print(df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df.groupby('Trip Duration').size().idxmax())

    # TO DO: display mean travel time
    print(df.groupby('Trip Duration').mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    #print(df['Gender'].value_counts())
    
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print ('Gender info not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth year' in df:
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())
        print(df['Birth Year'].mode())
    else: 
        print('Birth year not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
            """Displays individual trip data on bikeshare users."""
            print('Displaying raw data from biking dataset .... \n')
            user_question = input('Would you like to view individual trip data? Enter yes or no:  \n').lower()
            x = 0
            y = 5
            if user_question == 'yes':
                print(df.iloc[x:y])     # this will display 5 records in chunks 
            while x < len(df.index):
                 display = input('Would you like to view individual trip data? Enter yes or no:  \n').lower()

                 if display == 'yes':
                     x = x + 5
                     y = y + 5
                     print(df.iloc[x:y])
                 else:
                         break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
