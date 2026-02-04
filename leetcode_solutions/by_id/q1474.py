# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1474
标题: Longest ZigZag Path in a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/
题目类型: 树、深度优先搜索、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1372. 二叉树中的最长交错路径 - 给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下： * 选择二叉树中 任意 节点和一个方向（左或者右）。 * 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。 * 改变前进方向：左变右或者右变左。 * 重复第二步和第三步，直到你在树中无法继续移动。 交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。 请你返回给定树中最长 交错路径 的长度。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_1_1702.png] 输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1] 输出：3 解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_2_1702.png] 输入：root = [1,1,1,null,1,null,null,1,1,null,1] 输出：4 解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。 示例 3： 输入：root = [1] 输出：0 提示： * 每棵树最多有 50000 个节点。 * 每个节点的值在 [1, 100] 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，并记录每个节点的最长交错路径。

算法步骤:
1. 定义一个递归函数 `dfs`，它接受三个参数：当前节点、当前方向（左或右）和当前路径长度。
2. 在 `dfs` 函数中，更新全局最大路径长度。
3. 递归调用 `dfs` 函数，分别处理左子节点和右子节点，改变方向并增加路径长度。
4. 初始化全局最大路径长度为 0，并从根节点开始调用 `dfs` 函数。

关键点:
- 使用递归进行深度优先搜索。
- 通过传递方向和路径长度来跟踪当前路径。
- 更新全局最大路径长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def dfs(node: Optional[TreeNode], direction: str, length: int) -> None:
            if not node:
                return
            self.max_length = max(self.max_length, length)
            if direction == 'left':
                dfs(node.left, 'right', length + 1)
                dfs(node.right, 'left', 1)
            else:
                dfs(node.right, 'left', length + 1)
                dfs(node.left, 'right', 1)
        
        if root:
            dfs(root.left, 'right', 1)
            dfs(root.right, 'left', 1)
        
        return self.max_length

Solution = create_solution(Solution)