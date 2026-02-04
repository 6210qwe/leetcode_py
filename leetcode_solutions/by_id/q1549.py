# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1549
标题: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
难度: medium
链接: https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
题目类型: 队列、数组、有序集合、滑动窗口、单调队列、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1438. 绝对差不超过限制的最长连续子数组 - 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit。 示例 1： 输入：nums = [8,2,4,7], limit = 4 输出：2 解释：所有子数组如下： [8] 最大绝对差 |8-8| = 0 <= 4. [8,2] 最大绝对差 |8-2| = 6 > 4. [8,2,4] 最大绝对差 |8-2| = 6 > 4. [8,2,4,7] 最大绝对差 |8-2| = 6 > 4. [2] 最大绝对差 |2-2| = 0 <= 4. [2,4] 最大绝对差 |2-4| = 2 <= 4. [2,4,7] 最大绝对差 |2-7| = 5 > 4. [4] 最大绝对差 |4-4| = 0 <= 4. [4,7] 最大绝对差 |4-7| = 3 <= 4. [7] 最大绝对差 |7-7| = 0 <= 4. 因此，满足题意的最长子数组的长度为 2 。 示例 2： 输入：nums = [10,1,2,4,7,2], limit = 5 输出：4 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。 示例 3： 输入：nums = [4,2,2,2,4,4,2,2], limit = 0 输出：3 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * 0 <= limit <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和两个双端队列来维护当前窗口内的最大值和最小值。

算法步骤:
1. 初始化两个双端队列 max_deque 和 min_deque 来分别维护当前窗口内的最大值和最小值。
2. 使用两个指针 left 和 right 来表示当前窗口的左右边界。
3. 移动右指针 right，将新元素加入窗口，并更新 max_deque 和 min_deque。
4. 如果当前窗口内的最大值和最小值之差大于 limit，则移动左指针 left 缩小窗口，直到满足条件。
5. 记录当前窗口的最大长度。

关键点:
- 使用双端队列来维护窗口内的最大值和最小值，确保在 O(1) 时间内获取到最大值和最小值。
- 通过滑动窗口技术，可以在 O(n) 时间复杂度内找到满足条件的最长子数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_subarray(nums: List[int], limit: int) -> int:
    """
    函数式接口 - 返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit。
    """
    from collections import deque

    max_deque = deque()
    min_deque = deque()
    left = 0
    max_length = 0

    for right in range(len(nums)):
        # 更新最大值队列
        while max_deque and nums[right] > max_deque[-1]:
            max_deque.pop()
        max_deque.append(nums[right])

        # 更新最小值队列
        while min_deque and nums[right] < min_deque[-1]:
            min_deque.pop()
        min_deque.append(nums[right])

        # 检查当前窗口是否满足条件
        while max_deque[0] - min_deque[0] > limit:
            if max_deque[0] == nums[left]:
                max_deque.popleft()
            if min_deque[0] == nums[left]:
                min_deque.popleft()
            left += 1

        # 更新最大长度
        max_length = max(max_length, right - left + 1)

    return max_length


Solution = create_solution(longest_subarray)