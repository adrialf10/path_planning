
def update_node(node, node_new):
	node['backpoint'] = node_new['backpoint']
	node['state'] = node_new['state']
	node['h'] = node_new['h'] 
	node['k'] = node_new['k']
	node['isObstacle'] = node_new['isObstacle']

def update_list(node_set):
	node_set.sort( key=lambda node: node['h'], reverse=False)  
	return

def add_new_node(node_set, node):
	node_set.append(node)
	update_list(node_set)

def remove_node(node_set, node):
	node_set.remove(node)
	update_list(node_set)

def add_node(node_set, node):
	new = False
	for n in node_set:
		if n['xy'] == node['xy']:
			#ya existe, modificar valores
			#update_node(n, node)
			n['backpoint'] = node['backpoint']
			n['state'] = node['state']
			n['h'] = node['h'] 
			n['k'] = node['k']
			n['isObstacle'] = node['isObstacle']
			update_list(node_set)
			#print(node_set)
			new = True
	if not new:     
		add_new_node(node_set, node)

def list_node_to_point(list_node):
	list_point = list()
	for node in list_node:
		list_point.append((node['xy'], node['h']))
	return list_point

def print_n(node_set):
	print( list_node_to_point(node_set) )

def exists(node_set, node_xy):
	for n in node_set:
		if n['xy'] == node_xy:
			return True
	return False