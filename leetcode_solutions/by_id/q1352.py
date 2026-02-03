# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1352
标题: Maximum Profit in Job Scheduling
难度: hard
链接: https://leetcode.cn/problems/maximum-profit-in-job-scheduling/
题目类型: 数组、二分查找、动态规划、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1235. 规划兼职工作 - 你打算利用空闲时间来做兼职工作赚些零花钱。 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。 注意，时间上出现重叠的 2 份工作不能同时进行。 如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/19/sample1_1584.png] 输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70] 输出：120 解释： 我们选出第 1 份和第 4 份工作， 时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/19/sample22_1584.png] 输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60] 输出：150 解释： 我们选择第 1，4，5 份工作。 共获得报酬 150 = 20 + 70 + 60。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/19/sample3_1584.png] 输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4] 输出：6 提示： * 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4 * 1 <= startTime[i] < endTime[i] <= 10^9 * 1 <= profit[i] <= 10^4
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
