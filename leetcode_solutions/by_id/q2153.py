# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2153
标题: Subtree Removal Game with Fibonacci Tree
难度: hard
链接: https://leetcode.cn/problems/subtree-removal-game-with-fibonacci-tree/
题目类型: 树、数学、动态规划、二叉树、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2005. 斐波那契树的移除子树游戏 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们需要计算每个节点的最大得分，并且在每一步中选择最优的子树进行移除。

算法步骤:
1. 定义一个递归函数 `dp` 来计算以某个节点为根的子树的最大得分。
2. 对于每个节点，计算其左子树和右子树的最大得分。
3. 选择最优的子树进行移除，并更新当前节点的最大得分。
4. 返回根节点的最大得分。

关键点:
- 使用记忆化递归来避免重复计算。
- 在每一步中选择最优的子树进行移除。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只会被访问一次。
空间复杂度: O(n)，递归调用栈的深度最多为 n，并且使用了额外的字典来存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def dp(node: Optional[TreeNode], memo: dict) -> int:
    if not node:
        return 0
    if node in memo:
        return memo[node]
    
    left_score = dp(node.left, memo)
    right_score = dp(node.right, memo)
    
    # 选择最优的子树进行移除
    max_score = max(left_score + (node.val if node.left else 0),
                    right_score + (node.val if node.right else 0))
    
    memo[node] = max_score
    return max_score


def solution_function_name(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 计算斐波那契树的移除子树游戏的最大得分
    """
    memo = {}
    return dp(root, memo)


Solution = create_solution(solution_function_name)