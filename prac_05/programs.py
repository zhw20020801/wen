# 1. Percentage change
original_value = float(input("Input a value: "))
change_percentage =int(input("Input a percentage of change: "))
change = change_percentage / 100
print(f'Originak: {original_value},Change: {change}, Result: {result}')

# 2. Time of day
time = int(input("input the time (0-23 hours): "))
choice = input("Input y if the time is coming else input n:"). lower()
if time <= 12:
    before_after = "before"
else:
    before_after = "after"
if choice == "y":
  coming_going = "coming. Hi"
else:
    coming_going = "going. Bye"
print("It is {before_after} noon and you are {coming_going}!")

# 3. Coffee orders made simple
coffee_type = input("black or whits"). lower()
coffee_size = input("small, medium, large"). lower()
if coffee_size == "Small":
    cost = 3
elif coffee_size == "medium":
    cost = 4
else:
    cost = 5
if coffee_type != "black":
    cost += 1
print("your coffee type is {},and your size is {}, it cost ${}.". format(type, size, cost))

# 5. Accumulation
high_value = int(input("high_number: "))
low_value = int(input("low_number: "))
total_value = 0
while low_value > high_value:
    print("Invalid value")
    low_value = int(input("low_number: "))
    high_value = int(input("high_number: "))
for i in range(low_value, high_value + 1):
    print(i, end="")
    total_value += i
print("total value is:", total_value)

