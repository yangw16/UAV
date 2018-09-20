import neighbour
# import data.GeneratePointInCycle4 as generate
import data
import math
import func
import numpy as np
import matplotlib.pyplot as plt


error = math.pi/360
N = 20
R = 10000
L_max = 35
Num_tr = 4
theta_d = math.pi/36

info = data.GeneratePointInCycle4(N, R) 
neighbour_node,neighbour_dis,neighbour_theta,neighbour_divergence =  neighbour.neighbour(info,L_max,error)
# print neighbour_node[1],neighbour_theta[1]
# node_tr_theta = {tr:[math.pi*2/Num_tr*tr + theta_d/2] for tr in range(Num_tr)}

# node_tr_theta = {}
# for tr in range(Num_tr):
# 	node_tr_theta.update({tr:math.pi*2/Num_tr*tr + theta_d/2})
# node_tr_range = {tr:[math.pi*2/Num_tr*tr + theta_d/2 , math.pi*2/Num_tr*(tr+1) - theta_d/2] for tr in range(Num_tr)}
# # print node_tr_theta,'\n',node_tr_range
# tr_neighbours_node = func.tr_neighbours(neighbour_theta[1], node_tr_theta, node_tr_range, theta_d)
# print tr_neighbours_node

dict_tr_theta = {}
dict_tr_range = {}
for i in range(N):
	node_tr_theta = {}
	for tr in range(Num_tr):
		node_tr_theta.update({tr:math.pi*2/Num_tr*tr + theta_d/2})
	dict_tr_theta.update({i:node_tr_theta})
	node_tr_range = {tr:[math.pi*2/Num_tr*tr + theta_d/2 , math.pi*2/Num_tr*(tr+1) - theta_d/2] for tr in range(Num_tr)}
	dict_tr_range.update({i:node_tr_range})
# print dict_tr_range,'\n',dict_tr_theta

dict_net_tr_neighbours,link_list_tr_net = func.net_tr_neighbours(neighbour_theta,dict_tr_theta,dict_tr_range, theta_d)
link_edge_tr = func.edge_tr(link_list_tr_net)
print dict_net_tr_neighbours,'\n',link_list_tr_net,'\n',link_edge_tr




