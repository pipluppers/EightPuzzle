import numpy as np      # Work with matrices
#   n x n board
n = 3
#   Example Boards
trivial = np.zeros((3, 3), int)
trivial[0][0] = 1; trivial[0][1] = 2; trivial[0][2] = 3
trivial[1][0] = 4; trivial[1][1] = 5; trivial[1][2] = 6
trivial[2][0] = 7; trivial[2][1] = 8; trivial[2][2] = 0

veryez = np.zeros((3, 3), int)
veryez[0][0] = 1; veryez[0][1] = 2; veryez[0][2] = 3
veryez[1][0] = 4; veryez[1][1] = 5; veryez[1][2] = 6
veryez[2][0] = 7; veryez[2][1] = 0; veryez[2][2] = 8

easy = np.zeros((3, 3), int)
easy[0][0] = 1; easy[0][1] = 2; easy[0][2] = 0
easy[1][0] = 4; easy[1][1] = 5; easy[1][2] = 3
easy[2][0] = 7; easy[2][1] = 8; easy[2][2] = 6

doable = np.zeros((3, 3), int)
doable[0][0] = 0; doable[0][1] = 1; doable[0][2] = 2
doable[1][0] = 4; doable[1][1] = 5; doable[1][2] = 3
doable[2][0] = 7; doable[2][1] = 8; doable[2][2] = 6

ohboy = np.zeros((3, 3), int)
ohboy[0][0] = 8; ohboy[0][1] = 7; ohboy[0][2] = 1
ohboy[1][0] = 6; ohboy[1][1] = 0; ohboy[1][2] = 2
ohboy[2][0] = 5; ohboy[2][1] = 4; ohboy[2][2] = 3

impossible = np.zeros((3, 3), int)
impossible[0][0] = 1; impossible[0][1] = 2; impossible[0][2] = 3
impossible[1][0] = 4; impossible[1][1] = 5; impossible[1][2] = 6
impossible[2][0] = 8; impossible[2][1] = 7; impossible[2][2] = 0

# goal_state = [[1,2,3],[4,5,6],[7,8,0]] for a 3x3      # 0 is the blank space
goal_state = np.zeros((n,n),int)
value = 1
for i in range (0,n):
    for j in range(0,n):
        if i < n-1 or j < n-1:
            goal_state[i][j] = value
        else:
            goal_state[i][j] = 0    # Put a zero at the end
        value = value + 1

def main():
    arr = np.zeros((n,n), int)
    type_of_puzzle = input('Welcome to Alex Nguyen\'s 8-puzzle solver.\nType "1" to use a '
                'default puzzle, or "2" to enter your own puzzle.\n')
    if type_of_puzzle == '1':
        default_choice = input("Choose a difficulty 1 (easiest) - 5 (hardest) "
                               "or 6 (impossible): \n")
        if default_choice == '1':
            arr = np.copy(trivial)
        elif default_choice == '2':
            arr = np.copy(veryez)
        elif default_choice == '3':
            arr = np.copy(easy)
        elif default_choice == '4':
            arr = np.copy(doable)
        elif default_choice == '5':
            arr = np.copy(ohboy)
        elif default_choice == 6:
            arr = np.copy(impossible)
    if type_of_puzzle == '2':
        print("\tEnter your puzzle, use a zero to represent the blank")
        top = input('\tEnter the first row, use a space or tabs between numbers:  ').split()    # Use split to ignore whitespaces
        mid = input('\tEnter the second row, use a space or tabs between numbers: ').split()
        bot = input('\tEnter the third row, use a space or tabs between numbers:  ').split()
        combine = [top, mid, bot]
        #   If n > 3 (aka a 15-puzzle or 24-puzzle, the next loop generates those inputs
        for x in range(3,n):
            top = input('\tEnter the next row, use a space or tabs between numbers:  ').split()
            combine.append(top)
        #   Copy everything in combine (which is all the inputs) into arr
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                arr[i][j] = combine[i][j]

    print('\n\tEnter your choice of algorithm:')
    type_of_algo = input('\t\t1. Uniform Cost Search.\n\t\t2. A* with the Misplaced Tile '
                'heuristic.\n\t\t3. A* with the Manhatten distance heuristic\n\n\t\t')
    if type_of_algo == '1':
        heuristic = UUCS
    if type_of_algo == '2':
        heuristic = misplaced_tile
    if type_of_algo == '3':
        heuristic = manhattan

    #   Generate the board node with 3 indexes: actual board, cost (g(n)), and remaining cost to win (h(n))
    board = [arr, 0, heuristic(arr)]
    #   Call the search algorithm
    search(board, heuristic)

