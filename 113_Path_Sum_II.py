def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if root == None: return []
        temp = [root.val]
        answer = list(list())
        self.paths(root, root.val, target, answer, temp)
        return answer

def paths(self, root, sum_of_path, target, answer, temp):
        if sum_of_path == target and not root.left and not root.right:
            answer += [temp.copy()]
            return True
        elif not root.left and not root.right:
            return True
        else:
            l_path = False
            r_path = False
            
            if root.left:
                temp.append(root.left.val)
                l_path = self.paths(root.left, sum_of_path + root.left.val, target, answer, temp)
                if l_path or r_path:
                    temp.pop()
            if root.right:
                temp.append(root.right.val)
                r_path = self.paths(root.right, sum_of_path + root.right.val, target, answer, temp)
                if r_path or l_path:
                    temp.pop()
                    
            return l_path or r_path
