# initial_capactity = 50

# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
    
# class HashTable:
#     def __init__(self):
#         self.capacity = initial_capactity
#         self.size = 0
#         self.buckets = [None]*self.capacity
    
#     def hash(self, key):
#         hashsum = 0
#         for idx, c in enumerate(key):
#             hashsum += (idx + len(key))**ord(c)
#             hashsum = hashsum % initial_capactity
#         return hashsum
    
#     def insert(self, key, value):
#         self.size += 1
#         index = self.hash(key)
#         node = self.buckets[index]
#         if node is None:
#             self.buckets[index] = Node(key, value)
#             return
#         prev = node
#         while node is not None:
#             prev = node
#             node = node.next
#         prev.next = Node(key, value)
    
#     def find(self, key):
#         index = self.hash(key)
#         node = self.buckets[index]
#         while node is not None and node.key != key:
#             node = node.next
#         if node is None:
#             return None
#         else:
#             return node.value
        
#     def remove(self, key):
#         index = self.hash(key)
#         node = self.buckets[index]
#         prev = node
#         while node is not None and node.key != key:
#             prev = node
#             node = node.next
#         if node is None:
#             return None
#         else:
#             self.size -= 1
#             result = node.value
#             if prev is None:
#                 pass
#             else:
#                 prev.next = prev.next.next
#             return result
    
# # Testing
# d = HashTable()
# d.insert('A', 5)
# d.insert('B', 10)
# d.insert('Ball', 'hello')
# d.insert('Bhai', 34.7)

# print(d.find('A'))
# print(d.find('Ball'))

# # print(d.remove('Bhai'))
# # print(d.find('Bhai'))
# print(d.remove('A'))
# print(d.find('A'))


# Capacity for internal array
INITIAL_CAPACITY = 50

# Node data structure - essentially a LinkedList node
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

# Hash table with separate chaining
class HashTable:
	# Initialize hash table
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity

	# Generate a hash for a given key
	# Input:  key - string
	# Output: Index from 0 to self.capacity
	def hash(self, key):
		hashsum = 0
		# For each character in the key
		for idx, c in enumerate(key):
			# Add (index + length of key) ^ (current char code)
			hashsum += (idx + len(key)) ** ord(c)
			# Perform modulus to keep hashsum in range [0, self.capacity - 1]
			hashsum = hashsum % self.capacity
		return hashsum

	# Insert a key,value pair to the hashtable
	# Input:  key - string
	# 		  value - anything
	# Output: void
	def insert(self, key, value):
		# 1. Increment size
		self.size += 1
		# 2. Compute index of key
		index = self.hash(key)
		# Go to the node corresponding to the hash
		node = self.buckets[index]
		# 3. If bucket is empty:
		if node is None:
			# Create node, add it, return
			self.buckets[index] = Node(key, value)
			return
		# 4. Iterate to the end of the linked list at provided index
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# Add a new node at the end of the list with provided key/value
		prev.next = Node(key, value)

	# Find a data value based on key
	# Input:  key - string
	# Output: value stored under "key" or None if not found
	def find(self, key):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return None
		else:
			# Found - return the data value
			return node.value

	# Remove node stored at key
	# Input:  key - string
	# Output: removed data value or None if not found
	def remove(self, key):
		# 1. Compute hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# 2. Iterate to the requested node
		while node is not None and node.key != key:
			prev = node
			node = node.next
		# Now, node is either the requested node or none
		if node is None:
			# 3. Key not found
			return None
		else:
			# 4. The key was found.
			self.size -= 1
			result = node.value
			# Delete this element in linked list
			if prev is None:
				node = None
			else:
				prev.next = prev.next.next
			# Return the deleted language
			return result

d = HashTable()
d.insert('A', 5)
d.insert('B', 10)
d.insert('Ball', 'hello')
d.insert('Bhai', 34.7)

# print(d.find('A'))
print(d.find('Ball'))

# print(d.remove('Bhai'))
# print(d.find('Bhai'))
print(d.remove('A'))
print(d.remove('A'))
print(d.remove('A'))
print(d.find('A'))