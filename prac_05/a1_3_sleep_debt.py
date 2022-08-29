print('Welcome to sleep debt calculator')
days = int(input("Enter number of days for which sleep debt is to be calculated: "))
i = 1
# this actual_sleep variable will store total sleep taken by the user
actual_sleep = 0
desirable_sleep = days * 8
while(i<days+1):
    # taking input
    print("Night ", i, " hours sleep: ")
    real = float(input())
    # checking if user is entering an invalid input like hours in negative
    # or hours greater than 24
    if(real >= 0 and real <= 24):
        actual_sleep += real
        i += 1
    else:
        # throwing error for invalid input
        print('Invalid number of hours.')

# printing the sleep debt as per the input
print('Recommended total sleep is: ', desirable_sleep, 'hours.')
print('Your total sleep is: ', actual_sleep, ' hours.')
if(actual_sleep < desirable_sleep):
    print('Your total sleep debt over this time is: ', desirable_sleep-actual_sleep, " hours.")
else:
    print('You are getting enough sleep. Keep it up!')

# The repetition pattern used here is to enter the user's total sleep time per day.
# Only the days are changing.