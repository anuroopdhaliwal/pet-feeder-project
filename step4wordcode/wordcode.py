Word Code:
1.	Input the scheduled feeding times. #user input
2.	For each scheduled feeding time:
IF (TIME /= SCHEDULEDTIME)
# If the current time does not match a scheduled feeding time, the system waits 10 minutes and tries again.
THEN 
	Wait 10 minutes.
	Check again.
ELSE IF (TIME = SCHEDULEDTIME)
# If the current time does match a scheduled feeding time, the motor is activated to dispense food.
THEN 
	Activate MOTOR and dispense food.
3.	Check if food was dispensed:
IF (FOODDISPENSED = FALSE) 
# If food is not detected by sensor after the motor is activated, an alert is sent. It is likely the motor failed or the food needs to be manually refilled.
	ALERT = 1
	UPDATE = 0
	End the feeding cycle.
ELSE IF (FOODDISPENSED = TRUE) 
# If food is detected by sensor after motor activated, the system continues.
	Continue.
4.	Check if feeding period passed:
IF FEEDINGPERIOD has not passed 
# The feeding period is ongoing.
	Wait 10 minutes.
	Check again.
ELSE IF FEEDINGPERIOD has passed
	Continue.
5.	Check if food was consumed:
IF (FOODREMAINING = FALSE) 
# The scale detects no food remaining meaning the food has been consumed.
	ALERT = 0
	UPDATE = 1
ELSE IF (FOODREMAINING = TRUE) 
# The scale detects food remaining meaning the food has not been consumed.
	ALERT = 1
	UPDATE = 0
6.	Repeat for all scheduled feeding times.

