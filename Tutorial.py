import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import math
# Q1
f1 = 0.25 * 10 ** 6
f2 = 0.5 * 10 ** 6
f3 = 1 * 10 ** 6
f4 = 2.5 * 10 ** 6
f5 = 5 * 10 ** 6

T1 = 1 / f1
T2 = 1 / f2
T3 = 1 / f3
T4 = 1 / f4
T5 = 1 / f5

c = 1566

lam1 = c / f1
lam2 = c / f2
lam3 = c / f3
lam4 = c / f4
lam5 = c / f5

fig = px.scatter(x=[f1, f2, f3, f4, f5], y=[lam1, lam2, lam3, lam4, lam5])
fig.update_layout(title="Frequency v Wavelength", xaxis_title="Frequency (Hz)", yaxis_title="Wavelength (m)")
fig.show()

"""The relationship between the frequency against wavelength is that there exponential trend. As it frequency goes closer to 0 the wavelength increases exponentially"""

#Q2
"""The two factors that determines the speed of sound propagation with a medium are bulk modulus (stiffnes) and density.
There is significant increase in sound velocity with a small increase in stiffness while if there is a increase in density there will be a slight decrease in the sound velociy."""

#Q3
B_air = 1.2 * 10 ** 5
B_bone = 15 * 10 ** 9
B_muscle = 2800 * 10 ** 6

p_air = 1.2
p_bone = 1810
p_muscle = 1070

c_air = math.sqrt(B_air/p_air)
print(round(c_air))
#316
c_bone = math.sqrt(B_bone/p_bone)
print(round(c_bone)) 
#2879
c_muscle = math.sqrt(B_muscle/p_muscle)
print(round(c_muscle))
#1618
#Q4
c_lung = 650
c_blood = 1566
c_brain = 1612

p_lung = 400
p_blood = 1060
p_brain = 1030

Z_air = (p_air * c_air)
print(round(Z_air))
#379
Z_lung = p_lung * c_lung
print(round(Z_lung))
#260000
Z_blood = p_blood * c_blood
print(round(Z_blood))
#1659960
Z_brain = p_brain * c_brain
print(round(Z_brain))
#1660360
Z_bone = p_bone * c_bone
print(round(Z_bone))
#5210566 kg/s m^2
#Q5
Z_kidney = 1.62 * 10 ** 6
I = 100 * 10000 / 1000

P = math.sqrt(2 * Z_kidney * I)
print(round(P))
#56921