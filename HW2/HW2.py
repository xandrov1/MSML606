# Problem 1:
# Generate an expression tree (Binary tree) from a postfix expression
# Requirements:
# ➢ The input is a list of strings (e.g., [“3”, “4”, “+”, “2”, “*”]), which is parsed from a comma-separated CSV
# ➢ Support basic operators: +, -, *, and /
# ➢ Return the root node of the constructed expression tree

file = open("data\p1_construct_tree.csv", "r") # Open file to read

class Node: # Node class
    def __init__(self, data=None):
        self.data = data # Value store in node
        self.right = None # Connection to node's right
        self.left = None # Connection to node's left

def treeGenerator(ray): # Generates tree from list (postfix expression list)

    stack = [] # Stack to contain whole tree

    for element in ray: # Iterate through each element
        node = Node(element) # Create node instance per element

        if element in "+-*/": # If it's an operator
            node.right = stack.pop() # Pop and connect right first (Stacks are LIFO)
            node.left = stack.pop() # Pop and connect left
            stack.append(node) # Push back in stack
        else: # If it's an operand
            stack.append(node) # Push back in stack

    return stack.pop() # Return root

for line in file:

    node = treeGenerator(line.strip().split(",")) # Get root node with connections to other nodes
    print(f"Root node: {node}") # Print root

