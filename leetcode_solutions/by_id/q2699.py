# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2699
标题: Count the Number of Fair Pairs
难度: medium
链接: https://leetcode.cn/problems/count-the-number-of-fair-pairs/
题目类型: 数组、双指针、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2563. 统计公平数对的数目 - 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。 如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ： * 0 <= i < j < n，且 * lower <= nums[i] + nums[j] <= upper 示例 1： 输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6 输出：6 解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。 示例 2： 输入：nums = [1,7,9,2,5], lower = 11, upper = 11 输出：1 解释：只有单个公平数对：(2,3) 。 提示： * 1 <= nums.length <= 105 * nums.length == n * -109 <= nums[i] <= 109 * -109 <= lower <= upper <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法来统计符合条件的数对。

算法步骤:
1. 对数组进行排序。
2. 初始化两个指针 left 和 right，分别指向数组的起始位置和末尾位置。
3. 遍历数组，对于每个元素 nums[i]，使用双指针找到所有满足条件的数对。
4. 更新计数器，记录满足条件的数对数量。

关键点:
- 通过排序和双指针可以高效地找到所有满足条件的数对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_fair_pairs(nums: List[int], lower: int, upper: int) -> int:
    """
    函数式接口 - 统计公平数对的数目
    """
    nums.sort()  # 对数组进行排序
    n = len(nums)
    count = 0

    for i in range(n):
        left, right = i + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[i] + nums[mid] >= lower:
                right = mid - 1
            else:
                left = mid + 1

        l = left

        left, right = i + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[i] + nums[mid] > upper:
                right = mid - 1
            else:
                left = mid + 1

        r = right

        count += r - l + 1

    return count


Solution = create_solution(count_fair_pairs)