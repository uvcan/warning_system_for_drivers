import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import calculating_linearity
import calculating_parallelism
def plotting_maf(maf,rpm):
    new_rpm = []
    new_maf = []
    mean_maf=[]
    mean_rpm=[]
    for i in range(len(rpm)):
        if(rpm[i]>1000 and rpm[i]<2250):
            new_rpm.append(rpm[i])
            new_maf.append(maf[i])
    j=0
    while(j<len(new_maf)):
        sum_maf=0
        sum_rpm=0
        for k in range(5):
            sum_maf+=new_maf[j+k]
            sum_rpm+=new_rpm[j+k]
        m1=sum_maf/5
        m2=sum_rpm/5
        mean_maf.append(m1)
        mean_rpm.append(m2)
        j+=5
    plt1.plot(mean_rpm,mean_maf)
    plt1.xlabel("engine rpm")
    plt1.ylabel("mass air flow")
    plt1.show()

def plotting_maf_and_tps(mass_air_flow, throttle_position, engine_rpm):
    plt1.plot(mass_air_flow,  color='b', label='mass_air_flow')
    plt1.plot(throttle_position,  color='g', label='throttle position')
    plt1.title('maf and tps')
    plt1.legend()
    plt1.show()
    plt2.plot(mass_air_flow,engine_rpm, color='b', label='mass_air_flow')
    plt2.plot(throttle_position,engine_rpm, color='g', label='throttle position')
    plt2.title('maf and tps')
    plt2.xlabel('engine rpm')
    plt2.legend()
    plt2.show()

def linearity_maf_and_rpm(mass_air_flow, engine_rpm):
    print("---------------------------------------------------------------------------------------------------------")
    print("                     CALCULATING THE LINEARITY BETWEEN MAF AND ENGINE RPM")
    print()
    if(calculating_linearity.linearity_calculation(mass_air_flow,engine_rpm)>0.6):
        return "         MAF SENSOR IS FINE"
    else:
        return "         MAF IF FAULTY"

def parallelism_maf_and_tps(mass_air_flow, throttle_position, engine_rpm):
    print("---------------------------------------------------------------------------------------------------------")
    print("                       CALCULATING PARALLELISM BETWEEN MAF AND TPS")
    print("                       SLOPE OF MAF = ",calculating_parallelism.parallelism_calculation(mass_air_flow,engine_rpm))
    print("                       SLOPE OF TPS = ",calculating_parallelism.parallelism_calculation(throttle_position,engine_rpm))



