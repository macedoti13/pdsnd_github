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
    while True:
        city = input("Which city would you like explore the data from? Chigado, New York city or Washington?\n")
        city = city.lower()
        if city in ["washington", "new york city", "chicago"]:
            break
        else: print("Invalid input, please make sure you type a valid city.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to see the data from? If you want to see the data all from all months, just type 'all'.\n")
        month = month.lower();
        if month in ["january", "february", "march", "april", "june", "all"]:
            break
        else: print("Invalid input, make sure you are typing a valid month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of week yould you like to see the data from? If you want to see the data from all days, just type 'all'.\n")
        day = day.lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else: print("Invalid input, make sure you type a valid day")

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
    # getting de data for city
    print("Getting yout data...")
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'fubruary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df = df[df['month'] == month]

    #filter by day of week if applicable
    if day != 'all':
        # use the index of the days list to get the new dataframe
        df = df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is:", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day of week is:", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonlly used start station is: ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_route'] = df['Start Station'] + ' ' + df['End Station']
    print("The most frequent combination of start and end station is: ", df['frequent_route'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: ", df['Trip Duration'].sum(), "seconds\n")


    # TO DO: display mean travel time
    print("The mean travel time is: ", df['Trip Duration'].mean(), "seconds\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types: ", "\n", df["User Type"].value_counts())


    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'gender' in df.columns:
        print("Counts of gender: ", "\n", df["Gender"].value_counts(), "\n")
        print("The earliest year of birth is: ", df["Birth Year"].min(), "\n")
        print("The most recent year of birth is: ", df["Birth Year"].max(), "\n")
        print("The most common year of birth is: ", df["Birth Year"].value_counts().idxmax()) # In this line i searched for help in Stack Overflow



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Asks the user if the user wants to see 5 lines of raw data
def display_raw_data(df):
    print("Would tou like to see some raw data? Type 'no' if you don't")
    x = 0
    while (input()!= 'no'):
        x += 5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
