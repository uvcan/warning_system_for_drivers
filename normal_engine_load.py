def normal_engine_load(engine_load):
    sum=0.0
    for i in engine_load:
        sum+=i
    mean_load = sum/len(engine_load)
    print("---------------------------------------------------------------------------------------------------------")
    print("                            MEAN ENGINE LOAD % = ", mean_load)
    if(mean_load>30 and mean_load<50):
        return "NORMAL ENGINE LOAD"
    else:
        return "   HEAVY LOAD"
