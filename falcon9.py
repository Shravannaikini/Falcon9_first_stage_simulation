import time
import sys
import numpy

print("simulation of first stage")



def flight():
    acceleration = float(0)
    initial_velocity = float(0)
    final_velocity = float(0)
    thrust = 7607.2
    times = float(0)
    mass = float(549054)
    sp_fl_consumption = 2442.5

    for i in range(0,163):
        acceleration = float(thrust/(mass-sp_fl_consumption)*times)
        velocity = float(initial_velocity+(acceleration*times))
        altitude = (0.5*acceleration*(times*times))/1000
        print("Time: ",times,"seconds","acceleration: ", acceleration ,"m/s2","velocity: ",velocity, "m/s","Altitude: ", altitude," KMS")
        times = float(times+1)
        mass = float(mass - sp_fl_consumption)
        
        time.sleep(1)
        
flight()

