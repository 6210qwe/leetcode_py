# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000242
标题: 长度最小的子数组
难度: medium
链接: https://leetcode.cn/problems/2VG8Kg/
题目类型: 数组、二分查找、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 008. 长度最小的子数组 - 给定一个含有 n 个正整数的数组和一个正整数 target 。 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。 示例 1： 输入：target = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。 示例 2： 输入：target = 4, nums = [1,4,4] 输出：1 示例 3： 输入：target = 11, nums = [1,1,1,1,1,1,1,1] 输出：0 提示： * 1 <= target <= 109 * 1 <= nums.length <= 105 * 1 <= nums[i] <= 105 进阶： * 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。 注意：本题与主站 209 题相同：https://leetcode.cn/problems/minimum-size-subarray-sum/ [https://leetcode.cn/problems/minimum-size-subarray-sum/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口维护当前子数组和

算法步骤:
1. 使用两个指针 left, right 和当前窗口和 window_sum
2. 右指针 right 从 0 到 n-1 遍历，将 nums[right] 加入 window_sum
3. 当 window_sum >= target 时，尝试收缩左边界：
   - 更新最小长度 ans = min(ans, right - left + 1)
   - 将 nums[left] 从 window_sum 中减去，left += 1
4. 遍历结束后，若 ans 仍为无穷大，返回 0，否则返回 ans

关键点:
- 所有 nums[i] > 0，窗口右移时和单调增加，左移时和单调减少，保证 O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每个元素最多进出窗口一次
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_sub_array_len(target: int, nums: List[int]) -> int:
    """
    函数式接口 - 长度最小的子数组
    """
    n = len(nums)
    left = 0
    window_sum = 0
    ans = float("inf")

    for right in range(n):
        window_sum += nums[right]
        while window_sum >= target:
            ans = min(ans, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if ans == float("inf") else int(ans)


Solution = create_solution(min_sub_array_len)
