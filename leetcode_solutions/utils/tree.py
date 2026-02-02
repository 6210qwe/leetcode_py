# -*- coding:utf-8 -*-
"""树节点定义及工具函数"""

from typing import List, Optional, Any


class TreeNode:
    """二叉树节点定义"""
    
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        """打印树"""
        return f"TreeNode({self.val})"
    
    @staticmethod
    def from_list(lst: List[Optional[int]]) -> Optional['TreeNode']:
        """
        将列表转为二叉树（层序遍历格式）
        
        Args:
            lst: 层序遍历的节点值列表，None表示空节点
            
        Returns:
            二叉树根节点
            
        Example:
            >>> root = TreeNode.from_list([1, 2, 3, None, 5])
            >>> root.val
            1
        """
        if not lst or lst[0] is None:
            return None
        
        root = TreeNode(lst[0])
        queue = [root]
        i = 1
        
        while queue and i < len(lst):
            node = queue.pop(0)
            
            # 左子节点
            if i < len(lst) and lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            
            # 右子节点
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def to_list(self) -> List[Optional[int]]:
        """
        将二叉树转为列表（层序遍历格式）
        
        Returns:
            层序遍历的节点值列表
            
        Example:
            >>> root = TreeNode.from_list([1, 2, 3])
            >>> root.to_list()
            [1, 2, 3]
        """
        if not self:
            return []
        
        result = []
        queue = [self]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # 移除末尾的None
        while result and result[-1] is None:
            result.pop()
        
        return result
    
    def __eq__(self, other):
        """支持树比较"""
        if not isinstance(other, TreeNode):
            return False
        return self.to_list() == other.to_list()

