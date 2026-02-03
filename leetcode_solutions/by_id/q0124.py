# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 124
标题: Binary Tree Maximum Path Sum
难度: hard
链接: https://leetcode.cn/problems/binary-tree-maximum-path-sum/
题目类型: 树、深度优先搜索、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
124. 二叉树中的最大路径和 - 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。 路径和 是路径中各节点值的总和。 给你一个二叉树的根节点 root ，返回其 最大路径和 。 示例 1： [https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg] 输入：root = [1,2,3] 输出：6 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6 示例 2： [https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg] 输入：root = [-10,9,20,null,null,15,7] 输出：42 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42 提示： * 树中节点数目范围是 [1, 3 * 104] * -1000 <= Node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归DFS，对于每个节点，计算经过该节点的最大路径和

算法步骤:
1. 递归计算每个节点的最大贡献值（从该节点向下的最大路径和）
2. 对于每个节点，计算经过该节点的最大路径和（左子树贡献+右子树贡献+节点值）
3. 更新全局最大值

关键点:
- 递归DFS，计算节点贡献值
- 时间复杂度O(n)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历所有节点
空间复杂度: O(h) - h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def binary_tree_maximum_path_sum(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 二叉树中的最大路径和
    
    实现思路:
    递归DFS，对于每个节点，计算经过该节点的最大路径和。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        最大路径和
        
    Example:
        >>> root = TreeNode.from_list([-10,9,20,None,None,15,7])
        >>> binary_tree_maximum_path_sum(root)
        42
    """
    max_sum = float('-inf')
    
    def max_gain(node: Optional[TreeNode]) -> int:
        """计算节点的最大贡献值"""
        nonlocal max_sum
        if not node:
            return 0
        
        # 递归计算左右子树的最大贡献值
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # 经过当前节点的最大路径和
        current_path_sum = node.val + left_gain + right_gain
        
        # 更新全局最大值
        max_sum = max(max_sum, current_path_sum)
        
        # 返回节点的最大贡献值（只能选择一条路径）
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_maximum_path_sum)
