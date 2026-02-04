# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2545
标题: Height of Binary Tree After Subtree Removal Queries
难度: hard
链接: https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/
题目类型: 树、深度优先搜索、广度优先搜索、数组、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2458. 移除子树后的二叉树高度 - 给你一棵 二叉树 的根节点 root ，树中有 n 个节点。每个节点都可以被分配一个从 1 到 n 且互不相同的值。另给你一个长度为 m 的数组 queries 。 你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作： * 从树中 移除 以 queries[i] 的值作为根节点的子树。题目所用测试用例保证 queries[i] 不 等于根节点的值。 返回一个长度为 m 的数组 answer ，其中 answer[i] 是执行第 i 个查询后树的高度。 注意： * 查询之间是独立的，所以在每个查询执行后，树会回到其 初始 状态。 * 树的高度是从根到树中某个节点的 最长简单路径中的边数 。 示例 1： [https://assets.leetcode.com/uploads/2022/09/07/binaryytreeedrawio-1.png] 输入：root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4] 输出：[2] 解释：上图展示了从树中移除以 4 为根节点的子树。 树的高度是 2（路径为 1 -> 3 -> 2）。 示例 2： [https://assets.leetcode.com/uploads/2022/09/07/binaryytreeedrawio-2.png] 输入：root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8] 输出：[3,2,3,2] 解释：执行下述查询： - 移除以 3 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 4）。 - 移除以 2 为根节点的子树。树的高度变为 2（路径为 5 -> 8 -> 1）。 - 移除以 4 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 6）。 - 移除以 8 为根节点的子树。树的高度变为 2（路径为 5 -> 9 -> 3）。 提示： * 树中节点的数目是 n * 2 <= n <= 105 * 1 <= Node.val <= n * 树中的所有值 互不相同 * m == queries.length * 1 <= m <= min(n, 104) * 1 <= queries[i] <= n * queries[i] != root.val
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过两次深度优先搜索 (DFS) 来计算每个节点的高度和贡献，然后根据这些信息快速回答每个查询。

算法步骤:
1. 第一次 DFS 计算每个节点的高度。
2. 第二次 DFS 计算每个节点的贡献，即如果移除该节点，树的最大高度。
3. 对于每个查询，直接返回预先计算好的贡献值。

关键点:
- 使用两个字典分别存储每个节点的高度和贡献。
- 在第二次 DFS 中，维护一个当前最大高度，以便在移除节点时快速找到新的最大高度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是树中节点的数量，m 是查询的数量。两次 DFS 各自遍历所有节点一次，处理每个查询的时间复杂度为 O(1)。
空间复杂度: O(n)，用于存储每个节点的高度和贡献。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def tree_queries(root: Optional[TreeNode], queries: List[int]) -> List[int]:
    # 存储每个节点的高度
    heights = {}
    # 存储每个节点的贡献
    contributions = {}

    def dfs_height(node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        left_height = dfs_height(node.left)
        right_height = dfs_height(node.right)
        heights[node.val] = max(left_height, right_height) + 1
        return heights[node.val]

    def dfs_contribution(node: Optional[TreeNode], current_max: int):
        if not node:
            return
        # 当前节点的贡献
        contributions[node.val] = current_max
        # 更新当前最大高度
        new_current_max = max(current_max, heights[node.val])
        # 递归处理左子树
        dfs_contribution(node.left, max(new_current_max, heights.get(node.right.val, -1)))
        # 递归处理右子树
        dfs_contribution(node.right, max(new_current_max, heights.get(node.left.val, -1)))

    # 第一次 DFS 计算每个节点的高度
    dfs_height(root)
    # 第二次 DFS 计算每个节点的贡献
    dfs_contribution(root, -1)

    # 处理每个查询
    result = []
    for query in queries:
        result.append(contributions[query])
    return result


Solution = create_solution(tree_queries)