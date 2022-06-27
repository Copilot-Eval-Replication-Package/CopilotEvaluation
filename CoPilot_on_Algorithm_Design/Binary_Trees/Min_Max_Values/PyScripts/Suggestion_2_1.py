

def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

