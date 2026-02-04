# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100317
标题: 二叉树中和为目标值的路径
难度: medium
链接: https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
题目类型: 树、深度优先搜索、回溯、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 153. 二叉树中和为目标值的路径 - 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。 叶子节点 是指没有子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg] 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 输出：[[5,4,11,2],[5,8,4,5]] 示例 2： [https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg] 输入：root = [1,2,3], targetSum = 5 输出：[] 示例 3： 输入：root = [1,2], targetSum = 0 输出：[] 提示： * 树中节点总数在范围 [0, 5000] 内 * -1000 <= Node.val <= 1000 * -1000 <= targetSum <= 1000 注意：本题与主站 113 题相同：https://leetcode.cn/problems/path-sum-ii/ [https://leetcode.cn/problems/path-sum-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历二叉树，同时维护当前路径和当前路径和。当到达叶子节点且路径和等于目标值时，将路径加入结果。

算法步骤:
1. 定义一个递归函数 `dfs`，参数包括当前节点、当前路径、当前路径和。
2. 在递归函数中，如果当前节点为空，直接返回。
3. 将当前节点值加入路径，并更新路径和。
4. 如果当前节点是叶子节点且路径和等于目标值，将路径加入结果。
5. 递归调用左子节点和右子节点。
6. 回溯，移除当前节点值并恢复路径和。

关键点:
- 使用回溯法确保路径的正确性。
- 递归过程中维护当前路径和当前路径和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点都被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度。最坏情况下，二叉树退化为链表，空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_paths(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    找出所有从根节点到叶子节点路径总和等于给定目标和的路径。
    """
    def dfs(node: Optional[TreeNode], path: List[int], current_sum: int):
        if not node:
            return
        path.append(node.val)
        current_sum += node.val
        if not node.left and not node.right and current_sum == target_sum:
            result.append(path[:])
        dfs(node.left, path, current_sum)
        dfs(node.right, path, current_sum)
        path.pop()
    
    result: List[List[int]] = []
    dfs(root, [], 0)
    return result

Solution = create_solution(find_paths)