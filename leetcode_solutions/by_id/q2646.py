# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2646
标题: Kth Largest Sum in a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/
题目类型: 树、广度优先搜索、二叉树、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2583. 二叉树中的第 K 大层和 - 给你一棵二叉树的根节点 root 和一个正整数 k 。 树中的 层和 是指 同一层 上节点值的总和。 返回树中第 k 大的层和（不一定不同）。如果树少于 k 层，则返回 -1 。 注意，如果两个节点与根节点的距离相同，则认为它们在同一层。 示例 1： [https://assets.leetcode.com/uploads/2022/12/14/binaryytreeedrawio-2.png] 输入：root = [5,8,9,2,1,3,7,4,6], k = 2 输出：13 解释：树中每一层的层和分别是： - Level 1: 5 - Level 2: 8 + 9 = 17 - Level 3: 2 + 1 + 3 + 7 = 13 - Level 4: 4 + 6 = 10 第 2 大的层和等于 13 。 示例 2： [https://assets.leetcode.com/uploads/2022/12/14/treedrawio-3.png] 输入：root = [1,2,null,3], k = 1 输出：3 解释：最大的层和是 3 。 提示： * 树中的节点数为 n * 2 <= n <= 105 * 1 <= Node.val <= 106 * 1 <= k <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来遍历二叉树，并记录每一层的节点值之和。然后对这些层和进行排序，找到第 k 大的层和。

算法步骤:
1. 使用 BFS 遍历二叉树，记录每一层的节点值之和。
2. 将所有层和存储在一个列表中。
3. 对层和列表进行降序排序。
4. 如果树的层数小于 k，返回 -1；否则返回第 k 大的层和。

关键点:
- 使用队列进行 BFS 遍历。
- 记录每一层的节点值之和。
- 对层和列表进行排序以找到第 k 大的层和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是树中的节点数。BFS 的时间复杂度是 O(n)，排序的时间复杂度是 O(n log n)。
空间复杂度: O(n)，用于存储每一层的节点值之和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def kth_largest_level_sum(root: Optional[TreeNode], k: int) -> int:
    if not root:
        return -1

    from collections import deque
    queue = deque([root])
    level_sums = []

    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level_sums.append(level_sum)

    if len(level_sums) < k:
        return -1

    level_sums.sort(reverse=True)
    return level_sums[k - 1]


Solution = create_solution(kth_largest_level_sum)