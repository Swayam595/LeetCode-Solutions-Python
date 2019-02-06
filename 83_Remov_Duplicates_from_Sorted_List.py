def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if head == None or head.next == None: return head   #   If the input list is empty or contains only one node then return head
        
        result = ListNode(None)     #   Create a node to store the address of the head
        result = head               #   Make address of the head and result as same
        temp = ListNode(None)       #   Crate a temp to stroe the node  next to the head node
        temp = head.next            #   Make temp node stroe the address of head node
        while temp:                 #   Iterate till temp node reaches the end of the list
            if head.val == temp.val:    #   If the head value is same as temp value then
                head.next = temp.next   #   Make head next point the next node to temp node
                temp = temp.next        #   make temp as temp next
                
            elif head.val != temp.val:  #   If the temp value and head value are not same then 
                head = temp             #   Make head as temp
                temp = temp.next        #   Make temp as temp next
        return result                   #   Return result 
