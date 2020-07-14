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
   # while city == 'chicago' OR 'new york city' OR 'washington':
      #  try:
            city = input("Would you like to see data for Chicago, New york city, or Washington ?")
   # break
     #   except:
            print('Please enter the correct city name')
            
     
     
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month would you like to filter data for ?")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day would you like to filter data for ?")

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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month is: ', common_month)
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day = df['day_of_week'].mode()[0]
    print('Most common day is: ', common_day)
    
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_starthour = df['hour'].mode()[0]
    print('Most common start hour is: ', starthour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print("most commonly used start station: ", common_startstation)

    # TO DO: display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print("most commonly used end station: ", common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
     df['start_end'] = df['Start Station'+'End Station']
     common_startend =   df['start_end'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ", common_startend)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['End Time']-df['Start-Time']
    print("Total travel time is: ",travel_time)

    # TO DO: display mean travel time
    print("Mean travel time is: ", travel_time.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print(gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest year of birth is : ", df['Birth Year'].min())
    print("The most recent year of birth is : ", df['Birth Year'].max())
    common_by = df['Birth Year'].mode()[0]
    print("The most common  year of birth is : ", common_by)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
