import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import math
# Q1
f1 = 0.25 * 10 ** 6 # 0.25 MHz
f2 = 0.5 * 10 ** 6 # 0.5 MHz
f3 = 1 * 10 ** 6 # 1 MHz
f4 = 2.5 * 10 ** 6 # 2.5 MHz
f5 = 5 * 10 ** 6 # 5 MHz

T1 = 1 / f1 # Period calculation
print(T1)
# 4e-06 s
T2 = 1 / f2
print(T2)
# 2e-06 s
T3 = 1 / f3
print(T3)
# 1e-06 s
T4 = 1 / f4
print(T4)
# 4e-07 s
T5 = 1 / f5
print(T5)
# 2e-07 s

c = 1566 # Speed of the ultrasound wave in the liver tissue

lam1 = c / f1 # Wavelength calculation
print(lam1)
# 0.006264 m
lam2 = c / f2
print(lam2)
# 0.003132 m
lam3 = c / f3
print(lam3)
# 0.001566 m
lam4 = c / f4
print(lam4)
# 0.0006264 m
lam5 = c / f5
print(lam5)
# 0.0003132 m

fig = px.scatter(x=[f1, f2, f3,  f4, f5], y=[lam1, lam2, lam3, lam4, lam5]) # Plotting the dataset using plotly into a scatterplot
fig.update_layout(title= "Frequency v Wavelength", xaxis_title= "Frequency (Hz)", yaxis_title= "Wavelength (m)") # Updating the title and axis title
fig.show() # Show the graph on opera
"""
The relationship between the frequency against wavelength is that there exponential trend. As it frequency goes closer to 0 the wavelength increases exponentially
"""
# Q2
""" The two factors that determines the speed of sound propagation with a medium are bulk modulus (stiffnes) and density.
There is significant increase in sound velocity with a small increase in stiffness while if there is a increase in density there will be a slight decrease in the sound velociy.
"""
# Q3 
B_air = 1.2 * 10 ** 5 # Bulk modulus of air
B_bone = 15 * 10 ** 9 # Bulk modulus of bone
B_muscle = 2800 * 10 ** 6 # Bulk modulus of muscle

p_air = 1.2 # density of air
p_bone = 1810 # density of bone
p_muscle = 1070 # density of muscle

c_air = math.sqrt(B_air/p_air) # Speed of sound in air calculation
print(round(c_air)) # Print ronded value
# 316
c_bone = math.sqrt(B_bone/p_bone) # Speed of sound in bone
print(round(c_bone))
# 2879
c_muscle = math.sqrt(B_muscle/p_muscle) # Speed of sound in muscle
print(round(c_muscle))
# 1618
# Q4
c_lung = 650 # Speed of sound in lung
c_blood = 1566 # Speed of sound in blood
c_brain = 1612 # Speed of brain in brain

p_lung = 400 # Density in lung
p_blood = 1060 # Density in blood
p_brain = 1030 # Density in brain

Z_air = (p_air * c_air) # Calculation of acoustic impedance of air
print(round(Z_air))
# 379
Z_lung = p_lung * c_lung # Calculation of acoustic impedance of lung
print(round(Z_lung))
# 260000
Z_blood = p_blood * c_blood # Calculation of acoustic impedance of blood
print(round(Z_blood))
# 1659960
Z_brain = p_brain * c_brain # Calculation of acoustic impedance of brain
print(round(Z_brain))
# 1660360
Z_bone = p_bone * c_bone # Calculation of acoustic impedance of bone
print(round(Z_bone))
# 5210566 kg/s m^2
# Q5
Z_kidney = 1.62 * 10 ** 6 # Acoustic impedance of kidney
I = 100 * 10000 / 1000 # Intensity

P = math.sqrt(2 * Z_kidney * I) # Pressure calculation
print(round(P))
# 56921
# Q6
p_liver = 1060 # Density of liver
c_liver = 1566 # Speed of sound of liver
Z2_liver = p_liver * c_liver # Acoustic impedance calculation of liver
print(Z2_liver)
# 1659960

p_fat = 920 # Density of fat
c_fat = 1446 # Speed of sound of fat
Z1_fat = p_fat * c_fat # Acoustic impedance calculation of fat
print(Z1_fat)
# 1330320

R = (Z2_liver - Z1_fat) / (Z2_liver + Z1_fat) # Reflection coefficient calculation
print(round(R, 3))
# 0.11
# Q7
