# -*- coding:utf-8 -*-
"""链表节点定义及工具函数"""

from typing import List, Optional


class ListNode:
    """链表节点定义"""
    
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """打印链表"""
        return f"ListNode({self.to_list()})"
    
    @staticmethod
    def from_list(lst: List[int]) -> Optional['ListNode']:
        """
        将列表转为链表
        
        Args:
            lst: 整数列表
            
        Returns:
            链表头节点
            
        Example:
            >>> head = ListNode.from_list([1, 2, 3])
            >>> head.to_list()
            [1, 2, 3]
        """
        if not lst:
            return None
        dummy = ListNode()
        cur = dummy
        for num in lst:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next
    
    def to_list(self) -> List[int]:
        """
        将链表转为列表
        
        Returns:
            整数列表
            
        Example:
            >>> head = ListNode.from_list([1, 2, 3])
            >>> head.to_list()
            [1, 2, 3]
        """
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
    
    def __eq__(self, other):
        """支持链表比较"""
        if not isinstance(other, ListNode):
            return False
        return self.to_list() == other.to_list()

