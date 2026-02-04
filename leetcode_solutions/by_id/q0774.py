# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 774
标题: Maximum Depth of N-ary Tree
难度: easy
链接: https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/
题目类型: 树、深度优先搜索、广度优先搜索
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
559. N 叉树的最大深度 - 给定一个 N 叉树，找到其最大深度。 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。 N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。 示例 1： [https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png] 输入：root = [1,null,3,2,4,null,5,6] 输出：3 示例 2： [https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png] 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] 输出：5 提示： * 树的深度不会超过 1000 。 * 树的节点数目位于 [0, 104] 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来计算 N 叉树的最大深度。

算法步骤:
1. 如果根节点为空，返回 0。
2. 初始化最大深度为 0。
3. 对每个子节点递归调用 DFS，并更新最大深度。
4. 返回最大深度加 1（当前节点）。

关键点:
- 递归地计算每个子节点的最大深度，并取其中的最大值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def max_depth(root: 'Node') -> int:
    """
    计算 N 叉树的最大深度
    """
    if not root:
        return 0
    
    max_depth = 0
    for child in root.children:
        max_depth = max(max_depth, max_depth(child))
    
    return max_depth + 1

Solution = create_solution(max_depth)