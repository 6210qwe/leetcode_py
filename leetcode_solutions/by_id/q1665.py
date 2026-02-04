# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1665
标题: Diameter of N-Ary Tree
难度: medium
链接: https://leetcode.cn/problems/diameter-of-n-ary-tree/
题目类型: 树、深度优先搜索
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一棵 N 叉树的根节点 root，计算这棵树的直径长度。N 叉树的直径是指树中任意两节点之间最长路径的长度。这条路径可能经过也可能不经过根节点。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，并在每个节点处计算其子树的最大深度。通过这些最大深度来更新当前的直径。

算法步骤:
1. 定义一个全局变量 `self.diameter` 用于存储当前找到的最大直径。
2. 定义一个递归函数 `dfs`，用于计算从当前节点出发的最大深度。
3. 在 `dfs` 函数中，对每个节点的子节点进行递归调用，并记录前两个最大的子树深度。
4. 更新 `self.diameter` 为当前节点的两个最大子树深度之和。
5. 返回当前节点的最大深度。

关键点:
- 使用递归函数 `dfs` 来计算每个节点的最大深度。
- 维护一个全局变量 `self.diameter` 来记录当前找到的最大直径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只会被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。这是由于递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import Node
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def __init__(self):
        self.diameter = 0

    def dfs(self, node: 'Node') -> int:
        if not node.children:
            return 1
        
        max_depth1, max_depth2 = 0, 0
        for child in node.children:
            depth = self.dfs(child)
            if depth > max_depth1:
                max_depth1, max_depth2 = depth, max_depth1
            elif depth > max_depth2:
                max_depth2 = depth
        
        self.diameter = max(self.diameter, max_depth1 + max_depth2)
        return max_depth1 + 1

    def diameter_of_n_ary_tree(self, root: 'Node') -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.diameter

Solution = create_solution(Solution)