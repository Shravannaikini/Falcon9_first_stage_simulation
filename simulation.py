import time
import sys
import numpy

print("simulation of first stage")



def flight():
    acceleration = float(0)
    initial_velocity = float(0)
    final_velocity = float(0)
    thrust = 4846.9
    times = float(0)
    mass = float(320000)
    sp_fl_consumption = 1256.363636

    for i in range(0,111):
        acceleration = float(thrust/(mass-sp_fl_consumption)*times)
        print("Time: ",times,"seconds")
        print("acceleration: ", acceleration ,"m/s2")
        velocity = float(initial_velocity+(acceleration*times))
        print("velocity: ",velocity, "m/s or", (velocity*60*60)/1000,'KMPH')
        times = float(times+1)
        mass = float(mass - sp_fl_consumption)
        
        time.sleep(1)
        
flight()

