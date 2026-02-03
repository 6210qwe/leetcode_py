# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 671
标题: Second Minimum Node In a Binary Tree
难度: easy
链接: https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
671. 二叉树中第二小的节点 - 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。 更正式地说，即 root.val = min(root.left.val, root.right.val) 总成立。 给出这样的一个二叉树，你需要输出所有节点中的 第二小的值 。 如果第二小的值不存在的话，输出 -1 。 示例 1： [https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg] 输入：root = [2,2,5,null,null,5,7] 输出：5 解释：最小的值是 2 ，第二小的值是 5 。 示例 2： [https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg] 输入：root = [2,2,2] 输出：-1 解释：最小的值是 2, 但是不存在第二小的值。 提示： * 树中节点数目在范围 [1, 25] 内 * 1 <= Node.val <= 231 - 1 * 对于树中每个节点 root.val == min(root.left.val, root.right.val)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: DFS 找到严格大于根节点值的最小值

算法步骤:
1. 记录根节点值 root_val，它是整棵树中的最小值
2. 使用 DFS 遍历整棵树：
   - 若当前节点值 > root_val，则用它来更新候选答案 ans = min(ans, node.val)
   - 若当前节点值 == root_val，则继续递归遍历其左右子树
3. 遍历结束后，如果 ans 仍为无穷大，说明不存在第二小的值，返回 -1
4. 否则返回 ans

关键点:
- 根据题目性质，只有值等于 root_val 的节点才可能在其子树中出现更大的值
- 只关心严格大于 root_val 的最小值
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n 为节点数，需要遍历整棵树
空间复杂度: O(h) - 递归栈空间，h 为树的高度，最坏 O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_second_minimum_value(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 二叉树中第二小的节点

    实现思路:
    DFS 遍历，找到严格大于根节点值的最小值。
    """
    if root is None:
        return -1

    root_val = root.val
    ans = float("inf")

    def dfs(node: Optional[TreeNode]) -> None:
        nonlocal ans
        if not node:
            return
        if root_val < node.val < ans:
            ans = node.val
        elif node.val == root_val:
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return -1 if ans == float("inf") else int(ans)


Solution = create_solution(find_second_minimum_value)
