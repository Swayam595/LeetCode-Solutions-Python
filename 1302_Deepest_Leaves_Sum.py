#### My Solution using leetcode traversal ####
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sum_deepest_leaves = [0, 0]
        
        self.deepest_leaves_sum(root, sum_deepest_leaves, 0)
        
        return sum_deepest_leaves[1]
    
    def deepest_leaves_sum(self, root, sum_deepest_leaves, curr_height):
        curr_height += 1
        if root.left == None and  root.right == None:
            if curr_height > sum_deepest_leaves[0]:
                sum_deepest_leaves[0] = curr_height
                sum_deepest_leaves[1] = root.val
            elif curr_height == sum_deepest_leaves[0]:
                sum_deepest_leaves[1] += root.val
            return
        else:
            if root.left: 
                self.deepest_leaves_sum(root.left, sum_deepest_leaves, curr_height)
            if root.right: 
                self.deepest_leaves_sum(root.right, sum_deepest_leaves, curr_height)
            return

#### Leetcode Solution using Breadth First Search Traversal ####
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        tree = []
        if not root:
            return 0
        
        queue = [root]
        while queue:
            next_level = []
            current_level = []
            for node in queue:
                current_level.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            tree.append(current_level)
            queue = next_level
        
        return sum(tree[-1])
