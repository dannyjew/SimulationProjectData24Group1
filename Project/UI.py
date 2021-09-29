
def welcome_func():
    # These are all user input captures
    user_input = ""
    length = "3"
    centre_count = "1"

    # 1. Initial Screen with Simulation Settings
    print(f"""Simulation Settings\n{'-' * 50}
        Default Settings:
            Simulation Length (month):              {length}
            Initial Amount of Training Centres:     {centre_count}\n""")
    print("1. Run simulation with defaults")
    print("2. Change simulation settings\n")

    while True:
        user_input = input("Select an option: ")
        if user_input.isnumeric() and int(user_input) in range(1, 3):
            # Return the default settings
            if user_input == "1":
                return int(length), int(centre_count)
            break

    # 2. User wants to manually change settings
    while True:
        length = input("Enter Simulation Length (in months): ")
        if length.isnumeric() and int(length) > 0:
            break

    while True:
        centre_count = input("Enter the number of Training Centres at Simulation start: ")
        if centre_count.isnumeric() and int(centre_count) > 0:
            break

    return int(length), int(centre_count)
