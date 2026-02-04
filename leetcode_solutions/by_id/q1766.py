# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1766
标题: Minimum Number of Removals to Make Mountain Array
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/
题目类型: 贪心、数组、二分查找、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1671. 得到山形数组的最少删除次数 - 我们定义 arr 是 山形数组 当且仅当它满足： * arr.length >= 3 * 存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且： * arr[0] < arr[1] < ... < arr[i - 1] < arr[i] * arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 给你整数数组 nums ，请你返回将 nums 变成 山形状数组 的 最少 删除次数。 示例 1： 输入：nums = [1,3,1] 输出：0 解释：数组本身就是山形数组，所以我们不需要删除任何元素。 示例 2： 输入：nums = [2,1,1,5,6,2,3,1] 输出：3 解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。 提示： * 3 <= nums.length <= 1000 * 1 <= nums[i] <= 109 * 题目保证 nums 删除一些元素后一定能得到山形数组。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划计算每个位置作为山顶时的最长递增子序列和最长递减子序列，然后通过这些信息找到最小删除次数。

算法步骤:
1. 计算每个位置的最长递增子序列长度。
2. 计算每个位置的最长递减子序列长度。
3. 遍历所有可能的山顶位置，计算删除次数，并取最小值。

关键点:
- 使用二分查找优化最长递增子序列的计算。
- 通过两次遍历分别计算最长递增子序列和最长递减子序列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def min_removals_to_make_mountain_array(nums: List[int]) -> int:
    """
    函数式接口 - 返回将 nums 变成山形数组的最少删除次数
    """
    n = len(nums)
    if n < 3:
        return 0

    # 计算最长递增子序列长度
    def length_of_lis(nums):
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)

    # 计算最长递减子序列长度
    def length_of_lds(nums):
        dp = []
        for num in reversed(nums):
            idx = bisect.bisect_left(dp, -num)
            if idx == len(dp):
                dp.append(-num)
            else:
                dp[idx] = -num
        return len(dp)

    import bisect

    lis = [length_of_lis(nums[:i+1]) for i in range(n)]
    lds = [length_of_lds(nums[i:]) for i in range(n)]

    # 计算最小删除次数
    min_removals = float('inf')
    for i in range(1, n-1):
        if lis[i] > 1 and lds[i] > 1:
            min_removals = min(min_removals, n - (lis[i] + lds[i] - 1))

    return min_removals

Solution = create_solution(min_removals_to_make_mountain_array)