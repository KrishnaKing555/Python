""" 
Program to calculate the drag force
by Krishna
"""
import matplotlib.pyplot as plt

#input

# Drag co-efficient 
c_d = 0.8


# Frontal area (m^2)
A = 0.1


# Density (kg/m^3)
rho = 1.2 


# Bicycle velocity 
veleocities = [5,6,7,8,9,10,11,12]
drag_forces = [] 


for velocity in veleocities:
    drag_forces.append((0.5*rho*A*c_d*velocity*velocity))

plt.plot(veleocities,drag_forces)
plt.xlabel('velocity')
plt.ylabel('Drag forces')
plt.show()  

