# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 16
标题: 3Sum Closest
难度: medium
链接: https://leetcode.cn/problems/3sum-closest/
题目类型: 数组、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
16. 最接近的三数之和 - 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。 返回这三个数的和。 假定每组输入只存在恰好一个解。 示例 1： 输入：nums = [-1,2,1,-4], target = 1 输出：2 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。 示例 2： 输入：nums = [0,0,0], target = 1 输出：0 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。 提示： * 3 <= nums.length <= 1000 * -1000 <= nums[i] <= 1000 * -104 <= target <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 排序 + 双指针，类似三数之和，但寻找最接近target的和

算法步骤:
1. 对数组进行排序
2. 初始化最接近的和为前三个数的和
3. 遍历数组，固定第一个数nums[i]
4. 使用双指针left和right在剩余部分寻找另外两个数：
   - 计算当前三数之和
   - 如果更接近target，更新最接近的和
   - 根据当前和与target的关系移动指针
5. 返回最接近的和

关键点:
- 排序后使用双指针，时间复杂度O(n²)
- 需要跟踪最接近target的和，而不是等于target
- 时间复杂度O(n²)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n²) - 排序O(nlogn) + 双重循环O(n²)
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    函数式接口 - 排序 + 双指针实现
    
    实现思路:
    先排序，然后固定第一个数，使用双指针在剩余部分寻找另外两个数，找到最接近target的和。
    
    Args:
        nums: 整数数组
        target: 目标值
        
    Returns:
        最接近target的三数之和
        
    Example:
        >>> three_sum_closest([-1,2,1,-4], 1)
        2
        >>> three_sum_closest([0,0,0], 1)
        0
    """
    nums.sort()
    n = len(nums)
    closest_sum = nums[0] + nums[1] + nums[2]
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            # 如果当前和更接近target，更新closest_sum
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # 如果等于target，直接返回
                return current_sum
    
    return closest_sum


# 自动生成Solution类（无需手动编写）
Solution = create_solution(three_sum_closest)
