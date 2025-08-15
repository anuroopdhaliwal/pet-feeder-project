# Example Python implementation
DRIV = int(input("Driver seated? (1=Yes, 0=No): "))
PASS = int(input("Passenger seated? (1=Yes, 0=No): "))
BELTD = int(input("Driver belt fastened? (1=Yes, 0=No): "))
BELTP = int(input("Passenger belt fastened? (1=Yes, 0=No): "))
IGN = int(input("Ignition ON? (1=Yes, 0=No): "))

if ((DRIV and not BELTD) or (PASS and not BELTP)) and IGN:
    ALARM = 0  # ON
else:
    ALARM = 1  # OFF

print("ALARM status:", "ON" if ALARM == 0 else "OFF")
