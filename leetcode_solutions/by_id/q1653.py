# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1653
标题: Number of Good Leaf Nodes Pairs
难度: medium
链接: https://leetcode.cn/problems/number-of-good-leaf-nodes-pairs/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1530. 好叶子节点对的数量 - 给你二叉树的根节点 root 和一个整数 distance 。 如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。 返回树中 好叶子节点对的数量 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/26/e1.jpg] 输入：root = [1,2,3,null,4], distance = 3 输出：1 解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/26/e2.jpg] 输入：root = [1,2,3,4,5,6,7], distance = 3 输出：2 解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。 示例 3： 输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3 输出：1 解释：唯一的好叶子节点对是 [2,5] 。 示例 4： 输入：root = [100], distance = 1 输出：0 示例 5： 输入：root = [1,1,1], distance = 2 输出：1 提示： * tree 的节点数在 [1, 2^10] 范围内。 * 每个节点的值都在 [1, 100] 之间。 * 1 <= distance <= 10
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历树，并记录每个节点到其所有叶子节点的距离。然后在每个非叶子节点处，检查左子树和右子树中的叶子节点对是否满足条件。

算法步骤:
1. 定义一个递归函数 `dfs`，它返回从当前节点到其所有叶子节点的距离列表。
2. 在 `dfs` 函数中，如果当前节点是叶子节点，则返回 `[1]`（表示距离为 1）。
3. 否则，递归调用 `dfs` 函数处理左子树和右子树，并获取它们的叶子节点距离列表。
4. 对于每个左子树中的叶子节点距离 `l_dist` 和右子树中的叶子节点距离 `r_dist`，如果 `l_dist + r_dist <= distance`，则计数器加一。
5. 返回当前节点到其所有叶子节点的距离列表（将左子树和右子树的距离列表中的每个距离加 1）。
6. 在主函数中调用 `dfs` 函数并返回计数器的值。

关键点:
- 使用递归 DFS 遍历树，并记录每个节点到其所有叶子节点的距离。
- 在每个非叶子节点处，检查左子树和右子树中的叶子节点对是否满足条件。
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

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_good_leaf_pairs(root: Optional[TreeNode], distance: int) -> int:
    def dfs(node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        
        if not node.left and not node.right:
            return [1]
        
        left_distances = dfs(node.left)
        right_distances = dfs(node.right)
        
        for l_dist in left_distances:
            for r_dist in right_distances:
                if l_dist + r_dist <= distance:
                    nonlocal count
                    count += 1
        
        return [dist + 1 for dist in left_distances + right_distances]
    
    count = 0
    dfs(root)
    return count


Solution = create_solution(count_good_leaf_pairs)