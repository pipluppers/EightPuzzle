import numpy as np      # Work with matrices

#   Queue module
#       queue.Queue(maxsize = 0) is FIFO
#       queue.LifoQueue(maxsize = 0) is LIFO
#       queue.PriorityQueue(maxsize = 0) returns lowest number first
#           pop the lowest heuristic value
#           maybe use this one for the 2 heursitics
#import queue

n = 3

# goal_state = [[1,2,3],[4,5,6],[7,8,0]]      # 0 is the blank space
# Create Goal State
goal_state = np.zeros((3,3),int)
value = 1
for i in range (0,n):
    for j in range(0,n):
        if i < 2 or j < 2:
            goal_state[i][j] = value
        else:
            goal_state[i][j] = 0
        value = value + 1

'''
function general_search(problem, QUEUEING_FUNCTION):
    nodes = make_queue(make_node(problem.INITIAL_STATE)
    do
        if empty(nodes):
            return failure
        node = REMOVE_FRONT(nodes)
        if (problem.GOAL_TEST(node.STATE) == true)
            return success and the node
        nodes = QUEUEING_FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
    end

'''

#   Expand the nodes. i and j are the indexes of the blank space
#   We look to expand downward and rightward first because blank space should be in bottom right
def expand(node, i, j):
    list_nodes = []
    start_node = np.copy(node) # Have to do this away. If used equal, it refers to same object

    if i < n -1:
        #print("First expanded node")
        start_node[i][j] = node[i+1][j]
        start_node[i+1][j] = 0
        #print(start_node)
        list_nodes.append(start_node)
        start_node = np.copy(node)
    if j < n-1:
        #print("Second expanded node")
        start_node[i][j] = node[i][j+1]
        start_node[i][j+1] = 0
        #print(start_node)
        list_nodes.append(start_node)
        start_node = np.copy(node)

    if i > 0:
        #print("Third expanded node")
        start_node[i][j] = node[i-1][j]
        start_node[i-1][j] = 0
        #print(start_node)
        list_nodes.append(start_node)
        start_node = np.copy(node)
    if j > 0:
        #print("Fourth expanded node")
        start_node[i][j] = node[i][j-1]
        start_node[i][j-1] = 0
        #print(start_node)
        list_nodes.append(start_node)
    return list_nodes

#   Return the row and column of the blank space
def blank_space(node):
    for i in range(0,n):
        for j in range(0,n):
            if node[i][j] == 0:
                return (i,j)

# Using FIFO Queue
def Uniform_Cost_Search(node):
    max_queue_size = 1
    depth = 1
    num_expanded_nodes = 0

    # Create the queue and test the compare the inputted node with the goal_state
    #   because there is no do-while loop in python
    nodes = []
    encountered_nodes = []
    if np.array_equal(node,goal_state):
        print("Found the state")
        print("MAX QUEUE SIZE: ", max_queue_size, "\n")
        print("DEPTH: ", depth, "\n")
        print("NUMBER OF EXPANDED NODES: ", num_expanded_nodes, "\n")
        return True

    # Add nodes to list of nodes that we've seen
    encountered_nodes.append(node)

    # Check if we've seen the expanded node already (shouldn't happen in first step)
    # Add in nodes as a 3-tuple (node, depth, heuristic (going to be 0 for UCS))
    expanded_nodes = expand(node, blank_space(node)[0], blank_space(node)[1])
    for i in range(0,len(expanded_nodes)):
        nodes.append(expanded_nodes[i])

    max_queue_size = len(nodes)     # Initially, the max size is just the size of the expanded nodes

    supplementaryqueuesize = 0      # Queue is currently empty (used to distinguish levels for depth)
    num_expanded_nodes = len(nodes) # Starts with number of children

    while len(nodes) != 0 and max_queue_size < 26000:

        # Get the number of nodes per level. Increase the depth if we're on a new level
        if supplementaryqueuesize == 0:
            supplementaryqueuesize = len(nodes) - 1
            depth = depth + 1
        else:
            supplementaryqueuesize = supplementaryqueuesize - 1

        # Dequeue the next node (since FIFO, its the one that came in first)
        curr_node = nodes.pop(0)

        #   Check if its the goal state
        if np.array_equal(curr_node, goal_state):
            print("Found the state")
            print("MAX QUEUE SIZE: ", max_queue_size)
            print("DEPTH: ", depth)
            print("NUMBER OF EXPANDED NODES: ", num_expanded_nodes, "\n")
            return True

        #   If not goal state, add to list of seen nodes
        encountered_nodes.append(curr_node)
        #print("Printing list of seen nodes:\n")
        #for i in range(0, len(encountered_nodes)):
        #    print(encountered_nodes[i])

        nodes_not_seen = 0
        expanded_nodes = expand(curr_node, blank_space(curr_node)[0], blank_space(curr_node)[1])
        for i in range(0, len(expanded_nodes)):
            #print("Checking this expanded node: \n", expanded_nodes[i],"\n\n")
            seen = False
            #   Compare expanded node with each of the nodes we've seen before
            for j in range(0, len(encountered_nodes)):
                if np.array_equal(expanded_nodes[i], encountered_nodes[j]):
                    #print("Never seen this node yet. Enqueueing it so we can expand it later")
                    #nodes.put(expanded_nodes[i])
                    #print("Seen this node before. Don't expand")
                    seen = True
            if not seen:
                #print("Never seen this node before. Enqueuing it")
                nodes.append(expanded_nodes[i])
                nodes_not_seen = nodes_not_seen + 1
            #else:
                #print("Seen this node before. Don't expand")
        if len(nodes) > max_queue_size:
            max_queue_size = len(nodes)
        num_expanded_nodes = num_expanded_nodes + nodes_not_seen
        print("SIZE OF QUEUE: ", len(nodes), "\n\n")

    # If we exited the for loop, that means the size of the queue is zero, and we have not
    #   found the goal state. Therefore, return failure
    print("Failure")
    print("MAX QUEUE SIZE: ", max_queue_size, "\n")
    print("DEPTH: ", depth, "\n")
    print("NUMBER OF EXPANDED NODES: ", num_expanded_nodes, "\n")
    return False

