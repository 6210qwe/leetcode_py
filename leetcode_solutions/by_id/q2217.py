# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2217
标题: Step-By-Step Directions From a Binary Tree Node to Another
难度: medium
链接: https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
题目类型: 树、深度优先搜索、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2096. 从二叉树一个节点到另一个节点每一步的方向 - 给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。每个节点的值为 1 到 n 中的一个整数，且互不相同。给你一个整数 startValue ，表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。 请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 'L' ，'R' 和 'U' 分别表示一种方向： * 'L' 表示从一个节点前往它的 左孩子 节点。 * 'R' 表示从一个节点前往它的 右孩子 节点。 * 'U' 表示从一个节点前往它的 父 节点。 请你返回从 s 到 t 最短路径 每一步的方向。 示例 1： [https://assets.leetcode.com/uploads/2021/11/15/eg1.png] 输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6 输出："UURL" 解释：最短路径为：3 → 1 → 5 → 2 → 6 。 示例 2： [https://assets.leetcode.com/uploads/2021/11/15/eg2.png] 输入：root = [2,1], startValue = 2, destValue = 1 输出："L" 解释：最短路径为：2 → 1 。 提示： * 树中节点数目为 n 。 * 2 <= n <= 105 * 1 <= Node.val <= n * 树中所有节点的值 互不相同 。 * 1 <= startValue, destValue <= n * startValue != destValue
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
