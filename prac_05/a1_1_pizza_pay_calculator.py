# Display title
print("Warm Pizza Pay Calculator")
N_trips = input("    Number of trips: ")
N_minutes = input("Number of minutes: ")

# convert N_trips and N_minutes from string to int
N_trips = int(N_trips)
N_minutes = int(N_minutes)

# calculate pays
pay_for_trips = N_trips * 1.45
pay_for_minutes = N_minutes * 0.95
total_pay = pay_for_trips + pay_for_minutes

# display result
print(f"For {N_trips} trips, your pay is: ${pay_for_trips:.2f}")
print(f"For {N_minutes} minutes, your pay is: ${pay_for_minutes:.2f}")
print(f"Your total pay is: ${total_pay:.2f}")