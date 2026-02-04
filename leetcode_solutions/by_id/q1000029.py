# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000029
标题: Volume of Histogram LCCI
难度: hard
链接: https://leetcode.cn/problems/volume-of-histogram-lcci/
题目类型: 栈、数组、双指针、动态规划、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.21. 直方图的水量 - 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png] 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。 示例： 输入：[0,1,0,2,1,0,1,3,2,1,2,1] 输出：6
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法来计算直方图中的水量。

算法步骤:
1. 初始化两个指针 left 和 right 分别指向数组的两端。
2. 初始化两个变量 left_max 和 right_max 分别记录从左到右和从右到左的最大高度。
3. 当 left 小于 right 时，进行以下操作：
   - 如果 height[left] 小于 height[right]，则更新 left_max 并计算左侧的水量。
   - 否则，更新 right_max 并计算右侧的水量。
4. 返回总水量。

关键点:
- 使用双指针法可以避免重复计算，时间复杂度为 O(n)。
- 通过维护左右两侧的最大高度，可以有效地计算每个位置的水量。
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


def solution_function_name(height: List[int]) -> int:
    """
    函数式接口 - 计算直方图中的水量
    """
    if not height:
        return 0

    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


Solution = create_solution(solution_function_name)