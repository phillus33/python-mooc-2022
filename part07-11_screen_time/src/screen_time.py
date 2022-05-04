from datetime import datetime, timedelta

filename = input("Filename: ")
# start = input("Starting date: ")
start = "27.06.2020"
no_days = int(input("How many days: "))

start_date = datetime.strptime(start, "%d.%m.%Y")
printed_start = start_date.strftime("%d.%m.%Y")
printed_end = (datetime.strptime(start, "%d.%m.%Y") + timedelta(days = no_days)).strftime("%d.%m.%Y")

screen_times = {}
print("Please type in screen time in minutes on each day (TV computer mobile): ")
sum = 0
for i in range(no_days):
    date_formatted = start_date.strftime("%d.%m.%Y")
    screen_times[date_formatted] = [input(f"Screen time {date_formatted}: ")]
    
    numbers = screen_times[date_formatted][0].split(" ")
    for number in numbers:
        sum += int(number)

    
    start_date += timedelta(days = 1)
print(screen_times)
# print(sum)



# print(f"Time period: {printed_start}-{printed_end}")
print(f"Data stored in file {filename}")
for date, minutes in screen_times.items():
    result = str(date)
    for value in minutes:
        result += value + "***"
    result = result[:-1]
    print(result)

# with open(filename, "w") as file:
#     file.write(f"Time period: {printed_start}-{printed_end}\n")
#     file.write(f"Total minutes: {sum}\n")
#     file.write(f"Average minutes: {sum/len(screen_times)}")
#     for date, minutes in screen_times.items():



