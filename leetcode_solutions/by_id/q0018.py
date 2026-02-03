# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 18
标题: 4Sum
难度: medium
链接: https://leetcode.cn/problems/4sum/
题目类型: 数组、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
18. 四数之和 - 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： * 0 <= a, b, c, d < n * a、b、c 和 d 互不相同 * nums[a] + nums[b] + nums[c] + nums[d] == target 你可以按 任意顺序 返回答案 。 示例 1： 输入：nums = [1,0,-1,0,-2,2], target = 0 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] 示例 2： 输入：nums = [2,2,2,2,2], target = 8 输出：[[2,2,2,2]] 提示： * 1 <= nums.length <= 200 * -109 <= nums[i] <= 109 * -109 <= target <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 排序 + 双重循环 + 双指针，固定前两个数，用双指针找后两个数

算法步骤:
1. 对数组进行排序
2. 双重循环固定前两个数nums[i]和nums[j]
3. 使用双指针left和right在剩余部分寻找后两个数：
   - 如果nums[i] + nums[j] + nums[left] + nums[right] == target，添加到结果
   - 如果和小于target，left右移
   - 如果和大于target，right左移
4. 跳过重复元素避免重复结果
5. 返回所有不重复的四元组

关键点:
- 排序后可以使用双指针，避免四重循环
- 需要跳过重复元素，避免重复结果
- 时间复杂度O(n³)，空间复杂度O(1)（不考虑结果数组）
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n³) - 排序O(nlogn) + 三重循环O(n³)
空间复杂度: O(1) - 只使用常数额外空间（不考虑结果数组）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    函数式接口 - 排序 + 双重循环 + 双指针实现
    
    实现思路:
    先排序，然后固定前两个数，使用双指针在剩余部分寻找后两个数。
    
    Args:
        nums: 整数数组
        target: 目标值
        
    Returns:
        所有和为target且不重复的四元组列表
        
    Example:
        >>> four_sum([1,0,-1,0,-2,2], 0)
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> four_sum([2,2,2,2,2], 8)
        [[2, 2, 2, 2]]
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        # 跳过重复的第一个数
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            # 跳过重复的第二个数
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # 跳过重复的left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(four_sum)
