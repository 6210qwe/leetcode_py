# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2347
标题: Count Nodes Equal to Average of Subtree
难度: medium
链接: https://leetcode.cn/problems/count-nodes-equal-to-average-of-subtree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2265. 统计值等于子树平均值的节点数 - 给你一棵二叉树的根节点 root ，找出并返回满足要求的节点数，要求节点的值等于其 子树 中值的 平均值 。 注意： * n 个元素的平均值可以由 n 个元素 求和 然后再除以 n ，并 向下舍入 到最近的整数。 * root 的 子树 由 root 和它的所有后代组成。 示例 1： [https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png] 输入：root = [4,8,5,0,1,null,6] 输出：5 解释： 对值为 4 的节点：子树的平均值 (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4 。 对值为 5 的节点：子树的平均值 (5 + 6) / 2 = 11 / 2 = 5 。 对值为 0 的节点：子树的平均值 0 / 1 = 0 。 对值为 1 的节点：子树的平均值 1 / 1 = 1 。 对值为 6 的节点：子树的平均值 6 / 1 = 6 。 示例 2： [https://assets.leetcode.com/uploads/2022/03/26/image-20220326133920-1.png] 输入：root = [1] 输出：1 解释：对值为 1 的节点：子树的平均值 1 / 1 = 1。 提示： * 树中节点数目在范围 [1, 1000] 内 * 0 <= Node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历每个节点，并计算其子树的总和和节点数。然后检查当前节点的值是否等于其子树的平均值。

算法步骤:
1. 定义一个辅助函数 `dfs`，该函数返回一个元组 (sum, count, result)，其中 sum 是子树的总和，count 是子树的节点数，result 是满足条件的节点数。
2. 在 `dfs` 函数中，递归地处理左子树和右子树，获取它们的总和和节点数。
3. 计算当前节点的子树总和和节点数。
4. 检查当前节点的值是否等于其子树的平均值，如果是，则增加结果计数。
5. 返回当前节点的子树总和、节点数和结果计数。

关键点:
- 使用 DFS 遍历树，并在遍历过程中计算每个节点的子树总和和节点数。
- 检查当前节点的值是否等于其子树的平均值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。这是由于递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_nodes_equal_to_average_of_subtree(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 统计值等于子树平均值的节点数
    """
    def dfs(node: Optional[TreeNode]) -> (int, int, int):
        if not node:
            return 0, 0, 0
        
        left_sum, left_count, left_result = dfs(node.left)
        right_sum, right_count, right_result = dfs(node.right)
        
        current_sum = left_sum + right_sum + node.val
        current_count = left_count + right_count + 1
        current_result = left_result + right_result
        
        if node.val == current_sum // current_count:
            current_result += 1
        
        return current_sum, current_count, current_result
    
    _, _, result = dfs(root)
    return result


Solution = create_solution(count_nodes_equal_to_average_of_subtree)