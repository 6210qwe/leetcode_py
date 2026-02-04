# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1150
标题: Two Sum BSTs
难度: medium
链接: https://leetcode.cn/problems/two-sum-bsts/
题目类型: 栈、树、深度优先搜索、二叉搜索树、双指针、二分查找、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1214. 查找两棵二叉搜索树之和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将两棵二叉搜索树转换为有序数组，然后使用双指针在两个有序数组中查找目标值。

算法步骤:
1. 对两棵二叉搜索树进行中序遍历，生成两个有序数组。
2. 使用双指针在两个有序数组中查找是否存在两个数的和等于目标值。

关键点:
- 中序遍历二叉搜索树可以生成有序数组。
- 双指针可以在两个有序数组中高效查找目标值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是两棵树的节点数。中序遍历的时间复杂度是 O(n + m)，双指针查找的时间复杂度是 O(n + m)。
空间复杂度: O(n + m)，用于存储两个有序数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """中序遍历二叉搜索树，返回有序数组"""
    if not root:
        return []
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def two_sum_bsts(root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
    """
    判断两棵二叉搜索树中是否存在两个节点的值之和等于目标值
    """
    # 中序遍历生成有序数组
    nums1 = inorder_traversal(root1)
    nums2 = inorder_traversal(root2)
    
    # 双指针查找
    i, j = 0, len(nums2) - 1
    while i < len(nums1) and j >= 0:
        current_sum = nums1[i] + nums2[j]
        if current_sum == target:
            return True
        elif current_sum < target:
            i += 1
        else:
            j -= 1
    return False

Solution = create_solution(two_sum_bsts)