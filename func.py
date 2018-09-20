

def tr_neighbours(node_x,node_neighbours,node_tr_theta,node_tr_range,theta_d): #####node_neighbours_theta
	dict_tr_neighbours = {tr:{1:[],2:[]} for tr in node_tr_theta}
	link_list_tr = []
	for tr in node_tr_theta:
		for node in node_neighbours:  #####check if the neighbour node in tr normal range
			if ((node_neighbours[node] >= node_tr_range[tr][0]-theta_d/2) and (node_neighbours[node] < node_tr_range[tr][1]+theta_d/2)):
				dict_tr_neighbours[tr][2].append(node)
				link_list_tr.append((node_x,node,tr,2))

		if node_tr_theta[tr] < node_tr_range[tr][0]: ####check if the neighbour node in lower of range
			for node in node_neighbours:
				if ((node_neighbours[node] >= node_tr_theta[tr]-theta_d/2) and (node_neighbours[node] < node_tr_range[tr][0]+theta_d/2)):
					dict_tr_neighbours[tr][1].append(node)
					link_list_tr.append((node_x,node,tr,1))

		if node_tr_theta[tr] > node_tr_range[tr][1]: ####check if the neighbour node in upper of range
			for node in node_neighbours:
				print node_neighbours[node],node_tr_range[tr][1],node_tr_theta[tr]
				if ((node_neighbours[node] >= node_tr_range[tr][1]-theta_d/2) and (node_neighbours[node] < node_tr_theta[tr]+theta_d/2)):
					dict_tr_neighbours[tr][1].append(node)
					link_list_tr.append((node_x,node,tr,1))

	return dict_tr_neighbours,link_list_tr

def net_tr_neighbours(neighbours_theta,dict_tr_theta,dict_tr_range,theta_d):  #####single direction
	dict_net_tr_neighbours = {}
	link_list_tr_net = []
	for node in neighbours_theta:
		dict_tr_neighbours,link_list_tr= tr_neighbours(node,neighbours_theta[node],dict_tr_theta[node],dict_tr_range[node],theta_d)
		dict_net_tr_neighbours.update({node:dict_tr_neighbours})
		link_list_tr_net = link_list_tr_net + link_list_tr
	return dict_net_tr_neighbours,link_list_tr_net

def edge_tr(link_list_tr_net): #####double direction
	link_edge_tr = []
	for link_i in link_list_tr_net:
		for link_j in link_list_tr_net:
			if link_j != link_i:
				if (link_i[0] == link_j[1] and link_i[1] == link_j[0]):
					link_edge_tr.append((link_i[0],link_i[1],link_i[2],link_i[3],link_j[2],link_j[3]))
	return link_edge_tr

def edge_time(link_edge_tr,neighbours_theta,dict_tr_range,theta_d,omega_list,dict_tr_theta,omega_direction):
	link_edge_tr_time = []
	for link in link_edge_tr:
		omega = [omega_list[link[0]],omega_list[link[1]]]
		node_tr_theta = [dict_tr_theta[link[0]][link[2]],dict_tr_theta[link[1]][link[4]]]
		theta_range = [dict_tr_range[link[0]][link[2]],dict_tr_range[link[1]][link[4]]]
		relative_theta = [neighbours_theta[link[0]][link[1]],neighbours_theta[link[1]][link[0]]]
		omega_d = [omega_direction[link[0]][link[2]],omega_direction[link[1]][link[4]]]
		if link[3] == 1 or link[5] == 1:  ##### Time_algorithm1
			t = Time_algorithm1(link,relative_theta,theta_range,omega,theta_d,node_tr_theta,Tao,omega_d)
		else:                             ##### Time_algorithm2
			t = Time_algorithm2(link,relative_theta,theta_range,omega,theta_d,node_tr_theta,Tao,omega_d)
		link_edge_tr_time.append((link[0],link[1],link[2],link[4],t))
	return link_edge_tr_time

def Time_algorithm1(link,relative_theta,theta_range,omega,theta_d,node_tr_theta,Tao,omega_d):
	if link[3] == 1 and link[5] == 1:
		if node_theta_tr[0] < theta_range[0][0]:
			t_0 = [(relative_theta[0]-(node_tr_theta[0]+theta_d/2))/omega[0],(relative_theta[0]-(node_tr_theta[0]-theta_d/2))/omega[0]]
		if node_theta_tr[0] > theta_range[0][1]:
			t_0 = [((node_tr_theta[0]-theta_d/2)-relative_theta[0])/omega[0],((node_tr_theta[0]+theta_d/2)-relative_theta[0])/omega[0]]
		if node_theta_tr[1] < theta_range[1][0]:
			t_1 = [(relative_theta[1]-(node_tr_theta[1]+theta_d/2))/omega[1],(relative_theta[1]-(node_tr_theta[1]-theta_d/2))/omega[1]]
		if node_theta_tr[1] > theta_range[1][1]:
			t_1 = [((node_tr_theta[1]-theta_d/2)-relative_theta[1])/omega[1],((node_tr_theta[1]+theta_d/2)-relative_theta[1])/omega[1]]	
		######calculate time
		t = calculate_t(t_0,t_1)

	if link[3] == 1 and link[5] != 1:
		if node_theta_tr[0] < theta_range[0][0]:
			t_0 = [(relative_theta[0]-(node_tr_theta[0]+theta_d/2))/omega[0],(relative_theta[0]-(node_tr_theta[0]-theta_d/2))/omega[0]]
		if node_theta_tr[0] > theta_range[0][1]:
			t_0 = [((node_tr_theta[0]-theta_d/2)-relative_theta[0])/omega[0],((node_tr_theta[0]+theta_d/2)-relative_theta[0])/omega[0]]
		num = int(t_0[1]*omega[1]/(theta_range[1][1]-theta_range[1][0])/2)
		if num == 0:
			t_1 = 

def calculate_t(t_0,t_1):
	if t_0[1] <= t_1[0] or t_0[0] >= t_1[1]:  ####case 1 and case 2
		t = -1
	if t_0[1] > t_1[0] and t_0[1] < t_1[1] and t_1[0] > t_0[0]:   ####case 3
		t_len = t_0[1] - t_1[0]
		if t_len >=Tao:
			t = t_0[1]
	if t_0[1] >= t_1[1] and t_1[0] >= t_0[0]:    ####case 4
		t_len = t_1[1] - t_1[0]
		if t_len >=Tao:
			t = t_1[1]
		else:
			print 'wrong'
	if t_0[1] < t_1[1] and t_0[0] > t_1[0]:     #####case 5
		t_len = t_0[1] - t_0[0]
		if t_len >=Tao:
			t = t_0[1]
		else:
			print 'wrong'
	if t_0[1] > t_1[1] and t_0[0] < t_1[1] and t_0[0] > t_1[0]:   ####case 6
		t_len = t_1[0] - t_0[0]
		if t_len >=Tao:
			t = t_1[1]

	return t










