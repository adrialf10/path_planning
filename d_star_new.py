from manage_grid import *
import numpy as np
from math import dist
from node_list import *

openList = list()
closedList = list()

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

def get_distance(point_x, point_y):
	return dist(point_x, point_y)

def is_obstacle(color):
	return color != white and color != red and color != blue

def get_cost(node_prev, node_act):
	if node_act['isObstacle']:
		return MAX_COST
	else:
		return get_distance(node_act['xy'], node_prev['xy'])

def get_neighbours_list(node, grid, closedList, openList):
	point_list = get_neighbours(grid, node['xy'])
	node_list = list()
	#print_neighbours(grid,point_list)
	for n in point_list:
		if (not exists(closedList,n[0]) and not exists(openList,n[0])):
			#print(f"El nodo {n[0]} no esta en closedList ni open lsit")
			new_node = create_node(n[0],n[1])
			c = get_cost(node, new_node) + node['h']
			new_node['h'] = c
			new_node['k'] = c
			new_node['backpoint'] = node['xy']
			add_new_node(node_list, new_node)
	return node_list


def d_star(origin, goal, grid):
	goal_node = create_node(goal, red)
	origin_node = create_node(origin, red)

	grid.putpixel(origin, red)
	grid.putpixel(goal, red)

	add_new_node(openList, goal_node)
	i = 0

	finished = False
	while(len(openList) > 0 and not finished):
		actual_node = openList[0]
		finished = expand(actual_node, origin_node, openList,closedList, grid)
	#print('OPEN')
	#print_n(openList)
	#print('CLOSED')

	#print_n(closedList)

	path = get_optimal_path(closedList)
	print_path(grid, path)


def close_node(closedList, openList, node):
	node['state'] = CLOSED
	add_new_node(closedList, node)
	remove_node(openList, node)



def expand(actual_node, initial_node, openList, closedList, grid):
	#if k_old = h(actual_node, for each node del vecindario) -> ver significado todavia

	#si es el nodo final terminamos
	if actual_node['xy'] == initial_node['xy']:
		#print("END")
		close_node(closedList, openList, actual_node)
		return True
	#Sino calculamos los vecinos y cerramos el nodo
	neighbours_list = get_neighbours_list(actual_node, grid, closedList, openList)
	#print(f"Vecinos de {actual_node['xy']}")
	#print_n(neighbours_list)
	for node in neighbours_list:
		if not exists(closedList, node):
			if node['state'] == NEW:
				node['backpoint'] = actual_node['xy']
				#cOMPROBAR SINO ESTA EN LA OPEN LIST
				add_new_node(openList, node)
			else:
				continue
				#print(f"{node['xy']} in NOT NEW")
	close_node(closedList, openList, actual_node)
	return

def get_optimal_path(node_list):
	path = []
	reversed_nodes = list(reversed(node_list))
	start_node = reversed_nodes[0]
	goal_node = reversed_nodes[-1]
	backpoint = start_node['backpoint']
	path.append(start_node['xy'])
	for node in reversed_nodes:
		if node['xy'] == goal_node['xy']:
			path.append(node['xy'])
			break
		elif node['xy'] == backpoint:
			path.append(node['xy'])
			backpoint = node['backpoint']

	return path
		




	

