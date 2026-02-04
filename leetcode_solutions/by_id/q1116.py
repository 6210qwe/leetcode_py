# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1116
标题: Maximum Level Sum of a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1161. 最大层内元素和 - 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。 返回总和 最大 的那一层的层号 x。如果有多层的总和一样大，返回其中 最小 的层号 x。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/08/17/capture.jpeg] 输入：root = [1,7,0,7,-8,null,null] 输出：2 解释： 第 1 层各元素之和为 1， 第 2 层各元素之和为 7 + 0 = 7， 第 3 层各元素之和为 7 + -8 = -1， 所以我们返回第 2 层的层号，它的层内元素之和最大。 示例 2： 输入：root = [989,null,10250,98693,-89388,null,null,null,-32127] 输出：2 提示： * 树中的节点数在 [1, 104]范围内 * -105 <= Node.val <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）遍历二叉树，记录每一层的节点值之和，并找到和最大的层。

算法步骤:
1. 初始化一个队列，将根节点加入队列。
2. 初始化变量 `max_sum` 和 `max_level`，分别记录当前最大层和及其对应的层号。
3. 使用 BFS 遍历二叉树：
   - 对于每一层，计算该层所有节点值的和。
   - 更新 `max_sum` 和 `max_level`。
4. 返回 `max_level`。

关键点:
- 使用队列进行层次遍历。
- 记录每一层的节点值之和，并更新最大和及对应的层号。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只会被访问一次。
空间复杂度: O(w)，其中 w 是二叉树的最大宽度。队列中最多会存储一层的节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def max_level_sum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = [root]
    max_sum = float('-inf')
    max_level = 1
    level = 1

    while queue:
        level_sum = 0
        next_level = []
        for node in queue:
            level_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
        queue = next_level
        level += 1

    return max_level

Solution = create_solution(max_level_sum)