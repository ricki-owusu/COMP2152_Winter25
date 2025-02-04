# Ricki Owusu-Ansah
# Assignment1
from typing import Dict

#Variables
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 #int
membership_active = True #bool

# Dictionary with workout stats: values as tuples
workout_stats: Dict[str, tuple[int, int, int]] = {
            #Yoga , Running, Weightlifting
    "Alex": (30, 45, 75),
    "Sam": (60, 45, 25),
    "Taylor": (70, 35, 25),
    "Jamie": (25, 20, 35)
}

print(workout_stats)

# initializing holder dictionary to store total minutes
totals: Dict[str, int] = {}

# Loop through workout_stats to calculate the total minutes for each friend
for friend, stats in workout_stats.items():
    total_minutes = sum(stats) # sum the workout minutes
    totals[f"{friend}_Total"] = total_minutes # store in total minutes holder dictionary

# update workout stats
workout_stats.update(totals)

print(workout_stats)

# extract workout minutes into a 2D list
workout_list = [list(stats) for stats in workout_stats.values()
                if isinstance(stats, tuple)] # 2D list: rows -> friends cols -> activities
# print 2D list
print(workout_list)

# Extract Yoga and Running minutes
yoga_running_minutes = [row[:2] for row in workout_list]
print(yoga_running_minutes)

# Extract weightlifting from last two friends
weightlifting_minutes = [row[2:3] for row in workout_list[2:4]]
print(weightlifting_minutes)

# Check if any friends have workout minutes above 120
for friend, total in totals.items():
    if total >= 120:
        print(f"Great job staying active, {friend.replace('_Total', '')}!")

# Checks if a friend exists in the dictionary and prints their total workout minutes
def does_exist(name: str):
    if name in workout_stats:
        return True
    else:
        return False

for friend, total in totals.items():
    if does_exist(friend):
        print(f"{friend.replace('_Total', '')} has a total of {total} minutes!")
    else:
        print(f"{friend.replace('_Total', '')} not found in the records")

# print highest and lowest total
for friend, total in totals.items():
    if total == max(totals.values()):
        print(f"{friend.replace('_Total', '')} has the highest total of minutes, with {total} minutes")
    elif total == min(totals.values()):
        print(f"{friend.replace('_Total', '')} has the lowest total of minutes, with {total} minutes")
