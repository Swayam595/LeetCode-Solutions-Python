#### My Solution Using Hashtable ####
class FindElements:
    def __init__(self, root: TreeNode):
        self.hash_table = dict()
        self.decontaminate(root, 0)
        
    def decontaminate(self, root, value):
        if root == None:
            return
        else:
            root.val = value
            self.hash_table[value] = root
            l_val = 2 * value + 1
            self.decontaminate(root.left, l_val)
            r_val = 2 * value + 2
            self.decontaminate(root.right, r_val)
        
            
    def find(self, target: int) -> bool:
        if target in self.hash_table:
            return True
        else:
            return False
        
    def __del__(slef):
        del self.hash_table
        del self.root
