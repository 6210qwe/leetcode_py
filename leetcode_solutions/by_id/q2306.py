# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2306
标题: Create Binary Tree From Descriptions
难度: medium
链接: https://leetcode.cn/problems/create-binary-tree-from-descriptions/
题目类型: 树、数组、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2196. 根据描述创建二叉树 - 给你一个二维整数数组 descriptions ，其中 descriptions[i] = [parenti, childi, isLefti] 表示 parenti 是 childi 在 二叉树 中的 父节点，二叉树中各节点的值 互不相同 。此外： * 如果 isLefti == 1 ，那么 childi 就是 parenti 的左子节点。 * 如果 isLefti == 0 ，那么 childi 就是 parenti 的右子节点。 请你根据 descriptions 的描述来构造二叉树并返回其 根节点 。 测试用例会保证可以构造出 有效 的二叉树。 示例 1： [https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png] 输入：descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]] 输出：[50,20,80,15,17,19] 解释：根节点是值为 50 的节点，因为它没有父节点。 结果二叉树如上图所示。 示例 2： [https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png] 输入：descriptions = [[1,2,1],[2,3,0],[3,4,1]] 输出：[1,2,null,null,3,4] 解释：根节点是值为 1 的节点，因为它没有父节点。 结果二叉树如上图所示。 提示： * 1 <= descriptions.length <= 104 * descriptions[i].length == 3 * 1 <= parenti, childi <= 105 * 0 <= isLefti <= 1 * descriptions 所描述的二叉树是一棵有效二叉树
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
