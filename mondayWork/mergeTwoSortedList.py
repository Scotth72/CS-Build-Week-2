'''
https://leetcode.com/problems/merge-two-sorted-lists/
merge two sorted lists

merge two sorted linked list and return it as a new sorted list. The new list should be made by splicing together the nodes of the two lists.

Exmple:
Input: 1 -> 2 -> 4, 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

'''
# Defintintion for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # should we copy the lists before doing anything to them, or just mutate them directly?

        # don't forget to check that the inputs are None

        # attach on of the lists to the end of the other list
        # sort them
        # Sorting incurs a runtime fo O(n log n)
        # We wouldn't be able to use any built-in sorting methods
        # So we'd be able to implement it ourself

        # What is the best possible we can achieve for this problem?
        # We traversed each list once?
        # Added each node to a new list

        # init a new linked list
        new_list = ListNode(None)
        # variable to keep track of where we are in the new list
        current_new = new_list
        # keep track of the two current nodes, l1 and l2

        # traverse along both linked lists
        while l1 is not None and l2 is not None:
            # compare the two values that l1 and l2 are referring to
            if l2.val <= l2.val:
                # update the new_list reference
                l1 = l2.next
            else:
                current_new.next = ListNode(l2.val)
                l2 = l2.next
            current_new = current_new.next

        # append the lists and sort them
        # keep track of the two current nodes
        # traverse along both linked lists
            # compare the two values that l1 and l2 are referring to
            # take the smaller one and add it on to the end of a new linked list
        # once all of the nodes from one of the linked lists is added,
        # add all of the remaining nodes from the other list to the end of the new linked list
        # Runtime for this strategy is O(n + m) where n and m are the lengthhs of both link lists
