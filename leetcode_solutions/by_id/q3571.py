# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3571
标题: Length of the Longest Increasing Path
难度: hard
链接: https://leetcode.cn/problems/length-of-the-longest-increasing-path/
题目类型: 数组、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3288. 最长上升路径的长度 - 给你一个长度为 n 的二维整数数组 coordinates 和一个整数 k ，其中 0 <= k < n 。 coordinates[i] = [xi, yi] 表示二维平面里一个点 (xi, yi) 。 如果一个点序列 (x1, y1), (x2, y2), (x3, y3), ..., (xm, ym) 满足以下条件，那么我们称它是一个长度为 m 的 上升序列 ： * 对于所有满足 1 <= i < m 的 i 都有 xi < xi + 1 且 yi < yi + 1 。 * 对于所有 1 <= i <= m 的 i 对应的点 (xi, yi) 都在给定的坐标数组里。 请你返回包含坐标 coordinates[k] 的 最长上升路径 的长度。 示例 1： 输入：coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1 输出：3 解释： (0, 0) ，(2, 2) ，(5, 3) 是包含坐标 (2, 2) 的最长上升路径。 示例 2： 输入：coordinates = [[2,1],[7,0],[5,6]], k = 2 输出：2 解释： (2, 1) ，(5, 6) 是包含坐标 (5, 6) 的最长上升路径。 提示： * 1 <= n == coordinates.length <= 105 * coordinates[i].length == 2 * 0 <= coordinates[i][0], coordinates[i][1] <= 109 * coordinates 中的元素 互不相同 。 * 0 <= k <= n - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和二分查找来找到最长上升路径。

算法步骤:
1. 将坐标按照 x 坐标排序，如果 x 相同则按 y 坐标排序。
2. 使用动态规划数组 dp 来记录以每个点结尾的最长上升路径长度。
3. 使用二分查找来找到当前点之前的最后一个 y 坐标小于当前点 y 坐标的点，并更新 dp 数组。
4. 返回 dp 数组中对应 coordinates[k] 的值。

关键点:
- 排序后使用二分查找来优化查找过程。
- 动态规划数组 dp 用于记录以每个点结尾的最长上升路径长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 coordinates 的长度。排序操作的时间复杂度是 O(n log n)，二分查找和动态规划更新的时间复杂度是 O(n log n)。
空间复杂度: O(n)，需要额外的空间来存储排序后的坐标和动态规划数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def length_of_longest_increasing_path(coordinates: List[List[int]], k: int) -> int:
    # 按 x 坐标排序，如果 x 相同则按 y 坐标排序
    sorted_coords = sorted(enumerate(coordinates), key=lambda x: (x[1][0], x[1][1]))
    
    # 初始化动态规划数组
    dp = [1] * len(coordinates)
    
    # 二分查找函数
    def binary_search(y: int, end: int) -> int:
        left, right = 0, end
        while left < right:
            mid = (left + right) // 2
            if sorted_coords[mid][1][1] < y:
                left = mid + 1
            else:
                right = mid
        return left
    
    # 更新动态规划数组
    for i in range(len(sorted_coords)):
        idx, (x, y) = sorted_coords[i]
        if i > 0:
            prev_idx = binary_search(y, i)
            if prev_idx < i and sorted_coords[prev_idx][1][1] < y:
                dp[idx] = max(dp[idx], dp[sorted_coords[prev_idx][0]] + 1)
    
    # 返回 dp 数组中对应 coordinates[k] 的值
    return dp[k]

Solution = create_solution(length_of_longest_increasing_path)