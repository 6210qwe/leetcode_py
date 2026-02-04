# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 896
标题: Smallest Subtree with all the Deepest Nodes
难度: medium
链接: https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
865. 具有所有最深节点的最小子树 - 给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。 返回包含原始树中所有 最深节点 的 最小子树 。 如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。 一个节点的 子树 是该节点加上它的所有后代的集合。 示例 1： [https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png] 输入：root = [3,5,1,6,2,0,8,null,null,7,4] 输出：[2,7,4] 解释： 我们返回值为 2 的节点，在图中用黄色标记。 在图中用蓝色标记的是树的最深的节点。 注意，节点 5、3 和 2 包含树中最深的节点，但节点 2 的子树最小，因此我们返回它。 示例 2： 输入：root = [1] 输出：[1] 解释：根节点是树中最深的节点。 示例 3： 输入：root = [0,1,3,null,2] 输出：[2] 解释：树中最深的节点为 2 ，有效子树为节点 2、1 和 0 的子树，但节点 2 的子树最小。 提示： * 树中节点的数量在 [1, 500] 范围内。 * 0 <= Node.val <= 500 * 每个节点的值都是 独一无二 的。 注意：本题与力扣 1123 重复：https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves [https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来找到所有最深节点，并记录它们的最近公共祖先 (LCA)。

算法步骤:
1. 定义一个辅助函数 `dfs`，用于计算每个节点的深度，并记录最深节点。
2. 在 `dfs` 中，递归地计算左子树和右子树的深度。
3. 如果左右子树的深度相同，则当前节点就是最深节点的 LCA。
4. 如果左右子树的深度不同，则返回深度较大的子树的结果。
5. 最终返回最深节点的 LCA。

关键点:
- 使用 DFS 计算每个节点的深度。
- 通过比较左右子树的深度来确定 LCA。
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

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def subtree_with_all_deepest(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    返回包含所有最深节点的最小子树。
    """
    def dfs(node):
        if not node:
            return None, 0
        left_node, left_depth = dfs(node.left)
        right_node, right_depth = dfs(node.right)
        if left_depth == right_depth:
            return node, left_depth + 1
        elif left_depth > right_depth:
            return left_node, left_depth + 1
        else:
            return right_node, right_depth + 1

    return dfs(root)[0]


Solution = create_solution(subtree_with_all_deepest)