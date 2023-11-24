from datetime import datetime, timedelta
current_time = datetime.now()

start_of_day = datetime(
    current_time.year, current_time.month, current_time.day, 0, 0, 0
)
end_of_day = datetime(
    current_time.year, current_time.month, current_time.day, 23, 59, 59
)

time_passed = current_time - start_of_day

time_left = end_of_day - current_time

# Calculate percentage of time passed and left
percentage_passed = (
    time_passed.total_seconds() / timedelta(days=1).total_seconds()
) * 100
percentage_left = (time_left.total_seconds() / timedelta(days=1).total_seconds()) * 100

print(f"Percentage of time passed today: {percentage_passed:.2f}%")
print(f"Percentage of time left for the day: {percentage_left:.2f}%")
