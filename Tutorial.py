import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

f1 = 0.25 * 10 ** 6
print(f1)
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