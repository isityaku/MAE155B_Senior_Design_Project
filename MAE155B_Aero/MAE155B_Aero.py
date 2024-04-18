### MAE155B Aerodynamics [WIP]
# Made By: Lance De La Cruz

## Outline
# State and justify airfoil choice
#   Include lift and drag polars for airfoil (XFLR5)
# Compute parameters for aircraft lift and drag coefficient equations
#   Refer to lecture for parameters required
# Define the following aerodynamic parameters (at cruise):
#   Lift Coefficient
#   Drag Coefficient
#   Lift-to-Drag Ratio

## Importing Libraries
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Atmospheric Parameters
g = 9.81 # gravitational acceleration [in m/s^2]
gamma = 1.4 # specific heat ratio
P = 101280 # atmospheric pressure [in Pa]
temp = 286; # atmospheric temperature [in K]
R = 287 # gas constant
mu = 1.8*10**-5 # dynamic viscosity
rho = P/(R*temp) # atmospheric density [in kg/m^3]
a = math.sqrt(gamma*R*temp) # speed of sound [in m/s]
L = 0.75 # estimated aircraft planform length (refer to MAE155B_Sizing_Scoring.py) [in m]

## Cruise Conditions
V_cruise = 18 # assumed cruise velocity [in m/s]
M = V_cruise/a # cruise mach number
Re = rho*V_cruise*L/mu # Reynold's number at cruise velocity

## Airfoil Configuration
airfoil = "Clark Y" # airfoil used for aircaft wing
Cl_alp = 0.09756097561 # aircraft 2-D lift curve slope
alp0 = -3.5 # angle-of-attack where Cl = 0
Cl_max = 1.5240 # maximum 2-D lift coefficient
Cl_min = 1.0371 # minimum 2-D lift coefficient
Cd_max = 0.14464 # maximum 2-D drag coefficient
Cd_min = 0.00538 # minimum 2-D drag coefficient

## Aircraft Configuration (refer to MAE155B_Sizing_Scoring.py)
b = 1.099 # wing span [in m]
c = 0.182 # wing chord [in m]
MAC = (2/3)*c # mean aerodynamic chord [in m]
S = b*c # wing area [in m^2]
AR = b/c # aspect ratio
d = 0.35 # fuselage diameter [in m]
S_exp_ref = 0.9 # exposed-reference planform area ratio
Lambda_quart = 0 # sweep angle at quarter-chord
Lambda_max = 0 # max sweep angle

## 3-D Lift
# 3-D Lift Calculation
beta = math.sqrt(1-(M**2))
F = 1.07*(1+(d/b))**2
nu = Cl_alp/(2*math.pi/beta)
CL_alp = (2*math.pi*AR)/(2+(math.sqrt(4+((AR**2)*(beta**2)/(nu**2))*(1+(math.tan(math.radians(Lambda_max))**2/(beta**2))))))*S_exp_ref*F # semi-empirical formula for 3-D lift-curve slope
CL_max = 0.9*Cl_max*math.cos(Lambda_quart)

os.system('cls') # clearing terminal

# 3-D Lift Plotting
alp = np.linspace(0,20,100)
CL = CL_alp*(alp-alp0)
print(CL_alp)
plt.plot(alp, CL)
plt.ylim(0, CL_max)
plt.show()

# 3-D Drag