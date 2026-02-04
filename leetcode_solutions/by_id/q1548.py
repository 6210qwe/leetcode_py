# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1548
标题: Check If All 1's Are at Least Length K Places Away
难度: easy
链接: https://leetcode.cn/problems/check-if-all-1s-are-at-least-length-k-places-away/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1437. 是否所有 1 都至少相隔 k 个元素 - 给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 true ；否则，返回 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png] 输入：nums = [1,0,0,0,1,0,0,1], k = 2 输出：true 解释：每个 1 都至少相隔 2 个元素。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png] 输入：nums = [1,0,0,1,0,1], k = 2 输出：false 解释：第二个 1 和第三个 1 之间只隔了 1 个元素。 提示： * 1 <= nums.length <= 105 * 0 <= k <= nums.length * nums[i] 的值为 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过一次遍历数组来检查相邻的 1 之间的距离是否满足条件。

算法步骤:
1. 初始化一个变量 `last_one_index` 用于记录上一个 1 的位置。
2. 遍历数组，对于每一个 1，检查它与上一个 1 之间的距离是否小于 k。
3. 如果发现不满足条件的情况，返回 False。
4. 如果遍历完整个数组都满足条件，返回 True。

关键点:
- 通过一次遍历和一个变量来记录上一个 1 的位置，从而实现 O(n) 的时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], k: int) -> bool:
    """
    函数式接口 - 检查所有 1 是否至少相隔 k 个元素
    """
    last_one_index = -k - 1  # 初始化为 -k-1 以确保第一个 1 不会误判
    for i, num in enumerate(nums):
        if num == 1:
            if i - last_one_index <= k:
                return False
            last_one_index = i
    return True


Solution = create_solution(solution_function_name)