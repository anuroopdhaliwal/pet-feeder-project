def get_input(prompt):
    """Helper function to get validated binary input (0 or 1)."""
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            else:
                print("Please enter 1 for Yes or 0 for No.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 0).")

def check_alarm(DRIV, PASS, BELTD, BELTP, IGN):
    """Returns alarm status: 0 = ON, 1 = OFF"""
    if IGN == 1 and ((DRIV == 1 and BELTD == 0) or (PASS == 1 and BELTP == 0)):
        return 0  # Alarm ON
    else:
        return 1  # Alarm OFF

def main():
    print("=== Seatbelt Alarm System ===")
    DRIV = get_input("Is the driver seated? (1=Yes, 0=No): ")
    PASS = get_input("Is the passenger seated? (1=Yes, 0=No): ")
    BELTD = get_input("Is the driver's seatbelt fastened? (1=Yes, 0=No): ")
    BELTP = get_input("Is the passenger's seatbelt fastened? (1=Yes, 0=No): ")
    IGN = get_input("Is the ignition ON? (1=Yes, 0=No): ")

    ALARM = check_alarm(DRIV, PASS, BELTD, BELTP, IGN)
    print("ALARM status:", "ON" if ALARM == 0 else "OFF")

if __name__ == "__main__":
    main()
