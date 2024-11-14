import numpy as np

# Given values
P1 = 432815.69  # Pa (total pressure inside the tank)
P0 = 88077.69   # Pa (atmospheric pressure)
V = 0.02251     # m^3 (volume of the tank)

# Uncertainties (delta values)
delta_P1 = 13789.52/2  # Pa (uncertainty in gauge pressure)
delta_P0 = 33.86/2     # Pa (uncertainty in atmospheric pressure)

# Radius and its uncertainty
r = 0.1143  # meters
delta_r = 0.0015875  # meters (uncertainty in radius)

# Length of the tank
h = 0.55  # meters

# Calculating uncertainty in volume (delta_V)
delta_V = np.pi * 2 * r * delta_r * h

# Partial derivatives
# 1. Partial derivative w.r.t P1
dE_dP1 = V * (np.log(P1 / P0) + P0 / P1)

# 2. Partial derivative w.r.t P0
dE_dP0 = -V * (P1 / (P0**2))

# 3. Partial derivative w.r.t V
dE_dV = P1 * (np.log(P1 / P0) + P0 / P1 - 1)

# Error propagation formula
relative_error_E_P1 = (dE_dP1 * delta_P1 / P1)**2
relative_error_E_P0 = (dE_dP0 * delta_P0 / P0)**2
relative_error_E_V = (dE_dV * delta_V / V)**2

# Total relative error in E
total_relative_error_E = np.sqrt(relative_error_E_P1 + relative_error_E_P0 + relative_error_E_V)

# Largest source of error
largest_error_source = max(relative_error_E_P1, relative_error_E_P0, relative_error_E_V)

total_relative_error_E, largest_error_source, delta_V  # Returning total relative error, largest source, and delta_V

print(f'P0 {relative_error_E_P0}\nP1 {relative_error_E_P1}\nV {relative_error_E_V}')