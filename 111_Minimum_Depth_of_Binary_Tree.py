##### Solution implementing depth first search######
def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return self.Depth(root, 1)
        
    def Depth(self, root: TreeNode, height: int) -> int:
        if root.left == None and root.right == None:
            return height
        else:
            l_h = 0
            r_h = 0
            if root.left:
                l_h = self.Depth(root.left, height + 1)
            if root.right:
                r_h = self.Depth(root.right, height + 1)
            
            if l_h and r_h:
                if l_h <= r_h: return l_h
                else: return r_h
            elif l_h: return l_h
            elif r_h: return r_h
            
            
            
##### Another Solution implementing breadth first search######
def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            queue1 = [root]
            curr_height = 1
        
            while len(queue1) != 0:
                queue2 = []
                i = 0
                while i < len(queue1):
                    if queue1[i].left == None and queue1[i].right == None:    
                        return curr_height
                    elif queue1[i].left or queue1[i].right:
                        if queue1[i].left:
                            queue2.append(queue1[i].left)
                        if queue1[i].right:
                            queue2.append(queue1[i].right)
                    i += 1
                curr_height += 1
                queue1 = queue2
