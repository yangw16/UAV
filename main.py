import neighbour
# import data.GeneratePointInCycle4 as generate
import data
import math
import numpy as np
import matplotlib.pyplot as plt



error = math.pi/36
N = 30
R = 10000
L_max = 35
# info = data.GeneratePointInCycle4(N, R)
pi = np.pi
theta = np.linspace(0, pi*2, 100)
R = 10000
x = 100 + np.sin(theta)*(R**0.5)
y = 100 + np.cos(theta)*(R**0.5)
 
plt.figure(figsize=(6,6))
plt.plot(x,y,label = "cycle",color="red",linewidth=2)
plt.title("cycyle")
# info = generate(N, R) 
info = data.GeneratePointInCycle4(N, R) 
neighbour_node,neighbour_dis,neighbour_theta,neighbour_divergence =  neighbour.neighbour(info,L_max,error)
print neighbour_node,'\n'
print neighbour_divergence,'\n'
print neighbour_theta
for node in neighbour_theta:
	print node,'\n'
# print info
plt.legend()
plt.show()