# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 515
标题: Find Largest Value in Each Tree Row
难度: medium
链接: https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
515. 在每个树行中找最大值 - 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 示例1： [https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg] 输入: root = [1,3,2,5,3,null,9] 输出: [1,3,9] 示例2： 输入: root = [1,2,3] 输出: [1,3] 提示： * 二叉树的节点个数的范围是 [0,104] * -231 <= Node.val <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）遍历二叉树，逐层记录每层的最大值。

算法步骤:
1. 初始化一个队列，将根节点加入队列。
2. 使用一个循环处理队列中的节点，直到队列为空。
3. 对于每一层，初始化一个变量来记录当前层的最大值。
4. 遍历当前层的所有节点，更新当前层的最大值，并将子节点加入队列。
5. 将当前层的最大值加入结果列表。
6. 返回结果列表。

关键点:
- 使用队列进行层次遍历。
- 每一层单独处理，记录每层的最大值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数，因为每个节点都被访问一次。
空间复杂度: O(w)，其中 w 是二叉树的最大宽度，因为队列中最多会存储一层的节点数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_largest_value_in_each_tree_row(root: Optional[TreeNode]) -> List[int]:
    """
    函数式接口 - 找出二叉树中每一层的最大值
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_max = float('-inf')
        next_level = []

        for node in queue:
            level_max = max(level_max, node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(level_max)
        queue = next_level

    return result

Solution = create_solution(find_largest_value_in_each_tree_row)