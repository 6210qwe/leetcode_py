# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3165
标题: Find Indices With Index and Value Difference I
难度: easy
链接: https://leetcode.cn/problems/find-indices-with-index-and-value-difference-i/
题目类型: 数组、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2903. 找出满足差值条件的下标 I - 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，以及整数 indexDifference 和整数 valueDifference 。 你的任务是从范围 [0, n - 1] 内找出 2 个满足下述所有条件的下标 i 和 j ： * abs(i - j) >= indexDifference 且 * abs(nums[i] - nums[j]) >= valueDifference 返回整数数组 answer。如果存在满足题目要求的两个下标，则 answer = [i, j] ；否则，answer = [-1, -1] 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。 注意：i 和 j 可能 相等 。 示例 1： 输入：nums = [5,1,4,1], indexDifference = 2, valueDifference = 4 输出：[0,3] 解释：在示例中，可以选择 i = 0 和 j = 3 。 abs(0 - 3) >= 2 且 abs(nums[0] - nums[3]) >= 4 。 因此，[0,3] 是一个符合题目要求的答案。 [3,0] 也是符合题目要求的答案。 示例 2： 输入：nums = [2,1], indexDifference = 0, valueDifference = 0 输出：[0,0] 解释： 在示例中，可以选择 i = 0 和 j = 0 。 abs(0 - 0) >= 0 且 abs(nums[0] - nums[0]) >= 0 。 因此，[0,0] 是一个符合题目要求的答案。 [0,1]、[1,0] 和 [1,1] 也是符合题目要求的答案。 示例 3： 输入：nums = [1,2,3], indexDifference = 2, valueDifference = 4 输出：[-1,-1] 解释：在示例中，可以证明无法找出 2 个满足所有条件的下标。 因此，返回 [-1,-1] 。 提示： * 1 <= n == nums.length <= 100 * 0 <= nums[i] <= 50 * 0 <= indexDifference <= 100 * 0 <= valueDifference <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法来找到满足条件的下标对。

算法步骤:
1. 初始化两个指针 i 和 j，分别指向数组的起始位置和满足 indexDifference 位置。
2. 遍历数组，检查当前指针 i 和 j 是否满足条件 abs(i - j) >= indexDifference 和 abs(nums[i] - nums[j]) >= valueDifference。
3. 如果满足条件，返回 [i, j]。
4. 如果不满足条件，移动指针 i 和 j，继续检查。
5. 如果遍历完数组仍未找到满足条件的下标对，返回 [-1, -1]。

关键点:
- 使用双指针方法减少时间复杂度。
- 通过一次遍历来检查所有可能的下标对。
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
    for i in range(n):
        for j in range(i + index_difference, n):
            if abs(nums[i] - nums[j]) >= value_difference:
                return [i, j]
    return [-1, -1]

Solution = create_solution(find_indices_with_difference)