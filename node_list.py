
def update_node(node, node_new):
	node['backpoint'] = node_new['backpoint']
	node['state'] = node_new['state']
	node['h'] = node_new['h'] 
	node['k'] = node_new['k']
	node['isObstacle'] = node_new['isObstacle']

def update_list(node_list):
	node_list.sort( key=lambda node: node['h'], reverse=False)  

def add_new_node(node_list, node):
	node_list.append(node)
	update_list(node_list)

def remove_node(node_list, node):
	node_list.remove(node)
	update_list(node_list)

def add_node(node_list, node):
	new = False
	for n in node_list:
		if n['xy'] == node['xy']:
			print('ya existe')
			#ya existe, modificar valores
			#update_node(n, node)
			n['backpoint'] = node['backpoint']
			n['state'] = node['state']
			n['h'] = node['h'] 
			n['k'] = node['k']
			n['isObstacle'] = node['isObstacle']
			update_list(node_list)
			#print(node_list)
			new = True
	if not new:     
		add_new_node(node_list, node)

def list_node_to_point(list_node):
	list_point = list()
	for node in list_node:
		list_point.append((node['xy'], node['h']))
	return list_point

def print_n(node_list):
	print( list_node_to_point(node_list) )

def exists(node_list, node_xy):
	for n in node_list:
		if n['xy'] == node_xy:
			return True
	return False