# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4141
标题: Count Elements With at Least K Greater Values
难度: medium
链接: https://leetcode.cn/problems/count-elements-with-at-least-k-greater-values/
题目类型: 数组、二分查找、分治、快速选择、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3759. 统计合格元素的数目 - 给你一个长度为 n 的整数数组 nums 和一个整数 k。 如果数组 nums 中的某个元素满足以下条件，则称其为 合格元素：存在 至少 k 个元素 严格大于 它。 返回一个整数，表示数组 nums 中合格元素的总数。 示例 1： 输入： nums = [3,1,2], k = 1 输出： 2 解释： 元素 1 和 2 均有至少 k = 1 个元素大于它们。 没有元素比 3 更大。因此答案是 2。 示例 2： 输入： nums = [5,5,5], k = 2 输出： 0 解释： 由于所有元素都等于 5，没有任何元素比其他元素大。因此答案是 0。 提示： * 1 <= n == nums.length <= 105 * 1 <= nums[i] <= 109 * 0 <= k < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 对数组进行排序，然后通过二分查找找到每个元素在排序数组中的位置，从而确定有多少个元素大于它。

算法步骤:
1. 对数组进行排序。
2. 使用二分查找找到每个元素在排序数组中的位置。
3. 计算每个元素右侧有多少个元素，并判断是否满足条件。

关键点:
- 排序后使用二分查找可以高效地找到每个元素的位置。
- 通过计算每个元素右侧的元素数量来判断是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序的时间复杂度为 O(n log n)，二分查找的时间复杂度为 O(log n)，总的时间复杂度为 O(n log n)。
空间复杂度: O(1) - 除了输入数组外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_elements_with_at_least_k_greater_values(nums: List[int], k: int) -> int:
    """
    函数式接口 - 统计数组中至少有 k 个元素严格大于它的元素个数
    """
    # 对数组进行排序
    sorted_nums = sorted(nums)
    
    # 计算每个元素右侧有多少个元素
    def count_greater_elements(x: int) -> int:
        left, right = 0, len(sorted_nums)
        while left < right:
            mid = (left + right) // 2
            if sorted_nums[mid] > x:
                right = mid
            else:
                left = mid + 1
        return len(sorted_nums) - left
    
    # 统计符合条件的元素个数
    count = 0
    for num in set(nums):
        if count_greater_elements(num) >= k:
            count += nums.count(num)
    
    return count


Solution = create_solution(count_elements_with_at_least_k_greater_values)