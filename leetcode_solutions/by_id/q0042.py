# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 42
标题: Trapping Rain Water
难度: hard
链接: https://leetcode.cn/problems/trapping-rain-water/
题目类型: 栈、数组、双指针、动态规划、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
42. 接雨水 - 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png] 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1] 输出：6 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 示例 2： 输入：height = [4,2,0,3,2,5] 输出：9 提示： * n == height.length * 1 <= n <= 2 * 104 * 0 <= height[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针，从两端向中间移动，维护左右最大高度

算法步骤:
1. 使用左右两个指针
2. 维护left_max和right_max，分别表示左右两边的最大高度
3. 如果left_max < right_max，处理左边，否则处理右边
4. 每个位置能接的雨水 = min(left_max, right_max) - height[i]

关键点:
- 使用双指针优化空间
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历数组一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def trapping_rain_water(height: List[int]) -> int:
    """
    函数式接口 - 接雨水
    
    实现思路:
    使用双指针，从两端向中间移动，维护左右最大高度。
    
    Args:
        height: 每个柱子的高度数组
        
    Returns:
        能接的雨水总量
        
    Example:
        >>> trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1])
        6
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


# 自动生成Solution类（无需手动编写）
Solution = create_solution(trapping_rain_water)
