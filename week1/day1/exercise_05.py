battery_capacity = 100
power_usage_per_hour = 5
hours_used = 2

hours_until_empty = (hours_used * power_usage_per_hour) - battery_capacity

print("Hours Until Empty:", hours_until_empty)
