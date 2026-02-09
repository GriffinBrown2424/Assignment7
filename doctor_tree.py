class DoctorNode:
    """
    Represents a doctor in the reporting hierarchy.
    """
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """
    Manages the binary tree structure of doctor reports.
    """
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        if self.root is None:
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_name:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(doctor_name)
                return True
            if side == "right" and current_node.right is None:
                current_node.right = DoctorNode(doctor_name)
                return True
            return False

        found = False
        if current_node.left:
            found = self.insert(parent_name, doctor_name, side, current_node.left)
        if not found and current_node.right:
            found = self.insert(parent_name, doctor_name, side, current_node.right)

        return found

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
