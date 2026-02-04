# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3170
标题: Find Indices With Index and Value Difference II
难度: medium
链接: https://leetcode.cn/problems/find-indices-with-index-and-value-difference-ii/
题目类型: 数组、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2905. 找出满足差值条件的下标 II - 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，以及整数 indexDifference 和整数 valueDifference 。 你的任务是从范围 [0, n - 1] 内找出 2 个满足下述所有条件的下标 i 和 j ： * abs(i - j) >= indexDifference 且 * abs(nums[i] - nums[j]) >= valueDifference 返回整数数组 answer。如果存在满足题目要求的两个下标，则 answer = [i, j] ；否则，answer = [-1, -1] 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。 注意：i 和 j 可能 相等 。 示例 1： 输入：nums = [5,1,4,1], indexDifference = 2, valueDifference = 4 输出：[0,3] 解释：在示例中，可以选择 i = 0 和 j = 3 。 abs(0 - 3) >= 2 且 abs(nums[0] - nums[3]) >= 4 。 因此，[0,3] 是一个符合题目要求的答案。 [3,0] 也是符合题目要求的答案。 示例 2： 输入：nums = [2,1], indexDifference = 0, valueDifference = 0 输出：[0,0] 解释： 在示例中，可以选择 i = 0 和 j = 0 。 abs(0 - 0) >= 0 且 abs(nums[0] - nums[0]) >= 0 。 因此，[0,0] 是一个符合题目要求的答案。 [0,1]、[1,0] 和 [1,1] 也是符合题目要求的答案。 示例 3： 输入：nums = [1,2,3], indexDifference = 2, valueDifference = 4 输出：[-1,-1] 解释：在示例中，可以证明无法找出 2 个满足所有条件的下标。 因此，返回 [-1,-1] 。 提示： * 1 <= n == nums.length <= 105 * 0 <= nums[i] <= 109 * 0 <= indexDifference <= 105 * 0 <= valueDifference <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到满足条件的下标对。

算法步骤:
1. 初始化两个指针 `left` 和 `right`，分别指向数组的起始和 `indexDifference` 位置。
2. 使用两个变量 `min_index` 和 `max_index` 来记录当前窗口内的最小值和最大值的下标。
3. 滑动窗口，更新 `min_index` 和 `max_index`，并检查是否满足 `abs(nums[min_index] - nums[right]) >= valueDifference` 或 `abs(nums[max_index] - nums[right]) >= valueDifference`。
4. 如果找到满足条件的下标对，返回 `[min_index, right]` 或 `[max_index, right]`。
5. 如果遍历完数组仍未找到满足条件的下标对，返回 `[-1, -1]`。

关键点:
- 使用滑动窗口来维护当前窗口内的最小值和最大值的下标。
- 每次移动右指针时，更新最小值和最大值的下标。
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

from typing import List

def find_indices_with_difference(nums: List[int], index_difference: int, value_difference: int) -> List[int]:
    n = len(nums)
    if n < 2:
        return [-1, -1]

    left, right = 0, index_difference
    min_index, max_index = left, left

    while right < n:
        if nums[right - index_difference] < nums[min_index]:
            min_index = right - index_difference
        if nums[right - index_difference] > nums[max_index]:
            max_index = right - index_difference

        if abs(nums[min_index] - nums[right]) >= value_difference:
            return [min_index, right]
        if abs(nums[max_index] - nums[right]) >= value_difference:
            return [max_index, right]

        right += 1

    return [-1, -1]

Solution = create_solution(find_indices_with_difference)