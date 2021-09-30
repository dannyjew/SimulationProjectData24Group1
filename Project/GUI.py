import matplotlib.pyplot as plt
import sys


def welcome_func(default_val=True):
    # These are all user input captures
    user_input = ""
    length = "3"
    centre_count = "1"

    # 1. Initial Screen with Simulation Settings
    if default_val:
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


def print_simulation_results(simulation_result):
    print(f"""\n\n{'-' * 50}\nEnd of Simulation Report

            Number of open centres: {simulation_result["Open"]}
            Number of full centres: {simulation_result["Full"]}
            Number of trainees in training: {simulation_result['Training']}
            Number of trainees in waiting : {simulation_result['Waiting']}

    End of End of Simulation Report\n{'-' * 50}""")


def display_graph(xaxis, yaxis, y_label, graph_title):
    plt.xlabel('Month')
    plt.ylabel(y_label)
    plt.title(graph_title)
    plt.plot(xaxis, yaxis)
    plt.show()


def user_input_graph():
    input_choice = 0
    value = True
    print("Would you like to see one of these graphs? \n")
    print("1. Number of full centres x time")
    print("2. Number of trainees in waiting x time")
    print("3. Number of trainees in training x time")
    print("4. Number of open centres x time")
    print("5. Number of total centres x time")
    print("6. Do not show me a graph")
    value = True
    while value:
        input_choice = input("\nPlease select the graph you would like to see: ")
        if input_choice.isnumeric():
            if 0 < int(input_choice) <= 6:
                value = False
                return int(input_choice)


def graph_choice(simulation_result, input_choice):
    xaxis = []
    yaxis = []
    y_label = ""
    graph_title = ""

    # Graph choice for the number of full centres against time.

    if input_choice == 1:
        for key, value in simulation_result.items():
            # print(f"Month = {key}")
            # print(f"Training = {value['Training']}")
            xaxis.append(key)
            yaxis.append(value['Full Centres'])
            y_label = 'Number of Full Centres'
            graph_title = 'Graph showing number of full centres against time!'


    # Graph choice for the number of trainees in waiting against time.

    elif input_choice == 2:
        for key, value in simulation_result.items():
            # print(f"Month = {key}")
            # print(f"Training = {value['Training']}")
            xaxis.append(key)
            yaxis.append(value['Waiting'])
            y_label = 'Number of Trainees in the waiting list'
            graph_title = 'Graph showing number of trainees in waiting against time!'


    # Graph choice for the number of trainees in training against time.

    elif input_choice == 3:
        for key, value in simulation_result.items():
            # print(f"Month = {key}")
            # print(f"Training = {value['Training']}")
            xaxis.append(key)
            yaxis.append(value['Training'])
            y_label = 'Number of Trainees in training'
            graph_title = 'Graph showing the number of trainees in training against time!'


    # Graph choice for the number of open centres against time.

    elif input_choice == 4:
        for key, value in simulation_result.items():
            # print(f"Month = {key}")
            # print(f"Training = {value['Training']}")
            xaxis.append(key)
            yaxis.append(value['Open'])
            y_label = 'Number of Open centres'
            graph_title = 'Graph showing the number of open centres against time!'


    # Graph choice for the number of total centres against time.

    elif input_choice == 5:
        for key, value in simulation_result.items():
            total_centres = value['Full'] + value['Open']
            # print(f"Month = {key}")
            # print(total_centres)
            # Need to create a list for total centres
            xaxis.append(key)
            yaxis.append(total_centres)
            y_label = 'Total number of Centres'
            graph_title = 'Graph showing the number of total centres against time!'


    # Graph choice for not showing a graph.

    elif input_choice == 6:
        print(f"You've selected no graph!")
    display_graph(xaxis, yaxis, y_label, graph_title)
