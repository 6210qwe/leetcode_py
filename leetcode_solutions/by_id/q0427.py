# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 427
标题: 建立四叉树
难度: 中等
链接: https://leetcode.cn/problems/construct-quad-tree/
题目类型: 树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个 n * n 的二维矩阵 grid，其中每个值为 0 或 1。你需要将这个矩阵转换成一个四叉树。

四叉树的每个节点包含以下属性：
- val：表示该区域的值（0 或 1）。
- isLeaf：如果该节点是一个叶子节点，则为 True；否则为 False。
- topLeft、topRight、bottomLeft、bottomRight：指向四个子节点。

如果一个节点是叶子节点，那么它的所有子节点都为 null。

如果一个节点不是叶子节点，那么它的 val 为任意值，且它的四个子节点都不为 null。

构建四叉树的过程如下：
- 如果当前网格中的所有值都是相同的，或者网格大小为 1*1，那么该网格就是一个叶子节点。
- 否则，将网格划分为四个子网格，并递归地对每个子网格进行处理。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归构建四叉树

算法步骤:
1. 检查当前网格是否为叶子节点：如果所有值相同或网格大小为 1*1，则返回叶子节点。
2. 否则，将网格划分为四个子网格，并递归地对每个子网格进行处理。
3. 构建当前节点，并将其四个子节点设置为递归处理后的结果。

关键点:
- 通过递归处理子网格，确保每个节点的正确性。
- 优化时间和空间复杂度，避免不必要的重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 log n) - 每次递归处理的时间复杂度为 O(n^2)，递归深度为 O(log n)
空间复杂度: O(log n) - 递归调用栈的深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid: List[List[int]]) -> 'Node':
    """
    函数式接口 - 构建四叉树
    
    实现思路:
    递归构建四叉树，检查当前网格是否为叶子节点，如果不是则递归处理四个子网格。
    
    Args:
        grid: 二维矩阵，每个值为 0 或 1
        
    Returns:
        返回构建好的四叉树的根节点
        
    Example:
        >>> construct([[0, 1], [1, 0]])
        Node(1, False, Node(0, True, None, None, None, None), Node(1, True, None, None, None, None), Node(1, True, None, None, None, None), Node(0, True, None, None, None, None))
    """
    def is_leaf(grid, x, y, size):
        # 检查当前网格是否为叶子节点
        for i in range(x, x + size):
            for j in range(y, y + size):
                if grid[i][j] != grid[x][y]:
                    return False
        return True

    def build(grid, x, y, size):
        # 递归构建四叉树
        if is_leaf(grid, x, y, size):
            return Node(grid[x][y], True, None, None, None, None)

        half = size // 2
        topLeft = build(grid, x, y, half)
        topRight = build(grid, x, y + half, half)
        bottomLeft = build(grid, x + half, y, half)
        bottomRight = build(grid, x + half, y + half, half)

        return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

    return build(grid, 0, 0, len(grid))


# 自动生成Solution类（无需手动编写）
Solution = create_solution(construct)