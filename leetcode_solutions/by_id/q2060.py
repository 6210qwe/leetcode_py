# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2060
标题: Merge BSTs to Create Single BST
难度: hard
链接: https://leetcode.cn/problems/merge-bsts-to-create-single-bst/
题目类型: 树、深度优先搜索、哈希表、二分查找、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1932. 合并多棵二叉搜索树 - 给你 n 个 二叉搜索树的根节点 ，存储在数组 trees 中（下标从 0 开始），对应 n 棵不同的二叉搜索树。trees 中的每棵二叉搜索树 最多有 3 个节点 ，且不存在值相同的两个根节点。在一步操作中，将会完成下述步骤： * 选择两个 不同的 下标 i 和 j ，要求满足在 trees[i] 中的某个 叶节点 的值等于 trees[j] 的 根节点的值 。 * 用 trees[j] 替换 trees[i] 中的那个叶节点。 * 从 trees 中移除 trees[j] 。 如果在执行 n - 1 次操作后，能形成一棵有效的二叉搜索树，则返回结果二叉搜索树的 根节点 ；如果无法构造一棵有效的二叉搜索树，返回 null 。 二叉搜索树是一种二叉树，且树中每个节点均满足下述属性： * 任意节点的左子树中的值都 严格小于 此节点的值。 * 任意节点的右子树中的值都 严格大于 此节点的值。 叶节点是不含子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2021/06/08/d1.png] 输入：trees = [[2,1],[3,2,5],[5,4]] 输出：[3,2,5,1,null,4] 解释： 第一步操作中，选出 i=1 和 j=0 ，并将 trees[0] 合并到 trees[1] 中。 删除 trees[0] ，trees = [[3,2,5,1],[5,4]] 。 [https://assets.leetcode.com/uploads/2021/06/24/diagram.png] 在第二步操作中，选出 i=0 和 j=1 ，将 trees[1] 合并到 trees[0] 中。 删除 trees[1] ，trees = [[3,2,5,1,null,4]] 。 [https://assets.leetcode.com/uploads/2021/06/24/diagram-2.png] 结果树如上图所示，为一棵有效的二叉搜索树，所以返回该树的根节点。 示例 2： [https://assets.leetcode.com/uploads/2021/06/08/d2.png] 输入：trees = [[5,3,8],[3,2,6]] 输出：[] 解释： 选出 i=0 和 j=1 ，然后将 trees[1] 合并到 trees[0] 中。 删除 trees[1] ，trees = [[5,3,8,2,6]] 。 [https://assets.leetcode.com/uploads/2021/06/24/diagram-3.png] 结果树如上图所示。仅能执行一次有效的操作，但结果树不是一棵有效的二叉搜索树，所以返回 null 。 示例 3： [https://assets.leetcode.com/uploads/2021/06/08/d3.png] 输入：trees = [[5,4],[3]] 输出：[] 解释：无法执行任何操作。 提示： * n == trees.length * 1 <= n <= 5 * 104 * 每棵树中节点数目在范围 [1, 3] 内。 * 输入数据的每个节点可能有子节点但不存在子节点的子节点 * trees 中不存在两棵树根节点值相同的情况。 * 输入中的所有树都是 有效的二叉树搜索树 。 * 1 <= TreeNode.val <= 5 * 104.
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 使用一个字典来记录每个节点值对应的节点。
2. 构建一个初始的根节点集合，并尝试合并这些根节点。
3. 使用深度优先搜索 (DFS) 来验证最终的树是否是一棵有效的二叉搜索树。

算法步骤:
1. 初始化一个字典 `node_map` 来记录每个节点值对应的节点。
2. 将所有根节点加入 `root_set`。
3. 遍历所有树，将每个节点加入 `node_map`，并检查是否有可以合并的节点。
4. 如果可以合并，更新 `root_set` 并继续合并。
5. 最后，使用 DFS 验证最终的树是否是一棵有效的二叉搜索树。

关键点:
- 使用字典来快速查找和合并节点。
- 使用集合来管理当前的根节点。
- 使用 DFS 来验证最终的树是否有效。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_merge(trees: List[TreeNode]) -> Optional[TreeNode]:
    node_map = {}
    root_set = set()

    # 将所有节点加入 node_map，并初始化 root_set
    for tree in trees:
        if tree.left:
            node_map[tree.left.val] = tree.left
        if tree.right:
            node_map[tree.right.val] = tree.right
        root_set.add(tree)

    # 尝试合并节点
    for tree in trees:
        if tree.left and tree.left.val in node_map:
            tree.left = node_map[tree.left.val]
            root_set.remove(node_map[tree.left.val])
        if tree.right and tree.right.val in node_map:
            tree.right = node_map[tree.right.val]
            root_set.remove(node_map[tree.right.val])

    # 最终应该只有一个根节点
    if len(root_set) != 1:
        return None

    root = root_set.pop()

    # 验证最终的树是否是一棵有效的二叉搜索树
    def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (is_valid_bst(node.left, min_val, node.val) and
                is_valid_bst(node.right, node.val, max_val))

    if not is_valid_bst(root):
        return None

    return root


Solution = create_solution(can_merge)