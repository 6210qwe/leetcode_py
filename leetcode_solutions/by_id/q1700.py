# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1700
标题: Minimum Time to Make Rope Colorful
难度: medium
链接: https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/
题目类型: 贪心、数组、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1578. 使绳子变成彩色的最短时间 - Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。 Alice 想要把绳子装扮成 五颜六色的 ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 彩色 。给你一个 下标从 0 开始 的整数数组 neededTime ，其中 neededTime[i] 是 Bob 从绳子上移除第 i 个气球需要的时间（以秒为单位）。 返回 Bob 使绳子变成 彩色 需要的 最少时间 。 示例 1： [https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg] 输入：colors = "abaac", neededTime = [1,2,3,4,5] 输出：3 解释：在上图中，'a' 是蓝色，'b' 是红色且 'c' 是绿色。 Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。 移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。 示例 2： [https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg] 输入：colors = "abc", neededTime = [1,2,3] 输出：0 解释：绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。 示例 3： [https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg] 输入：colors = "aabaa", neededTime = [1,2,3,4,1] 输出：2 解释：Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。 移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。 提示： * n == colors.length == neededTime.length * 1 <= n <= 105 * 1 <= neededTime[i] <= 104 * colors 仅由小写英文字母组成
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
