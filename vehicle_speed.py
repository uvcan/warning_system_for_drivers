import  matplotlib.pyplot as plt
def speed_plotting(vehicle_speed, gps_speed):
    plt.plot(gps_speed, color='b', label='gps_speed')
    plt.ylabel('speed')
    plt.plot(vehicle_speed, color='g', label='vehicle_speed')
    plt.title('gps_speed and vehicle_speed')
    plt.legend()
    plt.show()
def speed_comparison(vehicle_speed, gps_speed):
    sum = 0
    for i in range(len(vehicle_speed)):
        diff = vehicle_speed[i]-gps_speed[i]
        if(diff<0):
            diff=diff*-1
        sum+=diff
    mean_diff = sum/len(vehicle_speed)
    print("---------------------------------------------------------------------------------------------------------")
    print(" MEAN DIFFERENCE IN VEHICLE SPEED AND GPS SPEED = ",mean_diff)
    print()
    if(mean_diff>6):
        return " CHECK YOUR ENGINE "
    else:
        return "ENGINE IS FINE"