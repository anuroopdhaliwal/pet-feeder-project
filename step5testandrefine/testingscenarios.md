# STEP 5: Test and Refine the Solution (Debug and Verify)
## Scenario 1: Pet eats as expected.
- System Logic:
1.	The system checks if the scheduled time matches the current time
2.	If so, the motor is activated, dispensing the food
3.	The sensor detects that the food is successfully dispensed
4.	After the feeding period passes, the scale checks food consumption and detects no food remaining
5.	The system sends a user update such as “PET FEEDER UPDATE: Food consumed successfully!”
- Expected output: A user update such as “PET FEEDER UPDATE: Food consumed successfully!”
- Actual Output: Matches the expected output 

## Scenario 2: Pet does not eat
- System Logic:
1.	The system checks if the scheduled time matches the current time
2.	If so, the motor is activated, dispensing the food
3.	The sensor detects that the food is successfully dispensed
4.	After the feeding period passes, the scale checks food consumption and detects food remaining
5.	The system sends a user alert such as “PET FEEDER ALERT: Food not consumed within feeding period.”
- Expected output: A user alert such as “PET FEEDER ALERT: Food not consumed within feeding period.”
- Actual Output: Matches the expected output
- Improvement: Sending another reminder to the user after thirty minutes to ensure they do not forget to check on the pet.
## Scenario 3: Food bin empty
- System Logic:
1.	The system checks if the scheduled time matches the current time
2.	If so, the motor is activated, dispensing the food
3.	The sensor detects that the food has not been successfully dispensed
4.	The system sends a user update such as “PET FEEDER ALERT: Food not dispensed.”
- Expected output: A user update such as “PET FEEDER ALERT: Food not dispensed.”
- Actual Output: Matches the expected output
- Improvement: Implement a sensor where the food is stored which sends an alert every time it drops below a certain threshold, informing the users of when the system must be refilled early in the day, before scheduled feeding times.

## System refinements:
Additional refinements could be made to the system and are listed below.

- Since the food scale is a Boolean type, the pet feeder does not have the ability to check if the pet has partially eaten and instead only monitors if they have eaten their food completely. This could be refined by replacing the discrete Boolean scale with a continuous variable scale which measures in grams. This would allow for the pet feeder to detect specific levels of consumption and send detailed updates such as “Pet consumed 50 out of 150 grams”, giving the user an indication as to how urgent the situation is.

- The pet feeder has a fixed amount of food which is dispensed, 150 grams, however the pet feeder could cater to a larger variety of pets if it allowed users to set the portion sizes. This could be refined by changing the food amount to a user input, designing the motor to dispense food based on weight, and using the bowl scale to verify the weight.

- Since the system runs on an outlet source, if the power fails or there is an outage, there is no backup system, and the pets would miss their meals. This issue could be solved by implementing a rechargeable battery which could run the pet feeder for a few pet cycles.

- A useful feature which could be added is a tracker which monitors the health of the animal by logging their eating habits over time. The tracker could record the specific amount of food eaten in grams by using a continuous scale to replace the current Boolean scale and track if the pet does not eat for consecutive days or deviate from their regular feeding pattern. This would improve user satisfaction through reliability and allow for early detection of health issues by tracking changes in appetite.   
