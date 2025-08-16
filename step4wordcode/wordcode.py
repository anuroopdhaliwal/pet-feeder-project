Word Code:
1.	Input the scheduled feeding times.
2.	For each scheduled feeding time:
IF (TIME /= SCHEDULEDTIME)
THEN 
	 Wait 10 minutes.
	Check again.
ELSE IF (TIME = SCHEDULE TIME)
THEN 
	Activate MOTOR and dispense food.
3.	Check if food was dispensed:
IF (FOODDISPENSED = FALSE)
	ALERT = 1
	UPDATE = 0
	End the feeding cycle.
ELSE IF (FOODDISPENSED = TRUE)
	Continue.
4.	Check if feeding period passed:
IF FEEDINGPERIOD has not passed 
	Wait 10 minutes.
	Check again.
ELSE IF FEEDINGPERIOD has passed
	Continue.
5.	Check if food was consumed:
IF (FOODREMAINING = FALSE)
	ALERT = 0
	UPDATE = 1
ELSE IF (FOODREMAINING = TRUE)
	ALERT = 1
	UPDATE = 0
6.	Repeat for all scheduled feeding times.
