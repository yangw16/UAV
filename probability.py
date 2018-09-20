
import math
import numpy as np
import matplotlib.pylab as plt


Ltheta_C = float(10.0/360.0*math.pi*2)*float(100.0)
# theta = float(10.0/360.0*math.pi*2)
# L = float(100.0)
# r = math.pi*L**2
R = float(3*10**2)
Omega = float(5.0/360.0)
# print theta,Omega
# T_max = (2*math.pi - theta)/Omega
m = 10

# t_list = np.linspace(0,T_max,100)

# print t_list

def prob_t(t,theta):
	L = Ltheta_C/theta
	r = math.pi*L**2
	# T_max = (2*math.pi - theta)/Omega
	prob = []
	E_num = []
	for k in range(m):
		C_mk = math.factorial(m)/(math.factorial(k)*math.factorial(m-k))
		prob_k = C_mk*((r/R)**k)*((1-r/R)**(m-k))*(((Omega*t+theta)/(math.pi*2))**k)
		num_k = prob_k*k
		# print prob_k,num_k,k
		prob.append(prob_k)
		E_num.append(num_k)
	return sum(prob),sum(E_num)

theta1 = float(10.0/360.0*math.pi*2)
theta2 = 2*theta1

def  theta_plot(theta):
	T_max = (2*math.pi - theta)/Omega
	t_list = np.linspace(0,T_max,100)
	prob_t_list = []
	E_num_t_list = []
	for t in t_list:
		prob_return,E_num_return = prob_t(t, theta)
		# print prob_return,E_num_return
		prob_t_list.append(prob_return)
		E_num_t_list.append(E_num_return)

		# prob_t_list.append(prob_t(t,theta))
	plt.plot(t_list,prob_t_list)
	# plt.plot(t_list,E_num_t_list)
# theta_list = [theta1,2*theta1,3*theta1,4*theta1,5*theta1,6*theta1,7*theta1]
theta_list = [11*theta1,12*theta1,14*theta1,16*theta1]
print theta_list

for theta in theta_list:
	L = Ltheta_C/theta
	r = math.pi*L**2
	print L,r,'\n'
	theta_plot(theta)

plt.show()



