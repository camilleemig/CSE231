# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:25:11 2016

@author: Camille
"""

points_str = input("Enter the lead in points: ")
points_ahead_int = int(points_str)

lead_calculation_float = float(points_ahead_int - 3)

has_ball_str = input("Does the lead team have the ball (Yes or No)? ")
if has_ball_str == "Yes":
    lead_calculation_float += .5
else:
    lead_calculation_float -=.5

if lead_calculation_float < 0:
    lead_calculation_float = 0

lead_calculation_float = lead_calculation_float**2

seconds_remaining_int = int(input("Enter the number of seconds remaining: "))

if lead_calculation_float > seconds_remaining_int:
    print("Lead is safe.")
else:
    print("Lead is not safe.")
    