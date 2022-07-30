import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_data_filters():
    """
    Requests user to specify a city, month, and day for analysis.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    print("There are data on three cities. \nWhich city would you like to see? \n")
    city = input("Type in either: 'washington', 'new york city', or 'chicago' below: \n ")
    while city.lower().strip() not in ['washington', 'new york city','chicago']:
        city =input("Please make a selection from the options above: \n")


    # get user input for month (all, january, february, ... , june)
    print("What month would like to see data on?")
    month = input("If you rather want to see data for all months press 'all' else press any key to choose \n")
    if month.lower().strip() == 'all':
        pass
    else:
        month = input("Select a month to filter by: \n[january, february, march, april, may, june]: \n")
        months =  ['january', 'february', 'march', 'april', 'may', 'june']
        while month.lower().strip() not in months:
            month = input("Please make a selection from the options above\n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("Would you also like to filter for a particular day of the week?")
    day = input("If you rather want to see data for all days press 'all' else press any key to choose\n")
    if day.lower().strip() == 'all':
        pass
    else:
        day = input("Select a day to filter by: \n[monday, tuesday, wednesday, thursday, friday, saturday, sunday] \n")
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while day.lower().strip() not in days:
            day = input("Please make a selection from the options above\n")
    city = CITY_DATA[city]

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
    df= pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month in months:
        fil_month = months.index(month) + 1
        df = df[df['month'] == fil_month]
    else: 
        pass
    if day == 'all':
        pass
    else:
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()
    print(f"The most common month was: {common_month[0]}")


    # display the most common day of week
    common_day = df['day_of_week'].mode()
    print(f"The most common day of week was: {common_day[0]}")


    # display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()
    print(f"The most common start hour was: {common_start_hour[0]}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()
    print(f"The most commonly used start station was: {start_station[0]}")


    # display most commonly used end station
    common_end_station = df['End Station'].mode()
    print(f"The most commonly used end station was: {common_end_station[0]}")


    # display most frequent combination of start station and end station trip
    combo = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(f"The most frequent combination of start station and end station trip was: \n{combo}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"The total travel time was: {df['Trip Duration'].sum()}")


    # display mean travel time
    print(f"The mean travel time was: {df['Trip Duration'].mean()}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(f"The User Type count is shown below: \n{user_type_count}")


    # Display counts of gender
    if 'Gender' in df:    
        print(f"The count for each gender is: \n{df['Gender'].value_counts()}")
    else: 
        pass
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print(f"The earliest year of birth was: {df['Birth Year'].min()}")
    else:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_data_filters()
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
