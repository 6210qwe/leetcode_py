# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 437
标题: Path Sum III
难度: medium
链接: https://leetcode.cn/problems/path-sum-iii/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
437. 路径总和 III - 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 示例 1： [https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg] 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8 输出：3 解释：和等于 8 的路径有 3 条，如图所示。 示例 2： 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 输出：3 提示: * 二叉树的节点个数的范围是 [0,1000] * -109 <= Node.val <= 109 * -1000 <= targetSum <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和和哈希表来记录从根节点到当前节点的所有路径和，并检查是否存在某个路径和等于当前路径和减去目标值。

算法步骤:
1. 定义一个递归函数 `dfs`，用于深度优先遍历二叉树。
2. 使用一个哈希表 `prefix_sum` 来记录从根节点到当前节点的所有路径和及其出现次数。
3. 在递归过程中，更新当前路径和，并检查是否存在某个路径和等于当前路径和减去目标值。
4. 递归结束后，回溯时更新哈希表。

关键点:
- 使用前缀和和哈希表来优化时间和空间复杂度。
- 注意边界条件，如空树的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每个节点访问一次
空间复杂度: O(n) - 哈希表存储路径和
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def path_sum_iii(root: Optional[TreeNode], target_sum: int) -> int:
    """
    函数式接口 - 计算二叉树中路径和等于 targetSum 的路径数目
    
    实现思路:
    使用前缀和和哈希表来记录从根节点到当前节点的所有路径和，并检查是否存在某个路径和等于当前路径和减去目标值。
    
    Args:
        root (Optional[TreeNode]): 二叉树的根节点
        target_sum (int): 目标路径和
        
    Returns:
        int: 路径和等于 targetSum 的路径数目
        
    Example:
        >>> path_sum_iii(TreeNode.from_list([10,5,-3,3,2,None,11,3,-2,None,1]), 8)
        3
    """
    def dfs(node: Optional[TreeNode], current_sum: int, prefix_sum: dict, target: int) -> int:
        if not node:
            return 0
        
        current_sum += node.val
        count = prefix_sum.get(current_sum - target, 0)
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        left_count = dfs(node.left, current_sum, prefix_sum, target)
        right_count = dfs(node.right, current_sum, prefix_sum, target)
        
        prefix_sum[current_sum] -= 1
        if prefix_sum[current_sum] == 0:
            del prefix_sum[current_sum]
        
        return count + left_count + right_count
    
    prefix_sum = {0: 1}
    return dfs(root, 0, prefix_sum, target_sum)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(path_sum_iii)