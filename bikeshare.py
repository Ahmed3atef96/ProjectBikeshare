import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')


    while True:
            city = input('Please choose a city from the following: chicago, new york city or washington. ').lower()
            if city not in CITY_DATA :
                    print('\nmake sure you\'re entering the right city name.\n')
                    continue
            else:
                    print('\nyou choose {} please restart the program if you want to change the city.'.format(city).title())
                    break




    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
            month= input('\n\nPlease choose the month you want to filter with or type all to apply no month filter: ').lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'June', 'all') :
                    print('\nmake sure you\'re entering the months in this format(case insensitive): january, February......\n')
                    continue
            elif month == 'all':
                    print('\nyou choose to apply no month filter')
                    break
            elif month in ('january', 'february', 'march', 'april', 'may', 'June'):
                    print('\nyou choose {}.'.format(month).title())
                    break
            else:
                    break


    # get user input for month (all, january, february, ... , june

    while True:
            day = input('\n\nPlease choose the day you want to filter with or type all to apply no month filter: ').lower()
            if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
                    print('\nmake sure you\'re entering the months in this format(case insensitive): friday, monday......\n')
                    continue
            elif day == 'all':
                    print('\nyou choose to apply no day filter')
                    break
            elif day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                    print('\nyou choose {}.'.format(day).title())
                    break
            else:
                    break

    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*100)
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
    try:
            df = pd.read_csv(CITY_DATA[city])

    except:
            print('please enter one of the cities name: chicago, new york city or washington')

    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")


    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Month of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]

    print('Most Frequent Month:', popular_month)

    # display the most common day of week
    print('\nCalculating The Most Frequent Day of the week...\n')

    popular_day = df['day_of_week'].mode()[0]

    print('Most Frequent Day of the week:', popular_day)

    # display the most common start hour
    print('\nCalculating The Most Frequent Hour of Travel...\n')
    df['Start Time'] =pd.to_datetime(df['Start Time'])


    df['hour'] =df['Start Time'].dt.hour


    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    print('Most used start station:', popular_start,'\n')


    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    print('Most used end station:', popular_end,'\n')


    # display most frequent combination of start station and end station trip
    df['combination']='from '+df['Start Station']+' to '+df['End Station']
    popular_combination = df['combination'].mode()[0]

    print('Most popular combination of start station and end station trips:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total travel time is: ', total_travel_time,'\n')


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Average travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()

    print('User types count:\n\n', user_types_count,'\n')

    # Display counts of gender
    try:
            gender_count = df['Gender'].value_counts()

            print('Genders count:\n\n', gender_count,'\n')

    except KeyError:
            print('Unfortunately, Washington doesnt have information on costumers genders\n')

    # Display earliest, most recent, and most common year of birth
    try:
            min_year = int(df['Birth Year'].min())

            print('earliest year of birth: ', min_year)

            max_year = int(df['Birth Year'].max())

            print('Most recent year of birth: ', max_year)

            mode_year = int(df['Birth Year'].mode())

            print('Most common year of birth: ', mode_year)
    except KeyError:
            print('Unfortunately, Washington doesnt have information on costumers birth years')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def user_data(df):

    while True:
        n = 5
        raw_data = str(df.head(n))
        print(raw_data)
        question = input('\nwould you like to view more raw user data?(yes or no) ').casefold()
        if question == 'yes':
                n +=5
                continue

        else:
                break



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
