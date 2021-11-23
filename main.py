import mass_air_flow_monitoring
import normal_engine_load
import reading_obd
#import matplotlib.pyplot as plt
import vehicle_information as VE
import coolant_temperature_monitoring as ctm
import vehicle_speed as VS
data_set = reading_obd.read_csv_obd()
coolant_temperature = data_set[0]
gps_speed = data_set[1]
intake_air_temperature = data_set[2]
engine_rpm = data_set[3]
mass_air_flow = data_set[4]
throttle_position = data_set[5]
engine_load = data_set[6]
vehicle_speed = []

def Vehicle_Speed(rpm):
    v = (float(rpm)*3.14*2*VE.Tyre_size*0.0254)/(VE.gear_ratio*VE.axle_ratio*60)
    return v

for i in engine_rpm:
    v = Vehicle_Speed(i)
    vehicle_speed.append(v)

print("                                       ",ctm.monitor_coolant(coolant_temperature))
print("---------------------------------------------------------------------------------------------------------")
print("                                       ",VS.speed_comparison(vehicle_speed,gps_speed))
print("---------------------------------------------------------------------------------------------------------")
print("                                      ",normal_engine_load.normal_engine_load(engine_load))
VS.speed_plotting(vehicle_speed,gps_speed)
#mass_air_flow_monitoring.plotting_maf(mass_air_flow,engine_rpm)
mass_air_flow_monitoring.plotting_maf_and_tps(mass_air_flow,throttle_position,engine_rpm)
print("                         ",mass_air_flow_monitoring.linearity_maf_and_rpm(mass_air_flow,engine_rpm))
#print("---------------------------------------------------------------------------------------------------------")
mass_air_flow_monitoring.parallelism_maf_and_tps(mass_air_flow,throttle_position,engine_rpm)
print("---------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------")
#print(vehicle_speed)









