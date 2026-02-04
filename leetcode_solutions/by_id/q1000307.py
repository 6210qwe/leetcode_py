# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000307
标题: 路径总和 III
难度: medium
链接: https://leetcode.cn/problems/6eUYwP/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 050. 路径总和 III - 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 示例 1： [https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg] 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8 输出：3 解释：和等于 8 的路径有 3 条，如图所示。 示例 2： 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 输出：3 提示: * 二叉树的节点个数的范围是 [0,1000] * -109 <= Node.val <= 109 * -1000 <= targetSum <= 1000 注意：本题与主站 437 题相同：https://leetcode.cn/problems/path-sum-iii/ [https://leetcode.cn/problems/path-sum-iii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和和哈希表来记录路径和的出现次数，从而快速查找满足条件的路径。

算法步骤:
1. 定义一个递归函数 `dfs`，用于深度优先遍历二叉树。
2. 使用一个哈希表 `prefix_sum` 记录从根节点到当前节点的路径和及其出现次数。
3. 在遍历过程中，计算当前路径和 `current_sum`，并检查 `current_sum - targetSum` 是否在 `prefix_sum` 中，如果存在则说明存在满足条件的路径。
4. 更新 `prefix_sum` 并继续递归遍历左右子树。
5. 递归结束后，回溯时更新 `prefix_sum`。

关键点:
- 使用前缀和和哈希表可以将时间复杂度优化到 O(n)。
- 递归过程中维护路径和的哈希表，确保路径和的正确性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只会被访问一次。
空间复杂度: O(n)，哈希表和递归栈的空间消耗。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def path_sum_iii(root: Optional[TreeNode], target_sum: int) -> int:
    """
    函数式接口 - 求二叉树中路径和等于 targetSum 的路径数目
    """
    def dfs(node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0
        
        current_sum += node.val
        count = prefix_sum.get(current_sum - target_sum, 0)
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        count += dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        prefix_sum[current_sum] -= 1
        if prefix_sum[current_sum] == 0:
            del prefix_sum[current_sum]
        
        return count
    
    prefix_sum = {0: 1}
    return dfs(root, 0)


Solution = create_solution(path_sum_iii)