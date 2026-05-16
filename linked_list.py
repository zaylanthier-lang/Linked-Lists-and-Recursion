class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        - Use recursion to sum all node data in the list.
        """

        def helper(node):
            # Base case
            if node is None:
                return 0

            # Recursive case
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        - Reverse the list in-place using recursion.
        """

        def helper(prev, current):
            # Base case
            if current is None:
                return prev

            # Save next node
            next_node = current.next

            # Reverse pointer
            current.next = prev

            # Recursive call
            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """
        - Return True if 'target' is found, otherwise False, using recursion.
        """

        def helper(node):
            # Base case: end of list
            if node is None:
                return False

            # Base case: target found
            if node.data == target:
                return True

            # Recursive case
            return helper(node.next)

        return helper(self.head)

    def display(self):
        """
        - Print the contents of the list for debugging.
        """
        current = self.head
        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.next

        values.append("None")

        print(" -> ".join(values))


# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)

    print("Original List:")
    linked_list.display()

    print("\nRecursive Sum:")
    print(linked_list.recursive_sum())

    print("\nSearch for 30:")
    print(linked_list.recursive_search(30))

    print("\nSearch for 100:")
    print(linked_list.recursive_search(100))

    linked_list.recursive_reverse()

    print("\nReversed List:")
    linked_list.display()