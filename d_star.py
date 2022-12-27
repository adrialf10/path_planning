from manage_grid import *
import numpy as np
from math import dist

openList = []
closeList = []

#funciones modify node y remove node para los nodos que ya existen 

NEW = 0
OPEN = 1
CLOSED = 2
RAISED = 3
LOWER = 4
MAX_COST = 100000000000

def create_node(xy, color):
	node = dict()
	node['xy'] = xy
	node['backpoint'] = xy
	node['state'] = NEW
	node['h'] = 0
	node['k'] = 0
	node['isObstacle'] = is_obstacle(color)
	return node

def remove_node(node_list, node):
	for item in node_list:
		if item['xy'] == node['xy']:
			node_list.remove(item)
	newlist = sorted(node_list, key=lambda node: node['h'], reverse=True) 	
	return newlist
def add_node(node_list, node):
	for item in node_list:
		if item['xy'] == node['xy']:
			item['backpoint'] = node['backpoint']
			#si el coste ha cambiado reordenar
			break;
	node_list.append(node)
	newlist = sorted(node_list, key=lambda node: node['h'], reverse=True) 	
	return newlist	
def list_node_to_point(list_node):
	list_point = list()
	for node in list_node:
		list_point.append(node['xy'])
	return list_point

def get_state(node):
	return node['state']

def is_obstacle(color):
	if color != white and color != red and color != blue:
		return True
	return False
def exists(node_list, node_xy):
	for n in node_list:
		if n['xy'] == node_xy:
			return True
	return False
def get_neighbours_list(node, grid, closedList, openList):
	point_list = get_neighbours(grid, node['xy'])
	node_list = list()
	#print_neighbours(grid,point_list)
	for n in point_list:
		if (not exists(closeList,n[0]) and not exists(openList,n[0])):
			#print(f"El nodo {n[0]} no esta en closedList ni open lsit")
			new_node = create_node(n[0],n[1])
			c = get_cost(node, new_node) + node['h']
			new_node['h'] = c
			new_node['k'] = c
			new_node['backpoint'] = node['xy']
			node_list.append(new_node)
	return node_list

def get_distance(point_x, point_y):
	return dist(point_x, point_y)

def get_cost(node_prev, node_act):
	#Tener en cuenta obstaculo
	cost = get_distance(node_act['xy'], node_prev['xy'])
	return cost #node_prev['h'] + cost

def d_star(origin, goal, grid):
	initial_node = create_node(origin,red)
	grid.putpixel(origin, red)
	grid.putpixel(goal, red)


	goal_node = create_node(goal,red)
	openList.append(goal_node)
	finished = False
	while(not finished ):
		print(f"Closed listv{list_node_to_point(closeList)}")
		print(f"OPEN listv{list_node_to_point(openList)}")
		actual_node = openList[0]
		finished = expand(actual_node,initial_node, openList, closeList, grid)
	#grid.putpixel(openList[-1]['xy'], red)
	#grid.putpixel(closeList[-1]['xy'], blue)
	if 	len(closeList) > 0:
		path = get_optimal_path(closeList, grid)
		#print_path(grid, path)
	#la open list y por otra parte hay que calcular 

def expand(actual_node, initial_node,openList, closeList, grid):	
	#node es inicial -> stop
	#if k_old = h(actual_node, for each node del vecindario)

	#CLOSE ACTUAL NODE, EXPAND LOS OTROS
	

	if actual_node['xy'] == initial_node['xy']:
		actual_node['state'] = CLOSED
		closeList = add_node(closeList, actual_node)
		openList = remove_node(openList, actual_node)
		#print(openList)
		print('END')
		return True;
	neighbours_list = get_neighbours_list(actual_node,grid, closeList, openList)
	

	#print(f"El nodo a buscar: {actual_node['xy']}, los vecinos: {list_node_to_point(neighbours_list)}")
	for node in neighbours_list:
		#set h y k como distancias al goal
		
		#print(neighbours_list)
		if node['state'] == NEW or (node['backpoint'] == actual_node['xy'] and (node['h'] != actual_node['h'] + c)
		or node['backpoint'] != actual_node['xy'] and (node['h'] > actual_node['h'] + c) ):
			#si estado es nuevo o 
			#backpointer o parent es Y, y H(Y) != h(X) + coste
			#o si no es su padre y l coste de Y > h(X) + coste
			#print(node['xy'])
			#print(actual_node['xy'])
			#print('\n---------------------------\n')

			#print(f"{actual_node['xy']}: cost {actual_node['k']}, parent {actual_node['backpoint']}")
			
			#if node['k'] > actual_node['k']:
			if node['xy'] == (10,10):
				print(f"{node['xy']}: cost {node['k']}, parent {node['backpoint']}")
			
			node['backpoint'] = actual_node['xy']
			
			openList = add_node(openList, node)

			
			#openList.append(node)
			#backpoint = actual_node ,add vecino to open list
	actual_node['state'] = CLOSED
	closeList = add_node(closeList, actual_node)
	openList = remove_node(openList, actual_node)

	return False
	#print(openList)
	#print('\n---------------------------\n')



def get_optimal_path(node_list, grid):
	#get origin node, ie last item?
	path = list()
	aux_list = list(reversed(node_list))
	origin_node = aux_list[0]
	#print(origin_node)
	#[print(f"{node['xy']}\n") for node in aux_list]
	goal_node = aux_list[-1]
	#print(origin_node)
	#print(goal_node)

	backpoint_xy = origin_node['backpoint']
	#print(backpoint_xy)
	for node in aux_list:
		#print(f"Node: {node['xy']} Backpoint: {node['backpoint']}")
		if node['xy'] == goal_node['xy']:
			path.append(node['xy'])
			break
		elif node['xy'] == origin_node['xy']:
			path.append(node['xy'])
			backpoint_xy = origin_node['backpoint']
		elif node['xy'] == backpoint_xy:
			path.append(node['xy'])
			backpoint_xy = node['backpoint']
	#print(path)
	return path
		




	

