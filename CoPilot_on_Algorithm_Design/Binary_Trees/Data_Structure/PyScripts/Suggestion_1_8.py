

class BST:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None
        self.vertices = []
        self.edges = []
        self.vertices.append(self)
        self.edges.append(self)
    def __str__(self):
        return str(self.value)
    def insert(self,value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
                self.left.parent = self
                self.left.vertices.append(self.left)
                self.edges.append(self.left)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
                self.right.parent = self
                self.right.vertices.append(self.right)
                self.edges.append(self.right)
        else:
            return False
    def search(self,value):
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.value:
            if self.right:
                return self.right.search(value)
            else:
                return False
        else:
            return True
    def findMin(self):
        if self.left:
            return self.left.findMin()
        else:
            return self
    def findMax(self):
        if self.right:
            return self.right.findMax()
        else:
            return self
    def findSuccessor(self):
        if self.right:
            return self.right.findMin()
        else:
            if self.parent:
                if self.parent.left == self:
                    return self.parent
                else:
                    return self.parent.findSuccessor()
            else:
                return None

