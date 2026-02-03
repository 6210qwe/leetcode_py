# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 112
标题: Path Sum
难度: easy
链接: https://leetcode.cn/problems/path-sum/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
112. 路径总和 - 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。 叶子节点 是指没有子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg] 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 输出：true 解释：等于目标和的根节点到叶节点路径如上图所示。 示例 2： [https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg] 输入：root = [1,2,3], targetSum = 5 输出：false 解释：树中存在两条根节点到叶子节点的路径： (1 --> 2): 和为 3 (1 --> 3): 和为 4 不存在 sum = 5 的根节点到叶子节点的路径。 示例 3： 输入：root = [], targetSum = 0 输出：false 解释：由于树是空的，所以不存在根节点到叶子节点的路径。 提示： * 树中节点的数目在范围 [0, 5000] 内 * -1000 <= Node.val <= 1000 * -1000 <= targetSum <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归检查是否存在从根到叶子的路径和等于targetSum

算法步骤:
1. 如果根节点为空，返回False
2. 如果当前节点是叶子节点，检查值是否等于targetSum
3. 递归检查左子树和右子树，targetSum减去当前节点值
4. 返回左子树或右子树的结果

关键点:
- 必须到达叶子节点才算完整路径
- 时间复杂度O(n)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(h) - 递归栈深度，h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def path_sum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    函数式接口 - 判断是否存在路径和等于targetSum
    
    实现思路:
    递归检查是否存在从根到叶子的路径和等于targetSum。
    
    Args:
        root: 二叉树的根节点
        targetSum: 目标和
        
    Returns:
        如果存在这样的路径返回True，否则返回False
        
    Example:
        >>> root = TreeNode.from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        >>> path_sum(root, 22)
        True
    """
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == targetSum
    
    return (path_sum(root.left, targetSum - root.val) or 
            path_sum(root.right, targetSum - root.val))


# 自动生成Solution类（无需手动编写）
Solution = create_solution(path_sum)
