# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 513
标题: Find Bottom Left Tree Value
难度: medium
链接: https://leetcode.cn/problems/find-bottom-left-tree-value/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
513. 找树左下角的值 - 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 假设二叉树中至少有一个节点。 示例 1: [https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg] 输入: root = [2,1,3] 输出: 1 示例 2: [https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg] 输入: [1,2,3,4,null,5,6,null,null,7] 输出: 7 提示: * 二叉树的节点个数的范围是 [1,104] * -231 <= Node.val <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用层次遍历（广度优先搜索）来找到最底层最左边的节点。

算法步骤:
1. 初始化一个队列，将根节点加入队列。
2. 进行层次遍历，每次处理一层的所有节点。
3. 在每一层开始时，记录当前层的第一个节点的值。
4. 当遍历完所有层后，最后一个记录的节点值即为最底层最左边的节点值。

关键点:
- 使用队列进行层次遍历。
- 每次处理一层时，记录第一个节点的值。
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


def find_bottom_left_value(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 找到二叉树最底层最左边的节点值
    """
    if not root:
        return None

    queue = [root]
    leftmost_value = None

    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.pop(0)
            if i == 0:
                leftmost_value = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return leftmost_value


Solution = create_solution(find_bottom_left_value)