# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3509
标题: K-th Largest Perfect Subtree Size in Binary Tree
难度: medium
链接: https://leetcode.cn/problems/k-th-largest-perfect-subtree-size-in-binary-tree/
题目类型: 树、深度优先搜索、二叉树、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3319. 第 K 大的完美二叉子树的大小 - 给你一棵 二叉树 的根节点 root 和一个整数k。 返回第 k 大的 完美二叉子树 的大小，如果不存在则返回 -1。 完美二叉树 是指所有叶子节点都在同一层级的树，且每个父节点恰有两个子节点。 示例 1： 输入： root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2 输出： 3 解释： [https://assets.leetcode.com/uploads/2024/10/14/tmpresl95rp-1.png] 完美二叉子树的根节点在图中以黑色突出显示。它们的大小按非递增顺序排列为 [3, 3, 1, 1, 1, 1, 1, 1]。 第 2 大的完美二叉子树的大小是 3。 示例 2： 输入： root = [1,2,3,4,5,6,7], k = 1 输出： 7 解释： [https://assets.leetcode.com/uploads/2024/10/14/tmp_s508x9e-1.png] 完美二叉子树的大小按非递增顺序排列为 [7, 3, 3, 1, 1, 1, 1]。最大的完美二叉子树的大小是 7。 示例 3： 输入： root = [1,2,3,null,4], k = 3 输出： -1 解释： [https://assets.leetcode.com/uploads/2024/10/14/tmp74xnmpj4-1.png] 完美二叉子树的大小按非递增顺序排列为 [1, 1]。完美二叉子树的数量少于 3。 提示： * 树中的节点数目在 [1, 2000] 范围内。 * 1 <= Node.val <= 2000 * 1 <= k <= 1024
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历二叉树，找到所有的完美二叉子树，并记录它们的大小。然后对这些大小进行排序，找到第 k 大的完美二叉子树的大小。

算法步骤:
1. 定义一个辅助函数 `is_perfect` 来判断一个子树是否是完美二叉树。
2. 定义一个主函数 `find_perfect_subtrees` 来遍历二叉树，找到所有的完美二叉子树，并记录它们的大小。
3. 对记录的完美二叉子树大小进行降序排序，找到第 k 大的完美二叉子树的大小。

关键点:
- 使用 DFS 遍历二叉树。
- 判断一个子树是否是完美二叉树。
- 记录并排序完美二叉子树的大小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log n)，其中 n 是二叉树的节点数。DFS 遍历的时间复杂度是 O(n)，排序的时间复杂度是 O(m * log m)，其中 m 是完美二叉子树的数量。
空间复杂度: O(n)，存储完美二叉子树的大小和递归调用栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_perfect(node: TreeNode) -> bool:
    """判断一个子树是否是完美二叉树"""
    if not node:
        return True
    if not node.left and not node.right:
        return True
    if not node.left or not node.right:
        return False
    return is_perfect(node.left) and is_perfect(node.right)


def find_perfect_subtrees(root: TreeNode, sizes: List[int]) -> None:
    """遍历二叉树，找到所有的完美二叉子树，并记录它们的大小"""
    if not root:
        return
    if is_perfect(root):
        size = 1
        while root.left:
            root = root.left
            size = size * 2 + 1
        sizes.append(size)
    find_perfect_subtrees(root.left, sizes)
    find_perfect_subtrees(root.right, sizes)


def solution_function_name(root: Optional[TreeNode], k: int) -> int:
    """
    函数式接口 - 找到第 k 大的完美二叉子树的大小
    """
    sizes = []
    find_perfect_subtrees(root, sizes)
    sizes.sort(reverse=True)
    if len(sizes) < k:
        return -1
    return sizes[k - 1]


Solution = create_solution(solution_function_name)