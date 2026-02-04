# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1232
标题: Sum of Mutated Array Closest to Target
难度: medium
链接: https://leetcode.cn/problems/sum-of-mutated-array-closest-to-target/
题目类型: 数组、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1300. 转变数组后最接近目标值的数组和 - 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近 target （最接近表示两者之差的绝对值最小）。 如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。 请注意，答案不一定是 arr 中的数字。 示例 1： 输入：arr = [4,9,3], target = 10 输出：3 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。 示例 2： 输入：arr = [2,3,5], target = 10 输出：5 示例 3： 输入：arr = [60864,25176,27249,21296,20204], target = 56803 输出：11361 提示： * 1 <= arr.length <= 10^4 * 1 <= arr[i], target <= 10^5
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定最优的 value 值。

算法步骤:
1. 对数组进行排序。
2. 初始化二分查找的左右边界，left 为 0，right 为数组的最大值。
3. 在每次迭代中，计算中间值 mid，并计算将所有大于 mid 的值变为 mid 后的数组和。
4. 根据当前数组和与 target 的差值调整二分查找的边界。
5. 最终返回最接近 target 的 value 值。

关键点:
- 使用前缀和来快速计算数组和。
- 通过二分查找来高效地找到最优的 value 值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log(max(arr)))，其中 n 是数组的长度，max(arr) 是数组的最大值。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def findBestValue(arr: List[int], target: int) -> int:
    """
    函数式接口 - 找到使得数组和最接近目标值的 value 值
    """
    arr.sort()
    n = len(arr)
    prefix_sum = 0
    left, right = 0, arr[-1]
    
    while left < right:
        mid = (left + right) // 2
        idx = bisect.bisect_left(arr, mid)
        current_sum = prefix_sum + (n - idx) * mid
        if current_sum == target:
            return mid
        elif current_sum < target:
            left = mid + 1
        else:
            right = mid
    
    # 检查 left 和 left - 1 哪个更接近 target
    idx = bisect.bisect_left(arr, left)
    current_sum_left = prefix_sum + (n - idx) * left
    idx = bisect.bisect_left(arr, left - 1)
    current_sum_left_minus_one = prefix_sum + (n - idx) * (left - 1)
    
    if abs(current_sum_left - target) < abs(current_sum_left_minus_one - target):
        return left
    else:
        return left - 1

Solution = create_solution(findBestValue)