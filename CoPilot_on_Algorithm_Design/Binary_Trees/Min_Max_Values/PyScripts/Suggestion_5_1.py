

def findMin(self):
        if self.left is None:
            return self
        else:
            return self.left.findMin()"