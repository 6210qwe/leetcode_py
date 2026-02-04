# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000298
标题: 找树左下角的值
难度: medium
链接: https://leetcode.cn/problems/LwUNpT/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 045. 找树左下角的值 - 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 假设二叉树中至少有一个节点。 示例 1： [https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg] 输入: root = [2,1,3] 输出: 1 示例 2： [https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg] 输入: [1,2,3,4,null,5,6,null,null,7] 输出: 7 提示： * 二叉树的节点个数的范围是 [1,104] * -231 <= Node.val <= 231 - 1 注意：本题与主站 513 题相同： https://leetcode.cn/problems/find-bottom-left-tree-value/ [https://leetcode.cn/problems/find-bottom-left-tree-value/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历二叉树，记录最深层的节点值。

算法步骤:
1. 初始化两个变量 `max_depth` 和 `leftmost_value`，分别记录当前最大深度和最左边的节点值。
2. 定义一个递归函数 `dfs(node, depth)`，用于遍历二叉树。
3. 在递归函数中，如果当前节点是叶子节点且深度大于 `max_depth`，更新 `max_depth` 和 `leftmost_value`。
4. 递归调用左子节点和右子节点，深度加一。
5. 返回 `leftmost_value`。

关键点:
- 使用深度优先搜索确保我们总是先访问左子树，从而找到最左边的节点。
- 通过记录最大深度来确保我们找到的是最底层的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数，因为每个节点都被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度，这是由于递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_bottom_left_value(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 找到二叉树最底层最左边节点的值
    """
    max_depth = 0
    leftmost_value = 0

    def dfs(node: Optional[TreeNode], depth: int):
        nonlocal max_depth, leftmost_value
        if not node:
            return
        if not node.left and not node.right:
            if depth > max_depth:
                max_depth = depth
                leftmost_value = node.val
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return leftmost_value

Solution = create_solution(find_bottom_left_value)