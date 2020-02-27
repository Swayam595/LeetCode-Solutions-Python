class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue_1 = [root]
        level_max_sum = root.val
        result = 1
        level = 1
        
        while len(queue_1) != 0:
            queue_2 = []
            level_sum = 0
            for node in queue_1:
                if node.left:
                    queue_2.append(node.left)
                    level_sum += node.left.val
                if node.right:
                    queue_2.append(node.right)
                    level_sum += node.right.val
            queue_1 = queue_2
            level += 1
            if level_sum > level_max_sum:
                level_max_sum = level_sum
                result = level
        
        return result
