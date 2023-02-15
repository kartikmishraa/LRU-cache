class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Node:
    def __init__(self, data):
        self.data = data    # data here is a Pair instance
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.root = Node(None)
        self.root.next = self.root
        self.root.prev = self.root

        self.len = 0    # Length of DLL


    # ------------------------------------------------
    # Description: Increment/Decrement DLL length by 1
    # ------------------------------------------------
    def up_len(self):
        self.len += 1
    def down_len(self):
        self.len -=  1


    #---------------------------------------------------------------
    # Description: Takes in node to be moved to the front of the DLL
    #---------------------------------------------------------------
    def move_front(self, node):    
        # None check
        if node is None:
            return None
        
        elif node.prev != None and node.next != None:
            # isolate the node
            node = self.isolate(node)

        # inserting in front
        self.root.next.prev = node
        node.next = self.root.next
        self.root.next = node
        node.prev = self.root


    # ---------------------------------------------------------------------------------
    # Description: Takes in data (Pair), makes a node of it and moves it to the front.
    #              Returns the newly created node.
    # ---------------------------------------------------------------------------------
    def insert(self, data):
        node = Node(data)
        self.move_front(node)
        self.up_len()

        return node


    # -------------------------------------------------------
    # Description: Pops out the tail of the queue (root.prev)
    #              Returns the popped out node
    # -------------------------------------------------------
    def pop_tail(self):
        node = self.root.prev
        node = self.isolate(node)
        self.down_len()

        return node

    # -------------------------------------------------
    # Description: Removes/Isolates a node from the DLL
    #              Returns the isolated node
    # -------------------------------------------------
    @staticmethod
    def isolate(node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

        return node

class Cache:
    def __init__(self, max_size = 20):
        if (max_size <= 0):
            raise Exception("Max size must be >= 0")
        
        self.max_size = max_size
        self.nodes = {} # Dictionary to store references to nodes in the DLL
        self.dll = DoublyLinkedList()

    # -------------------------------------------------------------------------------------
    # Description: Set/update data in the cache. 
    # 3 cases: (i) Data exists already (ii) Data doesn't exist already (ii.i) Cache is full
    # -------------------------------------------------------------------------------------
    def set(self, key, value):
        node = self.nodes.get(key)

        # Case (i)
        if node != None:
            node.data.value = value
            self.dll.move_front(node)
            return
        
        # Case (ii.i)
        if self.dll.len == self.max_size:
            popped = self.dll.pop_tail() 
            del self.nodes[popped.data.key]
        
        # Case (ii)
        self.nodes[key] = self.dll.insert(Pair(key, value))

    # -------------------------------------------
    # Description: Fetch data from cache. 
    # 2 cases: (i) Data found (ii) Data not found
    # -------------------------------------------
    def get(self, key):
        node = self.nodes.get(key)
        
        # Case (ii)
        if node is None:
            return None
        
        # Case (i)
        self.dll.move_front(node)
        return node.data.value
