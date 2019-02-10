def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        if p == None or q == None: return (p==q)  #  If the current node is NULL in either tree then check wheather both the node 
                                                  #  of the trees are NULL is yes return true else false
    
        return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)) #  Check if current node values 
                                              #  of the trees are same if true then go to the next node and check there node valuse 
