def monitor_coolant(temperature):
    sum=0
    for i in temperature:
        sum+=i
    mean_temperature = sum/len(temperature)
    print("---------------------------------------------------------------------------------------------------------")
    print("                             COOLANT TEMPERATURE = ", mean_temperature)
    if(mean_temperature>85):
        return "High temperature"
    else:
        return "fine temperature"