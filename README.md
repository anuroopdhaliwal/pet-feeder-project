# Anuroop Dhaliwal u3306135
## Intro to Information Technology Pet-Feeder Assignment 1
The project is a design of an automated and programmable pet-feeder which dispenses pet food for cats and dogs at scheduled times. The pet feeder monitors whether the food is dispensed at scheduled times and if it is consumed by the pet, sending alerts to the user accordingly. The feeder is designed for a single pet and requires weekly input due to limited memory.

## Features
- Scheduled feeding times input by the user for up to three times per day
- Automatically dispenses the food at the scheduled times
- Sends user alerts for unconsumed food or improper dispensing of food
- Sends user updates when the feeding is successful
- Powered by a continuous outlet source

## Constants/Operational Parameters
- Thirty minute feeding period
- 150 grams of food per feeding time

## Variables
- SCHEDULEDTIME: The scheduled feeding times set by the user
- TIME: The current time
- MOTOR: The motor status (True = motor activated, False = motor not activated)
- FOODDISPENSED: True if the food is detected by the sensor after the motor is activated.
- FEEDINGPERIOD: Thirty minutes (constant variable)
- FOODREMAINING: True if the food is detected by the scale after the feeding period passes.
- ALERT: 1 = alert is sent, 0 = alert is not sent
- UPDATE: 1 = update is sent, 0 = update is not sent

## Logic Flow
1. Input scheduled feeding times.
2. If (TIME /= SCHEDULEDTIME) then activate the motor. 
3. If motor is activated, dispense food.
4. If food is not detected, send alert. If food is detected, wait for feeding period to pass.
5. After the feeding period, check the scale.
   - If food does not remain, send update.
   - If food does remain, send an alert.
6. Repeat for all scheduled feeding times.


## Future improvements
- Send detailed alerts with the specific amount of food consumed
- Implement a sensor in the food storage bin to allow for refill alerts
- Allow users to input the amount of food to be dispensed
