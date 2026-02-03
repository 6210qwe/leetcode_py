# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000244
标题: 乘积小于 K 的子数组
难度: medium
链接: https://leetcode.cn/problems/ZVAVXX/
题目类型: 数组、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 009. 乘积小于 K 的子数组 - 给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。 示例 1： 输入: nums = [10,5,2,6], k = 100 输出: 8 解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。 示例 2： 输入: nums = [1,2,3], k = 0 输出: 0 提示： * 1 <= nums.length <= 3 * 104 * 1 <= nums[i] <= 1000 * 0 <= k <= 106 注意：本题与主站 713 题相同：https://leetcode.cn/problems/subarray-product-less-than-k/ [https://leetcode.cn/problems/subarray-product-less-than-k/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 正数数组 + 滑动窗口维护乘积

算法步骤:
1. 若 k <= 1，则所有子数组乘积都 >= 1 >= k，不可能小于 k，直接返回 0
2. 使用 left 指针、当前乘积 prod 和答案 ans
3. 遍历 right 从 0 到 n-1：
   - prod *= nums[right]
   - 当 prod >= k 时，说明窗口乘积过大，需要移动左指针：
       * prod //= nums[left]
       * left += 1
   - 此时窗口 [left, right] 内所有以 right 为结尾的子数组中，有 right-left+1 个子数组满足乘积 < k
   - 将其加到 ans 中
4. 返回 ans

关键点:
- 所有 nums[i] >= 1，窗口右移时乘积单调增加，左移时单调减少
- 每个元素最多进出窗口一次，整体 O(n)
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


def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
    """
    函数式接口 - 乘积小于 K 的子数组
    """
    if k <= 1:
        return 0
    prod = 1
    left = 0
    ans = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k and left <= right:
            prod //= nums[left]
            left += 1
        ans += right - left + 1
    return ans


Solution = create_solution(num_subarray_product_less_than_k)
