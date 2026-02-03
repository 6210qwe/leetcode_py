# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1840
标题: Minimize Hamming Distance After Swap Operations
难度: medium
链接: https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/
题目类型: 深度优先搜索、并查集、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1722. 执行交换操作后的最小汉明距离 - 给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，其中每个 allowedSwaps[i] = [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。注意，你可以按 任意 顺序 多次 交换一对特定下标指向的元素。 相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。形式上，其值等于满足 source[i] != target[i] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。 在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。 示例 1： 输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]] 输出：1 解释：source 可以按下述方式转换： - 交换下标 0 和 1 指向的元素：source = [2,1,3,4] - 交换下标 2 和 3 指向的元素：source = [2,1,4,3] source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。 示例 2： 输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = [] 输出：2 解释：不能对 source 执行交换操作。 source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。 示例 3： 输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]] 输出：0 提示： * n == source.length == target.length * 1 <= n <= 105 * 1 <= source[i], target[i] <= 105 * 0 <= allowedSwaps.length <= 105 * allowedSwaps[i].length == 2 * 0 <= ai, bi <= n - 1 * ai != bi
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
