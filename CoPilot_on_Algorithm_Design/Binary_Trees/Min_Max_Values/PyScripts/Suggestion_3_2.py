

def find_min(self):
        if self.left is None:
            return self
        else:
            return self.left.find_min()"