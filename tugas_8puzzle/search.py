#!/usr/bin/python
'Created by l3L4CK H4CK3l2'

from queue import PriorityQueue
from time import time
from queue import Queue

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
num_of_instances = 0

def generate_heuristic(state):
    heuristic = 0
    for num in range(9):
        if state.index(num) != goal.index(num):
            distance1 = state.index(num)
            distance2 = goal.index(num)
            i1 = int(distance1 / 3)
            j1 = int(distance1 % 3)
            i2 = int(distance2 / 3)
            j2 = int(distance2 % 3)
            distance = abs((i1 + j1) - (i2 + j2))
            heuristic += distance
    return heuristic

def goal_test(state):
    return state == goal

def find_legal_actions(i, j):
    legal_action = ['U', 'D', 'L', 'R']
    if i == 0:
        legal_action.remove('U')
    elif i == 2:
        legal_action.remove('D')
    if j == 0:
        legal_action.remove('L')
    elif j == 2:
        legal_action.remove('R')
    return legal_action

def generate_child(state, path_cost, parent, needs_heuristic):
    global num_of_instances
    children = []
    x = state.index(0)
    i = int(x / 3)
    j = int(x % 3)
    legal_actions = find_legal_actions(i, j)

    for action in legal_actions:
        new_state = state.copy()
        if action == 'U':
            new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
        elif action == 'D':
            new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
        elif action == 'L':
            new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
        elif action == 'R':
            new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
        
        new_path_cost = path_cost + 1
        heuristic = generate_heuristic(new_state) if needs_heuristic else None
        evaluation_function1 = heuristic + new_path_cost if heuristic is not None else None
        evaluation_function3 = heuristic if heuristic is not None else None
        child = (new_state, action, new_path_cost, parent, heuristic, evaluation_function1, evaluation_function3)
        children.append(child)
    num_of_instances += len(children)
    return children

def find_solution(path):
    solution = []
    while path:
        solution.append(path[1])
        path = path[3]
    solution = solution[:-1]
    solution.reverse()
    return solution

def Astar_search(initial_state):
    global num_of_instances
    count = 0
    explored = []
    start_node = (initial_state, None, 0, None, generate_heuristic(initial_state), None, None)
    start_node = (start_node[0], start_node[1], start_node[2], start_node[3], start_node[4], start_node[4] + start_node[2], start_node[4])
    q = PriorityQueue()
    q.put((start_node[5], count, start_node))

    while not q.empty():
        node = q.get()[2]
        explored.append(node[0])
        if goal_test(node[0]):
            return find_solution(node)

        children = generate_child(node[0], node[2], node, True)
        for child in children:
            if child[0] not in explored:
                count += 1
                q.put((child[5], count, child))
    return

def Greedy(initial_state):
    global num_of_instances
    count = 0
    explored = []
    start_node = (initial_state, None, 0, None, generate_heuristic(initial_state), None, generate_heuristic(initial_state))
    q = PriorityQueue()
    q.put((start_node[6], count, start_node))

    while not q.empty():
        node = q.get()[2]
        explored.append(node[0])
        if goal_test(node[0]):
            return find_solution(node)

        children = generate_child(node[0], node[2], node, True)
        for child in children:
            if child[0] not in explored:
                count += 1
                q.put((child[6], count, child))
    return

def breadth_first_search(initial_state):
    global num_of_instances
    start_node = (initial_state, None, 0, None, None, None, None)
    if goal_test(start_node[0]):
        return find_solution(start_node)
    q = Queue()
    q.put(start_node)
    explored = []
    while not q.empty():
        node = q.get()
        explored.append(node[0])
        children = generate_child(node[0], node[2], node, False)
        for child in children:
            if child[0] not in explored:
                if goal_test(child[0]):
                    return find_solution(child)
                q.put(child)
    return

state = [2, 6, 4, 8, 1, 3, 7, 5, 0]

num_of_instances = 0
t0 = time()
astar = Astar_search(state)
t1 = time() - t0
print('A*     :', astar)
print('Space  :', num_of_instances)
print('Time   :', t1 , 'ms')
print('-------------------------------------------------------------------------------------------------------------------------')

num_of_instances = 0
t0 = time()
greedy = Greedy(state)
t1 = time() - t0
print('Greedy :', greedy)
print('Space  :', num_of_instances)
print('Time   :', t1 , 'ms')
print('-------------------------------------------------------------------------------------------------------------------------')

num_of_instances = 0
t0 = time()
bfs = breadth_first_search(state)
t1 = time() - t0
print('BFS    :', bfs)
print('Space  :', num_of_instances)
print('Time   :', t1 , 'ms')
print('-------------------------------------------------------------------------------------------------------------------------')
