# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 272
标题: Closest Binary Search Tree Value II
难度: hard
链接: https://leetcode.cn/problems/closest-binary-search-tree-value-ii/
题目类型: 栈、树、深度优先搜索、二叉搜索树、双指针、二叉树、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
272. 最接近的二叉搜索树值 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 中序遍历BST，使用双端队列维护k个最接近的值

算法步骤:
1. 中序遍历BST，得到有序数组
2. 使用双端队列维护k个最接近target的值
3. 返回队列中的值

关键点:
- 中序遍历
- 双端队列
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有节点
空间复杂度: O(k) - 队列空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def closest_k_values(root: Optional[TreeNode], target: float, k: int) -> List[int]:
    """
    函数式接口 - 最接近的二叉搜索树值 II
    
    实现思路:
    中序遍历BST，使用双端队列维护k个最接近的值。
    
    Args:
        root: BST根节点
        target: 目标值
        k: 返回k个值
        
    Returns:
        k个最接近target的值
        
    Example:
        >>> root = TreeNode(4)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(5)
        >>> closest_k_values(root, 3.714286, 2)
        [3, 4]
    """
    queue = deque()
    
    def inorder(node: Optional[TreeNode]):
        """中序遍历"""
        if not node:
            return
        
        inorder(node.left)
        
        if len(queue) < k:
            queue.append(node.val)
        else:
            # 如果当前值更接近target，替换最远的
            if abs(node.val - target) < abs(queue[0] - target):
                queue.popleft()
                queue.append(node.val)
            else:
                # 后面的值只会更远
                return
        
        inorder(node.right)
    
    inorder(root)
    return list(queue)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(closest_k_values)
