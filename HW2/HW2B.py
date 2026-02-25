import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, ray) -> TreeNode:
        stack = [] # Stack to contain whole tree

        for element in ray: # Iterate through each element
            node = TreeNode(element) # Create node instance per element

            if element in "+-*/": # If it's an operator; works cause postfix lists can't start with an operators
                node.right = stack.pop() # Pop and connect right first (Stacks are LIFO)
                node.left = stack.pop() # Pop and connect left
                stack.append(node) # Push back in stack

            else: # If it's an operand
                stack.append(node) # Push back in stack

        return stack.pop() # Return root



    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        if head is None: # Base case 
            return [] 
        
        # Returning a list instead of using a global list 
        return [head.val] + self.prefixNotationPrint(head.left) + self.prefixNotationPrint(head.right) # Concatenates current, left subtree values and right subtree values 
        # Root -> left -> right

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        if head is None: 
            return [] 
    
        if head.left is None and head.right is None: # Check current node is a leaf
            return [head.val] # Return it with no parenthesis then
        
        # Returning list, current isn't leaf so add parenthesis 
        return ["("] + self.infixNotationPrint(head.left) + [head.val] + self.infixNotationPrint(head.right) + [")"] 
        # Left -> root -> right


    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        if head is None: 
            return [] 

        # Returning list 
        return self.postfixNotationPrint(head.left) + self.postfixNotationPrint(head.right) + [head.val] 
        # Left -> right -> root


class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        self.data = [] # List to contain elements
        self.top = -1 # Index of top element of stack (starts at -1 cause list is empty at this initialization)

    def push(self, value): # Push function
        self.top += 1 # Update index of top
        self.data.append(value) # Uses append from python lists kinda cheap

    def pop(self):
        if self.top == -1: # Check stack isn't empty
            raise IndexError("Empty stack") # Throw error
        
        self.top -= 1 # Update index of top
        return self.data.pop()

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self, exp: str) -> int:
        s = Stack()

        for token in exp.split(): # For each character in the expression string input
            if token in "+-/*":
                # Maintain correct left/right operand order
                b = s.pop() # Last element is second in expression 
                a = s.pop() # Fisrt element in expression
                # Handle every operator
                if token == "+":
                    s.push(a + b)
                elif token == "-":
                    s.push(a - b)
                elif token == "*":
                    s.push(a * b)
                elif token == "/":
                    if b == 0: # Handle division by 0
                        raise ZeroDivisionError("Division by zero")
                    s.push(a / b)
            else:
                s.push(float(token)) # Convert numbers to float when pushing them

        return s.pop()


# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('data/p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('data/p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('data/p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")