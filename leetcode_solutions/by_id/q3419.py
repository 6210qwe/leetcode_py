# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3419
标题: Maximum Points Inside the Square
难度: medium
链接: https://leetcode.cn/problems/maximum-points-inside-the-square/
题目类型: 数组、哈希表、字符串、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3143. 正方形中的最多点数 - 给你一个二维数组 points 和一个字符串 s ，其中 points[i] 表示第 i 个点的坐标，s[i] 表示第 i 个点的 标签 。 如果一个正方形的中心在 (0, 0) ，所有边都平行于坐标轴，且正方形内 不 存在标签相同的两个点，那么我们称这个正方形是 合法 的。 请你返回 合法 正方形中可以包含的 最多 点数。 注意： * 如果一个点位于正方形的边上或者在边以内，则认为该点位于正方形内。 * 正方形的边长可以为零。 示例 1： [https://assets.leetcode.com/uploads/2024/03/29/3708-tc1.png] 输入：points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca" 输出：2 解释： 边长为 4 的正方形包含两个点 points[0] 和 points[1] 。 示例 2： [https://assets.leetcode.com/uploads/2024/03/29/3708-tc2.png] 输入：points = [[1,1],[-2,-2],[-2,2]], s = "abb" 输出：1 解释： 边长为 2 的正方形包含 1 个点 points[0] 。 示例 3： 输入：points = [[1,1],[-1,-1],[2,-2]], s = "ccd" 输出：0 解释： 任何正方形都无法只包含 points[0] 和 points[1] 中的一个点，所以合法正方形中都不包含任何点。 提示： * 1 <= s.length, points.length <= 105 * points[i].length == 2 * -109 <= points[i][0], points[i][1] <= 109 * s.length == points.length * points 中的点坐标互不相同。 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定正方形的最大边长，并检查在这个边长下是否满足条件。

算法步骤:
1. 将点按距离原点的距离排序。
2. 使用二分查找来确定最大边长。
3. 对于每个可能的边长，检查是否存在标签相同的点。
4. 返回满足条件的最大边长对应的点数。

关键点:
- 使用二分查找来优化查找最大边长的过程。
- 使用集合来快速检查是否存在标签相同的点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 points 的长度。排序操作的时间复杂度为 O(n log n)，二分查找的时间复杂度为 O(log n)，每次检查的时间复杂度为 O(n)。
空间复杂度: O(n)，用于存储点和标签。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def max_points_inside_square(points: List[List[int]], s: str) -> int:
    def distance(point):
        return max(abs(point[0]), abs(point[1]))

    # 按距离原点的距离排序
    points = sorted(points, key=distance)

    def is_valid(length):
        seen = set()
        for i in range(len(points)):
            if distance(points[i]) > length:
                break
            if s[i] in seen:
                return False
            seen.add(s[i])
        return True

    left, right = 0, distance(points[-1])
    while left < right:
        mid = (left + right + 1) // 2
        if is_valid(mid):
            left = mid
        else:
            right = mid - 1

    # 计算最大边长下的点数
    seen = set()
    count = 0
    for i in range(len(points)):
        if distance(points[i]) > left:
            break
        if s[i] not in seen:
            seen.add(s[i])
            count += 1

    return count

Solution = create_solution(max_points_inside_square)