# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1157
标题: Insufficient Nodes in Root to Leaf Paths
难度: medium
链接: https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1080. 根到叶路径上的不足节点 - 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。 叶子节点，就是没有子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2019/06/05/insufficient-11.png] 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1 输出：[1,2,3,4,null,null,7,8,9,null,14] 示例 2： [https://assets.leetcode.com/uploads/2019/06/05/insufficient-3.png] 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22 输出：[5,4,8,11,null,17,4,7,null,null,null,5] 示例 3： [https://assets.leetcode.com/uploads/2019/06/11/screen-shot-2019-06-11-at-83301-pm.png] 输入：root = [1,2,-3,-5,null,4,null], limit = -1 输出：[1,null,-3,4] 提示： * 树中节点数目在范围 [1, 5000] 内 * -105 <= Node.val <= 105 * -109 <= limit <= 109
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