#   Return the row and column of the blank space. Used in expand()
def blank_space(node):
    for i in range(0,n):
        for j in range(0,n):
            if node[i][j] == 0:
                return (i,j)

#   Display function
def print_state(node, firstCall):
    for i in range(0, len(node)):
        print('\t\t', end='')
        for j in range(0, len(node)):
            if node[i][j] == 0:
                print('b', end=' ')
            else:
                print(node[i][j], end=' ')
        if not firstCall:
            if i == len(node) - 1:
                print('\tExpanding this node...')
        print('\n', end='')

#   ---------------------------------   Heuristics  ---------------------------------
def UUCS(node):
    return 0

#   Calculates the number of incorrect locations
#   Ignores placement of blank tile
def misplaced_tile(node):
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if (node[i][j] != goal_state[i][j]) and node[i][j] != 0:
                count = count + 1
    return count

#   Distance the misplaced tile is from its required location
def manhattan(node):
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if (node[i][j] != goal_state[i][j]) and node[i][j] != 0:
                goal_i = 0
                goal_j = 0
                tmp = node[i][j]
                while tmp - n > 0:
                    goal_i = goal_i + 1
                    tmp = tmp - n
                goal_j = tmp - 1
                count = count + abs(goal_i - i) + abs(goal_j - j)
    return count
#   --------------------------------------------------------------------------------

#   Input: node, board, heuristic, row of blank space, column of blank space
#   Output: list of expanded nodes (Size is either 2 (corner), 3 (edge), or 4 (away from edge))
#   Expands the children of the node
def expand(actualnode, node, i, j):
    list_nodes = []
    start_node = np.copy(node) # Have to do this way. If used equal, it refers to same object (shallow copy)

    #   Check possible children
    if i < n -1:
        start_node[i][j] = node[i+1][j]         #   Move blank right
        start_node[i+1][j] = 0
        list_nodes.append([start_node, actualnode[1], actualnode[2]])
        start_node = np.copy(node)
    if j < n-1:
        start_node[i][j] = node[i][j+1]         #   Move blank down
        start_node[i][j+1] = 0
        list_nodes.append([start_node,actualnode[1], actualnode[2]])
        start_node = np.copy(node)
    if i > 0:
        start_node[i][j] = node[i-1][j]         #   Move blank left
        start_node[i-1][j] = 0
        list_nodes.append([start_node, actualnode[1], actualnode[2]])
        start_node = np.copy(node)
    if j > 0:
        start_node[i][j] = node[i][j-1]         #   Move blank up
        start_node[i][j-1] = 0
        list_nodes.append([start_node, actualnode[1], actualnode[2]])
    return list_nodes

#   Apply heuristic and increase the depth
def apply_depth_and_heuristic(expanded_nodes, heuristic):
    j = list(expanded_nodes)
    for i in range(0, len(j)):
        j[i][1] = expanded_nodes[i][1] + 1         # Add 1 to depth
        j[i][2] = heuristic(expanded_nodes[i][0])  # Apply heuristic to node
    return j

#   Inputs: Queue, list of nodes to expand, list of seen nodes, number of nodes we yet to see, heuristic
#   Ouputs: Queue, list of nodes we haven't seen, list of seen nodes, number of nodes we yet to see
#   Inserts the node into the queue in a sorted order (so we expand the least cost node only)
#   Queue is used to decide which node to expand next. It is a priority queue that only pops the beginning element
def add_to_queue(nodes_queue, nodes_expanded, encountered_nodes, nodes_not_seen, heuristic):
    unseen_nodes = []       #   Don't expand previously expanded nodes
    for i in range(0, len(nodes_expanded)):
        seen = False
        for j in range(0, len(encountered_nodes)):
            if np.array_equal(nodes_expanded[i][0], encountered_nodes[j][0]):   #Check if we've expanded this node before
                seen = True
                break       #   --------------------- Just added this (March 25, 2018) -----------------------------
        if not seen:
            unseen_nodes.append(nodes_expanded[i])
            nodes_not_seen = nodes_not_seen + 1

    if heuristic == UUCS:
        if len(unseen_nodes) > 0 and unseen_nodes[0][2] == 0:   # If not UUCS, it should
                                                            # have been goal state
            while len(unseen_nodes) > 0:
                nodes_queue.append(unseen_nodes.pop(0))           # Put first element in queue
    else:
        while len(unseen_nodes) > 0:
            added = False
            tmp = unseen_nodes.pop()
            if len(nodes_queue) == 0:
                nodes_queue.append(tmp)     #   If this is the first node, just add it to the queue
            else:
                for i in range(0, len(nodes_queue)):
                    if tmp[2] < nodes_queue[i][2]:          #   Try to find where to put the node such that it's still sorted
                        nodes_queue.insert(i, tmp)          #       by heuristic (since g(n) is equal for all nodes)
                        added = True
                        break
                if not added:                   # AKA LARGEST NUMBER. put at the end
                    nodes_queue.append(tmp)
    return nodes_queue, unseen_nodes, encountered_nodes, nodes_not_seen

