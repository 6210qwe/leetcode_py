# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3467
标题: Find the Level of Tree with Minimum Sum
难度: medium
链接: https://leetcode.cn/problems/find-the-level-of-tree-with-minimum-sum/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3157. 找到具有最小和的树的层数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）遍历树的每一层，并记录每层的节点值之和。最后找到和最小的层。

算法步骤:
1. 初始化一个队列，将根节点加入队列。
2. 初始化一个字典，用于存储每一层的节点值之和。
3. 使用 BFS 遍历树：
   - 对于队列中的每个节点，将其值加到当前层的和中。
   - 将该节点的子节点加入队列。
4. 遍历完成后，找到和最小的层并返回其索引。

关键点:
- 使用 BFS 可以逐层遍历树，并且可以方便地计算每层的节点值之和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只会被访问一次。
空间复杂度: O(w)，其中 w 是树的最大宽度。队列中最多会存储一层的所有节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_level_with_minimum_sum(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 找到具有最小和的树的层数
    """
    if not root:
        return 0

    from collections import deque

    queue = deque([(root, 0)])
    level_sums = {}

    while queue:
        node, level = queue.popleft()
        if level not in level_sums:
            level_sums[level] = 0
        level_sums[level] += node.val

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    min_sum = float('inf')
    min_level = 0
    for level, level_sum in level_sums.items():
        if level_sum < min_sum:
            min_sum = level_sum
            min_level = level

    return min_level


Solution = create_solution(find_level_with_minimum_sum)