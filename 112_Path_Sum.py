def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if root == None: return False
    
        return self.find_path(root, root.val, target)

    def find_path(self, root, sum_of_path, target):
        if root.left == None and root.right == None:
            return sum_of_path == target
        else:
            l_path = False
            r_path = False
            
            if root.left:
                l_path = self.find_path(root.left, sum_of_path + root.left.val, target)
            if l_path:
                return True
            if root.right:
                r_path = self.find_path(root.right, sum_of_path + root.right.val, target)
            if r_path:
                return True
            return False
