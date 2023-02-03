

def successor(self, value):
        if self.value == value:
            if self.right is not None:
                return self.right.find_min()
            else:
                return None
        elif self.value > value:
            if self.left is not None:
                return self.left.successor(value)
            else:
                return None
        else:
            if self.right is not None:
                return self.right.successor(value)
            else:
                return None