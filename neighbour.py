####neighbour nodes#####
import math
import numpy as np


#L_max = 25
divergence_L_max = math.pi/18  #### 25 meter divergence
#error = math.pi/36   ###### 5 degree--------  50m:  2.18m error
def neighbour(info,L_max,error):
    N = len(info)
    neighbour_node = {i:[] for i in range(N)}
    neighbour_dis = {i:{} for i in range(N)}
    neighbour_theta = {i:{} for i in range(N)} ### angle
    neighbour_divergence = {i:{} for i in range(N)} ###divergence
    #print type(neighbours.keys())
    for i in range(N):
        for j in range(N):
            if j != i:
                x = info[j]['pos'][0]-info[i]['pos'][0]
                y = info[j]['pos'][1]-info[i]['pos'][1]
                if x>0 and y>0:
                    theta = math.atan(y/x)
                elif x<0:
                    theta = math.atan(y/x)+math.pi
                else:
                    theta = math.atan(y/x)+math.pi*2

                dis_ij = math.sqrt((info[i]['pos'][0]-info[j]['pos'][0])**2+(info[i]['pos'][1]-info[j]['pos'][1])**2)
                if dis_ij < L_max:
                    neighbour_node[i].append(j)
                    neighbour_dis[i].update({j:dis_ij})
                    neighbour_theta[i].update({j:theta})
                    neighbour_divergence[i].update({j:L_max/dis_ij*divergence_L_max})

    return neighbour_node,neighbour_dis,neighbour_theta,neighbour_divergence
                

        
        
