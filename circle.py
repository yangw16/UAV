import numpy as np
import matplotlib.pyplot as plt
import random
import math


def GeneratePointInCycle4(point_num, radius):
    for i in range(1, point_num+1):
        theta = random.random()*2*pi;
        r = random.uniform(0, radius)
        x = 100 + math.sin(theta)* (r**0.5)
        y = 100 + math.cos(theta)* (r**0.5)
        plt.plot(x, y, '*', color = "black")      
 
 
pi = np.pi
theta = np.linspace(0, pi*2, 100)
R = 10000
x = 100 + np.sin(theta)*(R**0.5)
y = 100 + np.cos(theta)*(R**0.5)
 
plt.figure(figsize=(6,6))
plt.plot(x,y,label = "cycle",color="red",linewidth=2)
plt.title("cycyle")
GeneratePointInCycle4(20, R) 
plt.legend()
plt.show()