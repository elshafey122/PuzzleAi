"""
search(intial_state):
	#node{ state , path , ..... }
	initialize fringe with intital state
	while fringe is not empty :
		pick a node from the fringe according to a strategy
		--if visited : continue
		if goal : return solution
		from state get possible actions
		from actions generate next states
		append successors to the fringe
	return failure 
"""
from puzzle8 import *
from functions import *

# def solve(strategy,initial_state):
# 	fringo=[]
# 	visited=[]
# 	currentnode=initial_node(strategy,initial_state)
# 	fringo.append(currentnode)
# 	while len(fringo)>0 :
# 		print(currentnode)
# 		currentnode=fringo.pop(selectnode(strategy,fringo))
# 		if currentnode['state'] in visited:continue
# 		visited.append(currentnode)
# 		if isgoal(currentnode['state']):
# 			return get_solution(strategy,currentnode,len(visited))
# 		possible_actions=get_actions(currentnode['state'])
# 		for action in possible_actions:
# 			nextnode=add_node(strategy,currentnode['state'],action)
# 			fringo.append(nextnode)
# 	return None
#
#
#
#
# def get_actions(puzzle):
# 	moves=[
# 		['>','٧'],['<','>','٧'],['<','٧'],
# 		['٧','^','>'],['^','٧','>','<'],['<','^','٧'],
# 		['^','>'],['<','>','^'],['<','^']
# 	]
# 	print(puzzle)
# 	if(puzzle.index(0)==0):
# 		return moves[0]
# 	elif(puzzle.index(0)==1):
# 		return moves[1]
# 	elif (puzzle.index(0) == 2):
# 		return moves[2]
# 	elif (puzzle.index(0) == 3):
# 		return moves[3]
# 	elif (puzzle.index(0) == 4):
# 		return moves[4]
# 	elif (puzzle.index(0) == 5):
# 		return moves[5]
# 	elif (puzzle.index(0) == 6):
# 		return moves[6]
# 	elif (puzzle.index(0) == 7):
# 		return moves[7]
#
#
# def add_node(strtegy,current_node,action):
# 	next_node = {}
# 	next_node['state']=get_state(action,current_node['state'])
# 	next_node['path']=current_node['path'][:]; next_node['path'].append(action)
# 	if strtegy=='UCS':
# 		next_node['cost']=current_node['cost'] + getcost(action,current_node['state'])
# 	return next_node
#
#
# def getcost(currentnode,stregy):
# 	return 1
#
#
# def get_state(action,currentnode):
# 	print(currentnode)
# 	copiednode=currentnode[:]
#
# 	indix=currentnode.index(0)
# 	if(action=='>'):
# 		copiednode[indix]=copiednode[indix+1]
# 		copiednode[indix+1]=0
# 	elif(action=='<'):
# 		copiednode[indix]=copiednode[indix-1]
# 		copiednode[indix-1]=0
# 	elif (action == '^'):
# 		copiednode[indix] = copiednode[indix - 3]
# 		copiednode[indix - 3] = 0
# 	elif (action == '٧'):
# 		copiednode[indix] = copiednode[indix + 3]
# 		copiednode[indix + 3] = 0
#
# 	return copiednode
#
#
#
# def get_solution(stategy,puzzle,time):
# 	solution={}
# 	solution['state']=puzzle['state']
# 	solution['time']=time
# 	if(stategy=='UCS'):
# 		solution['cost']=puzzle['cost']
# 	return solution
#
#
#
#
#
# def isgoal(fringo):
# 	return fringo==[0,1,2,3,4,5,6,7,8,9]
#
# def selectnode(strategy,fringo):
# 	if(strategy=='BFS'):
# 		return 0
# 	elif(strategy=="DFS"):
# 		return -1
# 	elif(strategy=="UCS"):
# 		return get_min('cost',fringo)
#
# def get_min(key,fringo):
# 	min_idx=0
# 	for i in range (1,len(fringo)):
# 	   if(fringo[i][key]<fringo[min_idx][key]):
# 		   min_idx=i
# 	return  min_idx
#
#
#
#
#
# def initial_node(strategy,initial_state):
# 	initial_node={}
# 	initial_node['state']=initial_state
# 	initial_node['path']=[]
# 	if(strategy=='UCS'):
# 		initial_node['cost']=0
# 	return  initial_node
#















def solve(strategy,intial_state):
	fringe=[]; visited=[]
	initial_node=init_node(strategy,intial_state)
	fringe.append(initial_node)
	while len(fringe)>0:
		current_node=fringe.pop(select_node(strategy,fringe))
		if current_node['state'] in visited : continue
		visited.append(current_node['state'])
		#print(current_node['path']); #input()
		if isgoal(current_node['state']):
			return get_solution(strategy,current_node,len(visited))
		possible_actions=get_actions(current_node['state'])
		for action in possible_actions:
			next_node=add_node(strategy,current_node,action)
			fringe.append(next_node)
	return None

def select_node(strategy,fringe):
	if strategy == 'DFS': return -1
	if strategy == 'BFS': return 0
	if strategy == 'UCS': return get_min('cost',fringe)

def get_min(key,fringe):
	idx_min= 0
	for i in range(1,len(fringe)):
		if fringe[i][key] < fringe[idx_min][key] :
			idx_min=i
	return idx_min

def init_node(strategy,intial_state):
	initial_node = {}
	initial_node['state']=intial_state
	initial_node['path']=[]
	if strategy=='UCS': initial_node['cost']=0
	return initial_node

def add_node(strategy,current_node,action):
	next_node = {}
	next_node['state']=get_state(action,current_node['state'])
	next_node['path']=current_node['path'][:]; next_node['path'].append(action)
	if strategy=='UCS':
		next_node['cost']=current_node['cost'] + compute_cost(action,current_node['state'])
	return next_node

def get_solution(strategy,current_node,time):
	solution={}
	solution['solution']=current_node['path']
	solution['time']=time
	if strategy=='UCS':
		solution['cost']=current_node['cost']
	return solution

def compute_cost(action, state):
    return 1
