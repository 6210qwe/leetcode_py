# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1796
标题: Correct a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/correct-a-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1660. 纠正二叉树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS遍历，找到指向已访问节点的错误节点并删除

算法步骤:
1. 使用BFS遍历树
2. 记录已访问的节点
3. 如果发现某个节点的子节点已经被访问过，删除该连接

关键点:
- BFS遍历
- 哈希表记录已访问节点
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有节点
空间复杂度: O(n) - 队列和哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def correct_binary_tree(root: TreeNode) -> TreeNode:
    """
    函数式接口 - 纠正二叉树
    
    实现思路:
    BFS遍历：找到指向已访问节点的错误节点并删除。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        纠正后的根节点
        
    Example:
        >>> # 示例用法
    """
    visited = set()
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node.right:
            if node.right in visited:
                # 找到错误节点，删除
                node.right = None
            else:
                visited.add(node.right)
                queue.append(node.right)
        
        if node.left:
            if node.left in visited:
                # 找到错误节点，删除
                node.left = None
            else:
                visited.add(node.left)
                queue.append(node.left)
    
    return root


Solution = create_solution(correct_binary_tree)
