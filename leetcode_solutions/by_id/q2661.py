# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2661
标题: Smallest Missing Non-negative Integer After Operations
难度: medium
链接: https://leetcode.cn/problems/smallest-missing-non-negative-integer-after-operations/
题目类型: 贪心、数组、哈希表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2598. 执行操作后的最大 MEX - 给你一个下标从 0 开始的整数数组 nums 和一个整数 value 。 在一步操作中，你可以对 nums 中的任一元素加上或减去 value 。 * 例如，如果 nums = [1,2,3] 且 value = 2 ，你可以选择 nums[0] 减去 value ，得到 nums = [-1,2,3] 。 数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。 * 例如，[-1,2,3] 的 MEX 是 0 ，而 [1,0,3] 的 MEX 是 2 。 返回在执行上述操作 任意次 后，nums 的最大 MEX 。 示例 1： 输入：nums = [1,-10,7,13,6,8], value = 5 输出：4 解释：执行下述操作可以得到这一结果： - nums[1] 加上 value 两次，nums = [1,0,7,13,6,8] - nums[2] 减去 value 一次，nums = [1,0,2,13,6,8] - nums[3] 减去 value 两次，nums = [1,0,2,3,6,8] nums 的 MEX 是 4 。可以证明 4 是可以取到的最大 MEX 。 示例 2： 输入：nums = [1,-10,7,13,6,8], value = 7 输出：2 解释：执行下述操作可以得到这一结果： - nums[2] 减去 value 一次，nums = [1,-10,0,13,6,8] nums 的 MEX 是 2 。可以证明 2 是可以取到的最大 MEX 。 提示： * 1 <= nums.length, value <= 105 * -109 <= nums[i] <= 109
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
