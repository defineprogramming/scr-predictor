def get_user_input():
    user_data = {}

    print("Please enter your current role:")
    user_data['current_role'] = input()

    print("Please enter your time in current role (in months):")
    user_data['time_in_role'] = int(input())

    print("Please enter your level of satisfaction with the current role (1-10):")
    user_data['satisfaction_level'] = int(input())

    print("Please enter your number of completed projects:")
    user_data['completed_projects'] = int(input())

    print("Please enter your average hours worked per week:")
    user_data['average_hours'] = int(input())

    return user_data