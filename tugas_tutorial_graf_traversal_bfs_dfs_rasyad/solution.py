from copy import deepcopy
from queue import PriorityQueue
from time import time

num_of_instances = 0

def generate_heuristic(state, goal_state):
    heuristic = 0
    for num in range(9):
        if state.index(str(num)) != goal_state.index(str(num)):
            distance1 = state.index(str(num))
            distance2 = goal_state.index(str(num))
            i1 = int(distance1 / 3)
            j1 = int(distance1 % 3)
            i2 = int(distance2 / 3)
            j2 = int(distance2 % 3)
            distance = abs((i1 + j1) - (i2 + j2))
            heuristic += distance
    return heuristic

def goal_test(state, goal_state):
    return state == goal_state

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

def generate_child(state, path_cost, parent, needs_heuristic, goal_state):
    global num_of_instances
    children = []
    x = state.index('0')
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
        heuristic = generate_heuristic(new_state, goal_state) if needs_heuristic else None
        evaluation_function3 = heuristic if heuristic is not None else None
        child = (new_state, action, new_path_cost, parent, heuristic, None, evaluation_function3)
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

def greedy_best_first_search(initial_state, goal_state):
    global num_of_instances
    count = 0
    explored = []
    start_node = (initial_state, None, 0, None, generate_heuristic(initial_state, goal_state), None, generate_heuristic(initial_state, goal_state))
    q = PriorityQueue()
    q.put((start_node[6], count, start_node))

    while not q.empty():
        node = q.get()[2]
        explored.append(node[0])
        if goal_test(node[0], goal_state):
            return find_solution(node)

        children = generate_child(node[0], node[2], node, True, goal_state)
        for child in children:
            if child[0] not in explored:
                count += 1
                q.put((child[6], count, child))
    return

def read_board_state(path):
    state_str = open(path, 'r').readline()
    board_state = state_str.split(',')
    return board_state

def print_board_state(board):
    for row in range(0, 7):
        if(row % 2 == 0):
            print('+-----+-----+-----+')
        else:
            start_id = (row//2)*3
            print(f'|{board[start_id]:>{3}}  |{board[start_id+1]:>{3}}  |{board[start_id+2]:>{3}}  |')

def move_atas(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id+3]
    new_state[current_zero_id+3] = '0'
    return new_state

def move_bawah(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id-3]
    new_state[current_zero_id-3] = '0'
    return new_state

def move_kiri(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id+1]
    new_state[current_zero_id+1] = '0'
    return new_state

def move_kanan(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id-1]
    new_state[current_zero_id-1] = '0'
    return new_state

def update_queue_and_visited(queue, visited, new_state, move, current_state_key):
    visited_key = ','.join(new_state)
    if visited.get(visited_key) == None:
        queue.append([new_state, move])
        visited[visited_key] = [True, current_state_key, move]

def BFS(init_state, goal_state):
    queue = [[init_state, None]]
    visited = {','.join(init_state): True}
   
    while queue:
        current_state, move = queue[0]
        current_state_key = ','.join(current_state)
        queue.pop(0)
        current_zero_id = current_state.index('0')

        if current_state == goal_state:
            print('found solution')
            break

        if current_zero_id < 6:
            new_state = move_atas(current_state, current_zero_id)
            update_queue_and_visited(queue, visited, new_state, 'up', current_state_key)
        
        if current_zero_id > 2:
            new_state = move_bawah(current_state, current_zero_id)
            update_queue_and_visited(queue, visited, new_state, 'down', current_state_key)

        if current_zero_id % 3 < 2:
            new_state = move_kiri(current_state, current_zero_id)
            update_queue_and_visited(queue, visited, new_state, 'left', current_state_key)

        if current_zero_id % 3 > 0:
            new_state = move_kanan(current_state, current_zero_id)
            update_queue_and_visited(queue, visited, new_state, 'right', current_state_key)

    path_key = ','.join(goal_state)
    init_key = ','.join(init_state)
    paths = []
    while path_key != init_key:
        _, new_key, move = visited[path_key]
        paths.append((new_key, move))
        path_key = new_key

    counter = 1
    for state_key, move in paths[::-1]:
        state = state_key.split(',')
        print(f'{counter}. Move: {move}')
        counter += 1

def main():
    init_state = read_board_state('start.txt')
    goal_state = read_board_state('goal.txt')
    print('START')
    print_board_state(init_state)
    print('GOAL')
    print_board_state(goal_state)

    print('Begin search ... ')

    global num_of_instances
    num_of_instances = 0
    t0 = time()
    solution = greedy_best_first_search(init_state, goal_state)
    t1 = time() - t0
    print('Found solution:')
    for count, move in enumerate(solution):
        print(f'{count}. Move: {move}')
    print('Space  :', num_of_instances)
    print('Time   :', t1, 'ms')

if __name__ == "__main__":
    main()
