import csv
def read_csv_obd():
    with open('OBD.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        coolant_temperature = []
        engine_rpm = []
        gps_speed = []
        intake_air_temperature = []
        mass_air_flow = []
        throttle_position = []
        engine_load = []
        for row in csv_reader:
            #print(row)
            coolant_temperature.append(float(row['Engine Coolant Temperature(Â°C)']))
            gps_speed.append(float(row['GPS Speed (Meters/second)']))
            engine_rpm.append(float(row['Engine RPM(rpm)']))
            intake_air_temperature.append(float(row['Intake Air Temperature(Â°C)']))
            engine_load.append(float(row['Engine Load(%)']))
            mass_air_flow.append(float(row['Mass Air Flow Rate(g/s)']))
            throttle_position.append(float(row['Throttle Position(Manifold)(%)']))
            engine_load.append(float(row['Engine Load(%)']))
        #print("coolant temperature : " ,coolant_temperature)
        #print("GPS speed : " ,gps_speed)
        #print("engine rpm : ",engine_rpm)
        #print("intake air temperature : ",intake_air_temperature)
        #print("engine rpm : ",engine_rpm)
        #print("mass air flow : " , mass_air_flow)
        #print("throttle position : " ,throttle_position)
        return (coolant_temperature,gps_speed,intake_air_temperature,engine_rpm,mass_air_flow,throttle_position,engine_load)
# GPS Speed (Meters/second)
# Engine Coolant Temperature(Â°C)
# Engine RPM(rpm)
# Intake Air Temperature(Â°C)
# Engine Load(%)
# Mass Air Flow Rate(g/s)
# Throttle Position(Manifold)(%)