#   Nodes is a queue that contains the tuple (state, g(n) aka depth, h(n) aka heuristic)
'''
120
453
786

123 1   102 1
450     453
786     786

123 2
456
780


'''


#def search(node, heuristic)

trivial = np.zeros((3,3),int)
trivial[0][0] = 1; trivial[0][1] = 2; trivial[0][2] = 3
trivial[1][0] = 4; trivial[1][1] = 5; trivial[1][2] = 6
trivial[2][0] = 7; trivial[2][1] = 8; trivial[2][2] = 0

veryez = np.zeros((3,3),int)
veryez[0][0] = 1; veryez[0][1] = 2; veryez[0][2] = 3
veryez[1][0] = 4; veryez[1][1] = 5; veryez[1][2] = 6
veryez[2][0] = 7; veryez[2][1] = 0; veryez[2][2] = 8

easy = np.zeros((3,3),int)
easy[0][0] = 1; easy[0][1] = 2; easy[0][2] = 0
easy[1][0] = 4; easy[1][1] = 5; easy[1][2] = 3
easy[2][0] = 7; easy[2][1] = 8; easy[2][2] = 6

doable = np.zeros((3,3),int)
doable[0][0] = 0; doable[0][1] = 1; doable[0][2] = 2
doable[1][0] = 4; doable[1][1] = 5; doable[1][2] = 3
doable[2][0] = 7; doable[2][1] = 8; doable[2][2] = 6

ohboy = np.zeros((3,3),int)
ohboy[0][0] = 8; ohboy[0][1] = 7; ohboy[0][2] = 1
ohboy[1][0] = 6; ohboy[1][1] = 0; ohboy[1][2] = 2
ohboy[2][0] = 5; ohboy[2][1] = 4; ohboy[2][2] = 3

impossible = np.zeros((3,3),int)
impossible[0][0] = 1; impossible[0][1] = 2; impossible[0][2] = 3
impossible[1][0] = 4; impossible[1][1] = 5; impossible[1][2] = 6
impossible[2][0] = 8; impossible[2][1] = 7; impossible[2][2] = 0

print("\n\nTesting Board")
print("\nTesting Uniform Cost Search")
Uniform_Cost_Search(trivial)





def UUCS(node):
    return 0

# Calculates the number of tiles
# Ignores placement of blank tile
def misplaced_tile(node):
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if (node[i][j] != goal_state[i][j]) and node[i][j] != 0:
                count = count + 1
    return count

def manhatten(node):
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if (node[i][j] != goal_state[i][j]) and node[i][j] != 0:
                goal_i = 0
                goal_j = 0
                tmp = node[i][j]
                while tmp - n > 0:
                    goal_i = goal_i + 1
                    tmp = tmp - 3
                goal_j = tmp - 1
                count = count + abs(goal_i - i) + abs(goal_j - j)
    return count

def addToQueue(nodes, node, depth, heuristic):
    a = depth + 1
    b = heuristic(node)
    nodes.append(node, a, b)



#   actualnode = checking
#   node = checking[0]
#   i = blank space row
#   j = blank space col
def expand2(actualnode, node, i, j):
    list_nodes = []
    start_node = np.copy(node) # Have to do this away. If used equal, it refers to same object

    if i < n -1:
        start_node[i][j] = node[i+1][j]
        start_node[i+1][j] = 0
        list_nodes.append([start_node, actualnode[1], actualnode[2]])
        start_node = np.copy(node)
    if j < n-1:
        start_node[i][j] = node[i][j+1]
        start_node[i][j+1] = 0
        list_nodes.append([start_node,actualnode[1], actualnode[2]])
        start_node = np.copy(node)

    if i > 0:
        start_node[i][j] = node[i-1][j]
        start_node[i-1][j] = 0
        list_nodes.append([start_node, actualnode[1], actualnode[2]])
        start_node = np.copy(node)

    if j > 0:
        start_node[i][j] = node[i][j-1]
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


