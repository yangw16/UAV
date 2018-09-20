import matplotlib.pyplot as plt
import numpy as np
import math
import random


# def data(NumP, data_in):
# 	info = {i:[] for i in range(NumP)}
# 	for i in range(NumP):
# 		info[i] = {'pos':data_in[i]}
# 	return info


def GeneratePointInCycle4(point_num, radius):
	info = {i:[] for i in range(point_num)}
	for i in range(point_num):
		theta = random.random()*2*np.pi
		r = random.uniform(0, radius)
		x = 100 + math.sin(theta)* (r**0.5)
		y = 100 + math.cos(theta)* (r**0.5)
		plt.plot(x, y, '*', color = "black")
		info[i] = {'pos':(x,y)}
	return info 
 
 
