class Node:
    def __init__(self, data=None):
        """
        Initializes a new node with the given data and sets the next node to None.
        
        Parameters:
        data: The data to be stored in the node. Defaults to None if not provided.
        """
        self.data = data  # The data stored in the node.
        self.next = None  # Pointer to the next node in the linked list. Initialized to None.

    def __repr__(self):
        """
        Returns a string representation of the node.
        
        This method is used to provide a readable string representation of the node
        for debugging and logging purposes.
        
        Returns:
        str: A string in the format 'Node(data)'.
        """
        return f"Node({self.data})"  # String representation of the node.

    def set_next(self, next_node):
        """
        Sets the next node for the current node.
        
        Parameters:
        next_node (Node): The node to set as the next node.
        """
        self.next = next_node

    def get_next(self):
        """
        Gets the next node of the current node.
        
        Returns:
        Node: The next node.
        """
        return self.next

class mtf_algorithm:
    def __init__(self, values=None, requests=None):
        """
        Initializes the mtf_algorithm object with a list of values and constructs the initial linked list.
        
        Parameters:
        values: A list of values to initialize the linked list with. Defaults to None if not provided.
        requests: A list of values that will be searched for in the linked list using the Move-To-Front algorithm.
        """
        self.values = values  # The list of values to initialize the linked list.
        self.requests = requests  # The list of values to be searched in the linked list.
        self.head = None  # The head of the linked list, initially set to None.
        self.initConfigList()  # Initialize the linked list based on the provided values.

    def initConfigList(self):
        """
        Initializes the configuration of the linked list using the values provided.
        
        This method creates a linked list from the values list, setting up nodes and linking them together.
        """
        if not self.values:  # If no values are provided, exit the method.
            return
        
        # Create the head node
        self.head = Node(self.values[0])  # Initialize the head node with the first value.
        current_node = self.head  # Start with the head node as the current node.

        # Loop through the remaining values and create nodes
        for i in range(1, len(self.values)):
            node = Node(self.values[i])  # Create a new node with the current value.
            current_node.next = node  # Set the next pointer of the current node to the new node.
            current_node = node  # Move to the new node.

    def __repr__(self):
        """
        Returns a string representation of the linked list.
        
        This method traverses the linked list and constructs a string showing the sequence of nodes.
        
        Returns:
        str: A string representation of the linked list in the format 'Node(data) -> Node(data) -> ...'.
        """
        nodes = []  # List to store the string representations of the nodes.
        current_node = self.head  # Start with the head node.

        # Traverse the linked list and collect the string representations of the nodes
        while current_node:
            nodes.append(str(current_node))  # Add the string representation of the current node to the list.
            current_node = current_node.next  # Move to the next node.
        return " → ".join(nodes)  # Join the node representations with ' -> ' and return the result.

    def moveToFront(self):
        """
        Processes each request in the self.requests list by moving the corresponding node to the front
        of the linked list if found and prints the list after each request.
        """

        print(f"Initial Configuration List:\n{self}")
        total_cost = 0

        for et in self.requests:
            req_cost = 0
            current_node = self.head  # Start with the head node as the current node for each request.
            prev = None  # Previous node is initially set to None.

            while current_node:
                req_cost += 1
                if current_node.data == et:
                    if prev is not None:  # If the node to move is not already the head
                        prev.next = current_node.next  # Remove the node from its current position.
                        current_node.next = self.head  # Set the node's next to the current head.
                        self.head = current_node  # Update the head to be the current node.
                    break  # Node is moved to the front, break the inner loop.
                prev = current_node  # Move prev to the current node.
                current_node = current_node.next  # Move to the next node in the list.

            # Print the request, its cost and the current configuration of the list
            print(f"\nRequest: {et}, Cost: {req_cost}")
            print(f"List: {self}")
            total_cost += req_cost
        
        print(f"\nTotal Cost: {total_cost}")