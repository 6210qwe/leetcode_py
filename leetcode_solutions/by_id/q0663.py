# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 663
标题: Equal Tree Partition
难度: medium
链接: https://leetcode.cn/problems/equal-tree-partition/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
663. 均匀树划分 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）计算每个子树的和，并检查是否存在一个子树的和等于整棵树和的一半。

算法步骤:
1. 使用 DFS 计算整棵树的和。
2. 再次使用 DFS 计算每个子树的和，并将这些和存储在一个集合中。
3. 检查是否存在一个子树的和等于整棵树和的一半。

关键点:
- 使用集合来存储子树的和，以便快速查找。
- 两次 DFS 分别用于计算整棵树的和和每个子树的和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。我们需要遍历整个树两次。
空间复杂度: O(n)，递归调用栈的空间和存储子树和的集合的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_target_sum(root: Optional[TreeNode], target: int) -> bool:
    if not root:
        return False
    if root.val == target and (not root.left and not root.right):
        return True
    return find_target_sum(root.left, target - root.val) or find_target_sum(root.right, target - root.val)

def get_tree_sum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return root.val + get_tree_sum(root.left) + get_tree_sum(root.right)

def check_equal_partition(root: Optional[TreeNode]) -> bool:
    total_sum = get_tree_sum(root)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    subsums = set()
    
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        current_sum = node.val + left_sum + right_sum
        subsums.add(current_sum)
        return current_sum
    
    dfs(root)
    return target in subsums

Solution = create_solution(check_equal_partition)