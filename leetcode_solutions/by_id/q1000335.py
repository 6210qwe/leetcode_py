# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000335
标题: 按权重随机选择
难度: medium
链接: https://leetcode.cn/problems/cuyjEf/
题目类型: 数组、数学、二分查找、前缀和、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 071. 按权重随机选择 - 给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标 i，选取下标 i 的概率与 w[i] 成正比。 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。 也就是说，选取下标 i 的概率为 w[i] / sum(w) 。 示例 1： 输入： inputs = ["Solution","pickIndex"] inputs = [[[1]],[]] 输出： [null,0] 解释： Solution solution = new Solution([1]); solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。 示例 2： 输入： inputs = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"] inputs = [[[1,3]],[],[],[],[],[]] 输出： [null,1,1,1,1,0] 解释： Solution solution = new Solution([1, 3]); solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。 solution.pickIndex(); // 返回 1 solution.pickIndex(); // 返回 1 solution.pickIndex(); // 返回 1 solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。 由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的: [null,1,1,1,1,0] [null,1,1,1,1,1] [null,1,1,1,0,0] [null,1,1,1,0,1] [null,1,0,1,0,0] ...... 诸若此类。 提示： * 1 <= w.length <= 10000 * 1 <= w[i] <= 10^5 * pickIndex 将被调用不超过 10000 次 注意：本题与主站 528 题相同： https://leetcode.cn/problems/random-pick-with-weight/ [https://leetcode.cn/problems/random-pick-with-weight/]
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
