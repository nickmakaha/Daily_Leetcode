# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        leader = head
        follower = head
        if(leader.next == None):
            return None
        for i in range(0,n):
            leader = leader.next
        print(head.val)
        if(leader == None):
            head = follower.next
            return head
        print(leader.val)
        skipOnce = True
        while(leader is not None):
            leader = leader.next
            if(skipOnce):
                #follower = follower.next
                skipOnce = False
            else:
                follower = follower.next

        print(follower.val)
        follower.next = follower.next.next
        return head
            


