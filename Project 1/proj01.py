###########################################################
#  Computer Project #1
#
#  Algorithm
#    print a Temperature
#    print a Wind Speed
#    print the wind chill using WCT = 35.74 + .6215T - 35.75**.16 + .4275TV**.16
#    print a Temperature
#    print a Wind Speed
#    print the wind chill using WCT = 35.74 + .6215T - 35.75**.16 + .4275TV**.16
#    print a Temperature
#    print a Wind Speed
#    print the wind chill using WCT = 35.74 + .6215T - 35.75**.16 + .4275TV**.16
#    prompt for a Temperature and wind Speed
#    convert temperature and wind Speed to floats from strings
#    print temperature, new line, wind speed, new line, wind chill
###########################################################
print("Wind Chill Conversion\n")

print("Temperature (degrees F): 15.0")
print("Wind Speed (MPH): 10.0")
print("Wind Chill Temperature Index:", 35.74 + 0.6215*15.0 - 35.75*(10.0**0.16) + 0.4275*15.0*(10.0**0.16), "\n")

print("Temperature (degrees F): 0.0")
print("Wind Speed (MPH): 20.0")
print("Wind Chill Temperature Index:", 35.74 + 0.6215*0.0 - 35.75*(20.0**0.16) + 0.4275*0.0*(20.0**0.16), "\n")

print("Temperature (degrees F): -15.0")
print("Wind Speed (MPH): 30.0")
print("Wind Chill Temperature Index:", 35.74 + 0.6215*-15.0 - 35.75*(30.0**0.16) + 0.4275*-15.0*(30.0**0.16), "\n")

temp_str = input("Please enter the temperature (degrees F): ")
wind_str = input("Please enter the wind speed (MPH): ")
print("\n")

temp_flt = float(temp_str)
wind_flt = float(wind_str)

print("Temperature (degrees F):", temp_flt)
print("Wind Speed (MPH):", wind_flt)
print("Wind Chill Temperature Index:", 35.74 + 0.6215*temp_flt - 35.75*(wind_flt**0.16) + 0.4275*temp_flt*(wind_flt**0.16))
