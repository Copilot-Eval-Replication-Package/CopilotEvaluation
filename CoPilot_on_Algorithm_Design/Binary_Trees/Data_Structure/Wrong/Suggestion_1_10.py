

class BST():
	# initialize an empty tree
	def __init__(self):
		self.value = None
		self.left = None
		self.right = None
		self.parent = None
		self.vertices = []
		self.edges = []

	# insert a new node into the tree
	def insert(self,new_node):
		# if the tree is empty
		if self.value == None:
			self.value = new_node
			return
		# if the tree is not empty
		if new_node.value < self.value:
			# if the left child is empty
			if self.left == None:
				self.left = new_node
				new_node.parent = self
				return
			# if the left child is not empty
			else:
				self.left.insert(new_node)
				return
		# if the new node is larger than the root
		if new_node.value > self.value:
			# if the right child is empty
			if self.right == None:
				self.right = new_node
				new_node.parent = self
				return
			# if the right child is not empty
			else:
				self.right.insert(new_node)
				return

	# find the node with the given value
	def find(self,value):
		# if the value is equal to the root
		if self.value == value:
			return self
		# if the value is less than the root
		if value < self.value:
			# if the left child is empty
			if self.left == None:
				return None
			# if the left child is not empty
			else:
				return self.left.find(value)
		# if the value is larger than the root"