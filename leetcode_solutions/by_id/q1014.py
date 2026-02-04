# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1014
标题: K Closest Points to Origin
难度: medium
链接: https://leetcode.cn/problems/k-closest-points-to-origin/
题目类型: 几何、数组、数学、分治、快速选择、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
973. 最接近原点的 K 个点 - 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。 这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)2 + (y1 - y2)2 ）。 你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。 示例 1： [https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg] 输入：points = [[1,3],[-2,2]], k = 1 输出：[[-2,2]] 解释： (1, 3) 和原点之间的距离为 sqrt(10)， (-2, 2) 和原点之间的距离为 sqrt(8)， 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。 示例 2： 输入：points = [[3,3],[5,-1],[-2,4]], k = 2 输出：[[3,3],[-2,4]] （答案 [[-2,4],[3,3]] 也会被接受。） 提示： * 1 <= k <= points.length <= 104 * -104 < xi, yi < 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快速选择算法来找到第 k 小的距离。

算法步骤:
1. 定义一个计算欧几里得距离平方的函数。
2. 使用快速选择算法在 O(n) 时间复杂度内找到第 k 小的距离。
3. 返回前 k 个最近的点。

关键点:
- 快速选择算法的时间复杂度期望为 O(n)，最坏情况下为 O(n^2)。
- 通过随机选择枢轴可以减少最坏情况的发生概率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)（期望），O(n^2)（最坏情况）
空间复杂度: O(1)（不考虑递归栈的空间）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import random

def euclidean_distance_squared(point: List[int]) -> int:
    return point[0] ** 2 + point[1] ** 2

def quick_select(points: List[List[int]], k: int) -> int:
    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_distance = euclidean_distance_squared(points[pivot_index])
        points[pivot_index], points[right] = points[right], points[pivot_index]
        store_index = left
        for i in range(left, right):
            if euclidean_distance_squared(points[i]) < pivot_distance:
                points[i], points[store_index] = points[store_index], points[i]
                store_index += 1
        points[store_index], points[right] = points[right], points[store_index]
        return store_index

    def select(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return left
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        if k_smallest == pivot_index:
            return k_smallest
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(points) - 1, k - 1)

def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    index = quick_select(points, k)
    return points[:k]

Solution = create_solution(k_closest_points)