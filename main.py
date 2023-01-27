from datetime import datetime

user_input = input("Enter Your goal with a deadline seperated by colon: \n ")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
# calculate how many days from now till deadline
today_date = datetime.today()
if deadline_date > today_date:
    remaining_time = deadline_date - today_date
    print(f"Dear user! Time remaining for your goal ' {goal} ' is {remaining_time.days} days")
    hour_calculation = int(remaining_time.total_seconds() /60 /60)
    print(f"Dear user! Time remaining for your goal ' {goal} ' is {hour_calculation} hours")
else:
    print("Sorry, Deadline has already passed!! ")