#   Check if size of nodes_expanded is greater than zero before calling this
#   Inserts the node into the queue in a sorted order
def add_to_queue(nodes_queue, nodes_expanded, encountered_nodes, nodes_not_seen, heuristic):
    unseen_nodes = []
    for i in range(0, len(nodes_expanded)):
        seen = False
        for j in range(0, len(encountered_nodes)):
            if np.array_equal(nodes_expanded[i][0], encountered_nodes[j][0]):
                seen = True
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
                nodes_queue.append(tmp)
            else:
                for i in range(0, len(nodes_queue)):
                    if tmp[2] < nodes_queue[i][2]:
                        nodes_queue.insert(i, tmp)
                        added = True
                        break
                if not added:                   # AKA LARGEST NUMBER. put at the end
                    nodes_queue.append(tmp)
    return nodes_queue, unseen_nodes, encountered_nodes, nodes_not_seen

def search(node, heuristic):
    nodes = []                  # Make queue
    encountered_nodes = []      # Nodes we've seen before. Don't bother expanding
    #expanded_nodes = []         # Container for the expanded nodes (max size of 4)
    #   Performance Metrics
    num_expanded_nodes = 0
    nodes_not_seen = 0  # used to increment num_expanded_nodes

    #   Check if first node is the goal state
    if np.array_equal(node[0], goal_state):
        print("Goal!!\n")
        print("To solve this problem, the search algorithm expanded a total of %d nodes." %
              num_expanded_nodes)
        print("The maximum number of nodes in the queue at any one time was 1.")
        print("The depth of the goal node was %d." % node[1])
        return node[0]

    #   Add to list of seen nodes
    encountered_nodes.append(node)
    expanded_nodes = expand2(node, node[0], blank_space(node[0])[0], blank_space(node[0])[1])
    expanded_nodes = apply_depth_and_heuristic(expanded_nodes, heuristic)
    nodes, expanded_nodes, encountered_nodes, nodes_not_seen = add_to_queue(nodes,
                            expanded_nodes, encountered_nodes, nodes_not_seen, heuristic)

    #   Update two metrics
    num_expanded_nodes = num_expanded_nodes + nodes_not_seen
    max_queue_size = len(nodes)

    print("Expanding state\n", node[0])
    print("---------------")
    print("SIZE OF QUEUE: ", len(nodes))
    while len(nodes) > 0:
        checking = nodes.pop(0)            # Remove the first element in the queue
        if np.array_equal(checking[0], goal_state):
            print("Goal!!\n")
            print("To solve this problem, the search algorithm expanded a total of %d nodes." %
                  num_expanded_nodes)
            print("The maximum number of nodes in the queue at any one time "
                  "was %d." % max_queue_size)
            print("The depth of the goal node was %d." % checking[1])
            return checking[0]
        encountered_nodes.append(checking)
        expanded_nodes = expand2(checking, checking[0], blank_space(checking[0])[0],
                                 blank_space(checking[0])[1])
        expanded_nodes = apply_depth_and_heuristic(expanded_nodes, heuristic)
        add_to_queue(nodes, expanded_nodes, encountered_nodes, nodes_not_seen, heuristic)
        if max_queue_size < len(nodes):
            max_queue_size = len(nodes)

        #print("MAX QUEUE SIZE: %d" % max_queue_size)
        num_expanded_nodes = num_expanded_nodes + nodes_not_seen
        #print("NUM_EXPANDED NODES: %d" % num_expanded_nodes)

        # TESTING
        '''
        print(len(nodes), "--------------------------------------------------")
        for i in range(0, len(nodes)):
            print(nodes[i][0])
            print("g(n) + h(n) = %d + %d = %d" %
                  (nodes[i][1], nodes[i][2], (nodes[i][1]+ nodes[i][2])))
        '''
    print("Failure to find the solution\n")
    print("Expanded %d nodes" % num_expanded_nodes)
    print("The maximum number of nodes in the queue at any one time was %d." % max_queue_size)


print('\nTesting blah')
print(misplaced_tile(trivial))
blah = [np.copy(ohboy), 1, manhatten(ohboy)]
print(blah[0])
print(search(blah, manhatten))


'''
example = np.zeros((3,3),int)
example[0][0] = 1; example[0][1] = 2; example[0][2] = 3
example[1][0] = 4; example[1][1] = 8; example[1][2] = 0
example[2][0] = 7; example[2][1] = 6; example[2][2] = 5

exam = [np.copy(example), 1, manhatten(example)]

print("\n\n\n\n\n")
print(search(exam, manhatten))
'''

'''
test = np.zeros((3,3),int)
test[0][0] = 1; test[0][1] = 2; test[0][2] = 0
test[1][0] = 0; test[1][1] = 5; test[1][2] = 0
test[2][0] = 4; test[2][1] = 8; test[2][2] = 0
print("Testing Manhatten Distance")
print(manhatten(test))
'''
