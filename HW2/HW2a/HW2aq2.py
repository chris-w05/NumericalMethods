import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Question 2 Finite difference method

x = [0, 0.375, .75, 1.125, 1.5, 1.875, 2.25, 2.625, 3]
y = [1, -.2571, -0.9484, -1.9689, -3.2262, -4.6414, -6.1503, -7.7051, -9.275]

slopes = [ 0 ]

for i in range(1 , len(x)):
    slopes.append( (y[i] - y[i-1])/(x[i] - x[i-1]))
    

#finding derivative of slope:
dTheta = [0]
for i in range(1 , len(slopes)):
    dTheta.append( (slopes[i] - slopes[i-1])/(x[i] - x[i-1]))

#finding second y derivative:
dY2 = [0]
for i in range(1, len(y) - 1):
    ydiff = ( y[i + 1] - y[i]) - (y[i] - y[i-1])
    xdiff = ( x[i + 1] - x[i]) - (x[i] - x[i-1])
    dY2.append(ydiff )
dY2.append(0)

#Finding bending moment
E = 200 #[GPa]
I = 0.0003 #[m^4]
My =  np.multiply( dY2, E * I)
Mt =  np.multiply( dTheta, E * I)

data = {
    ("X values") : x,
    ("Y values") : y,
    ("Slope") : slopes,
    ("dTheta") : dTheta,
    ("dY2") : dY2
}

df = pd.DataFrame(data)
df.index = range(1, len(x)+1)


print(df)

plt.figure()
plt.plot(x, y)
plt.title("Profile of rod")

plt.figure()
plt.plot(x, Mt, label='M theta')
plt.plot(x, My, label='M Y')
plt.title("Second Derivatives Comparison")
plt.xlabel("X [m]")
plt.ylabel("Moment")
plt.legend()
plt.show()