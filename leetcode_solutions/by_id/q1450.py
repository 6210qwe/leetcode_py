# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1450
标题: Delete Leaves With a Given Value
难度: medium
链接: https://leetcode.cn/problems/delete-leaves-with-a-given-value/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1325. 删除给定值的叶子节点 - 给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。 注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。 也就是说，你需要重复此过程直到不能继续删除。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_1_1684.png] 输入：root = [1,2,3,2,null,2,4], target = 2 输出：[1,null,3,null,4] 解释： 上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。 有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_2_1684.png] 输入：root = [1,3,3,3,2], target = 3 输出：[1,3,null,null,2] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_3_1684.png] 输入：root = [1,2,null,2,null,2], target = 2 输出：[1] 解释：每一步都删除一个绿色的叶子节点（值为 2）。 提示： * 树中节点数量的范围是 [1, 3000]。 * 1 <= Node.val, target <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
