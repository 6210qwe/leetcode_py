# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3496
标题: Minimum Number of Seconds to Make Mountain Height Zero
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/
题目类型: 贪心、数组、数学、二分查找、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3296. 移山所需的最少秒数 - 给你一个整数 mountainHeight 表示山的高度。 同时给你一个整数数组 workerTimes，表示工人们的工作时间（单位：秒）。 工人们需要 同时 进行工作以 降低 山的高度。对于工人 i : * 山的高度降低 x，需要花费 workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x 秒。例如： * 山的高度降低 1，需要 workerTimes[i] 秒。 * 山的高度降低 2，需要 workerTimes[i] + workerTimes[i] * 2 秒，依此类推。 返回一个整数，表示工人们使山的高度降低到 0 所需的 最少 秒数。 示例 1： 输入： mountainHeight = 4, workerTimes = [2,1,1] 输出： 3 解释： 将山的高度降低到 0 的一种方式是： * 工人 0 将高度降低 1，花费 workerTimes[0] = 2 秒。 * 工人 1 将高度降低 2，花费 workerTimes[1] + workerTimes[1] * 2 = 3 秒。 * 工人 2 将高度降低 1，花费 workerTimes[2] = 1 秒。 因为工人同时工作，所需的最少时间为 max(2, 3, 1) = 3 秒。 示例 2： 输入： mountainHeight = 10, workerTimes = [3,2,2,4] 输出： 12 解释： * 工人 0 将高度降低 2，花费 workerTimes[0] + workerTimes[0] * 2 = 9 秒。 * 工人 1 将高度降低 3，花费 workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12 秒。 * 工人 2 将高度降低 3，花费 workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12 秒。 * 工人 3 将高度降低 2，花费 workerTimes[3] + workerTimes[3] * 2 = 12 秒。 所需的最少时间为 max(9, 12, 12, 12) = 12 秒。 示例 3： 输入： mountainHeight = 5, workerTimes = [1] 输出： 15 解释： 这个示例中只有一个工人，所以答案是 workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15 秒。 提示： * 1 <= mountainHeight <= 105 * 1 <= workerTimes.length <= 104 * 1 <= workerTimes[i] <= 106
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