#   General Search Algorithm A*. Works for any search
#   Input heuristic will be different depending on uniform cost search,
#       misplaced tile, or Manhatten
def search(node, heuristic):
    nodes = []                  # Make queue
    encountered_nodes = []      # Nodes we've seen before. Don't bother expanding
    #expanded_nodes = []         # Container for the expanded nodes (max size of 4)
    num_expanded_nodes = 0      #   Deleting this
    nodes_not_seen = 0  # used to increment num_expanded_nodes
    firstCall = True    # used for the printing of the nodes (aesthetics)

    #   Check if first node is the goal state
    if np.array_equal(node[0], goal_state):
        print("Goal!!\n")
        print("To solve this problem, the search algorithm expanded a total of 0 nodes.")
        print("The maximum number of nodes in the queue at any one time was 1.")
        print("The depth of the goal node was %d." % node[1])
        return node[0]

    #   Add to list of seen nodes, get the expanded nodes, and apply the depth and heuristic
    encountered_nodes.append(node)
    expanded_nodes = expand(node, node[0], blank_space(node[0])[0], blank_space(node[0])[1])
    expanded_nodes = apply_depth_and_heuristic(expanded_nodes, heuristic)
    nodes, expanded_nodes, encountered_nodes, nodes_not_seen = add_to_queue(nodes,
                            expanded_nodes, encountered_nodes, nodes_not_seen, heuristic)
    #   Update two performance metrics
    num_expanded_nodes = 0 + nodes_not_seen         #   Time complexity
    max_queue_size = len(nodes)                     #   Space complexity

    print('\nExpanding state: ')
    print_state(node[0], firstCall)
    firstCall = False               # No longer the first call to print_state
    print(end='\n')

    while len(nodes) > 0 and max_queue_size < 50000:
        checking = nodes.pop(0)            # Remove the first element in the queue

        #   Goal State Check
        if np.array_equal(checking[0], goal_state):
            print("Goal!!\n")
            print("To solve this problem, the search algorithm expanded a total of %d nodes." %
                  num_expanded_nodes)
            print("The maximum number of nodes in the queue at any one time "
                  "was %d." % max_queue_size)
            print("The depth of the goal node was %d." % checking[1])
            return checking[0]

        print('The best state to expand with a g(n) = %d and h(n) = %d' %
              (checking[1], checking[2]))
        print_state(checking[0], firstCall)

        #   We've now seen this node
        encountered_nodes.append(checking)
        #   Check its children and apply the depth and heuristic. Then add to the queue
        expanded_nodes = expand(checking, checking[0], blank_space(checking[0])[0],
                                 blank_space(checking[0])[1])
        expanded_nodes = apply_depth_and_heuristic(expanded_nodes, heuristic)
        add_to_queue(nodes, expanded_nodes, encountered_nodes, nodes_not_seen, heuristic)
        #   Update maximum queue size if the queue got larger than it. Measures our space usage
        if max_queue_size < len(nodes):
            max_queue_size = len(nodes)

        #   Print performance metrics
        #print("MAX QUEUE SIZE: %d" % max_queue_size)
        num_expanded_nodes = num_expanded_nodes + nodes_not_seen
        #print("NUM_EXPANDED NODES: %d" % num_expanded_nodes)

    print("Failure to find the solution\n")
    print("Expanded %d nodes" % num_expanded_nodes)
    print("The maximum number of nodes in the queue at any one time was %d." % max_queue_size)

#   Run main
if __name__ == "__main__":
    main()
