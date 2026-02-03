# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 337
标题: House Robber III
难度: medium
链接: https://leetcode.cn/problems/house-robber-iii/
题目类型: 树、深度优先搜索、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
337. 打家劫舍 III - 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。 示例 1: [https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg] 输入: root = [3,2,3,null,3,null,1] 输出: 7 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7 示例 2: [https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg] 输入: root = [3,4,5,1,3,null,1] 输出: 9 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9 提示： * 树的节点数在 [1, 104] 范围内 * 0 <= Node.val <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 树形DP，每个节点返回(抢,不抢)的最大值

算法步骤:
1. DFS遍历树
2. 对于每个节点，返回(抢当前节点,不抢当前节点)的最大值
3. 抢当前节点：不能抢子节点
4. 不抢当前节点：可以抢子节点

关键点:
- 树形DP
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有节点
空间复杂度: O(h) - 递归栈空间，h为树高
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def rob(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 打家劫舍 III
    
    实现思路:
    树形DP：每个节点返回(抢,不抢)的最大值。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        最大金额
        
    Example:
        >>> root = TreeNode(3)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> rob(root)
        7
    """
    def dfs(node: Optional[TreeNode]) -> tuple:
        """返回(抢当前节点,不抢当前节点)的最大值"""
        if not node:
            return (0, 0)
        
        left_rob, left_not_rob = dfs(node.left)
        right_rob, right_not_rob = dfs(node.right)
        
        # 抢当前节点
        rob_current = node.val + left_not_rob + right_not_rob
        
        # 不抢当前节点
        not_rob_current = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return (rob_current, not_rob_current)
    
    rob_root, not_rob_root = dfs(root)
    return max(rob_root, not_rob_root)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(rob)
