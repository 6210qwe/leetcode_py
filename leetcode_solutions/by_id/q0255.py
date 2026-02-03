# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 255
标题: Verify Preorder Sequence in Binary Search Tree
难度: medium
链接: https://leetcode.cn/problems/verify-preorder-sequence-in-binary-search-tree/
题目类型: 栈、树、二叉搜索树、递归、数组、二叉树、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
255. 验证二叉搜索树的前序遍历序列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈模拟前序遍历，维护下界

算法步骤:
1. 使用栈模拟BST的前序遍历
2. 维护一个下界lower，表示当前子树的最小值
3. 如果当前值小于下界，说明不是有效的BST前序遍历

关键点:
- 栈模拟前序遍历
- 维护下界
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历数组一次
空间复杂度: O(n) - 栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def verify_preorder(preorder: List[int]) -> bool:
    """
    函数式接口 - 验证二叉搜索树的前序遍历序列
    
    实现思路:
    使用栈模拟前序遍历，维护下界。
    
    Args:
        preorder: 前序遍历序列
        
    Returns:
        是否为有效的BST前序遍历
        
    Example:
        >>> verify_preorder([5,2,1,3,6])
        True
    """
    stack = []
    lower = float('-inf')
    
    for val in preorder:
        # 如果当前值小于下界，说明不是有效的BST
        if val < lower:
            return False
        
        # 弹出所有小于当前值的节点，更新下界
        while stack and stack[-1] < val:
            lower = stack.pop()
        
        stack.append(val)
    
    return True


# 自动生成Solution类（无需手动编写）
Solution = create_solution(verify_preorder)
