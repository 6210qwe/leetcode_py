# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000239
标题: 三数之和
难度: medium
链接: https://leetcode.cn/problems/1fGaJU/
题目类型: 数组、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 007. 三数之和 - 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。 示例 1： 输入：nums = [-1,0,1,2,-1,-4] 输出：[[-1,-1,2],[-1,0,1]] 示例 2： 输入：nums = [] 输出：[] 示例 3： 输入：nums = [0] 输出：[] 提示： * 0 <= nums.length <= 3000 * -105 <= nums[i] <= 105 注意：本题与主站 15 题相同：https://leetcode.cn/problems/3sum/ [https://leetcode.cn/problems/3sum/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 排序 + 双指针枚举三元组

算法步骤:
1. 若数组长度小于 3，直接返回空列表
2. 对数组 nums 排序
3. 遍历下标 i 作为第一个数：
   - 若 nums[i] > 0，则后面的数都 >= 0，不可能和为 0，直接 break
   - 若 i > 0 且 nums[i] == nums[i-1]，跳过以避免重复三元组
   - 使用左右指针 left = i+1, right = n-1：
       * 计算 s = nums[i] + nums[left] + nums[right]
       * 若 s == 0，加入答案，并跳过所有与 nums[left]、nums[right] 相等的元素
       * 若 s < 0，left += 1
       * 若 s > 0，right -= 1

关键点:
- 排序后可以用双指针在 O(n^2) 内找到所有不重复三元组
- 需要小心地跳过重复的数，避免重复解
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 外层 O(n)，内层双指针 O(n)
空间复杂度: O(1) 额外空间（不计结果集）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    函数式接口 - 三数之和
    """
    res: List[List[int]] = []
    nums.sort()
    n = len(nums)

    for i in range(n):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left_val = nums[left]
                right_val = nums[right]
                while left < right and nums[left] == left_val:
                    left += 1
                while left < right and nums[right] == right_val:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res


Solution = create_solution(three_sum)
