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
    
    
    city= input("plz select city (chicago, new york city, washington): ").lower()
    while city in CITY_DATA.keys():
        break
    if city not in CITY_DATA.keys():
        print(" wrong city")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Eneter month(all, january, february, ... , june_: ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week (all, monday, tuesday, ... sunday): ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
    
     month_list = [ 'january', 'february', 'march', 'april', 'may', 'june']
     month = month_list.index(month)+1
     df =df[df['month'] == month]
    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    
    # TO DO: display the most common month
    poplr_month = df['month'].mode()[0]
    print('Most Popular Month:', poplr_month)
    # TO DO: display the most common day of week
    popur_day_of_week = df['day_of_week'].mode()[0]
    print('Most Day Of Week:', popur_day_of_week)
    # TO DO: display the most common start hour
    poplr_comon_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', poplr_comon_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    poplar_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', poplar_start_station)

    # TO DO: display most commonly used end station
    poplar_end_station = df['End Station'].mode()[0]

    print('Most End Station:', poplar_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    poplar_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', poplar_combination_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
          
    # TO DO: Display counts of gender
    if city != 'washington':
           print('Gender Stats:')
           print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
           print('Birth Year Stats:')
           most_common_year = df['Birth Year'].mode()[0]
           print('Most Common Year:',most_common_year)
           most_recent_year = df['Birth Year'].max()
           print('Most Recent Year:',most_recent_year)
           earliest_year = df['Birth Year'].min()
           print('Earliest Year:',earliest_year)

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
