# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3478
标题: Check if the Rectangle Corner Is Reachable
难度: hard
链接: https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/
题目类型: 深度优先搜索、广度优先搜索、并查集、几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3235. 判断矩形的两个角落是否可达 - 给你两个正整数 xCorner 和 yCorner 和一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示一个圆心在 (xi, yi) 半径为 ri 的圆。 坐标平面内有一个左下角在原点，右上角在 (xCorner, yCorner) 的矩形。你需要判断是否存在一条从左下角到右上角的路径满足：路径 完全 在矩形内部，不会 触碰或者经过 任何 圆的内部和边界，同时 只 在起点和终点接触到矩形。 如果存在这样的路径，请你返回 true ，否则返回 false 。 示例 1： 输入：X = 3, Y = 4, circles = [[2,1,1]] 输出：true 解释： [https://assets.leetcode.com/uploads/2024/05/18/example2circle1.png] 黑色曲线表示一条从 (0, 0) 到 (3, 4) 的路径。 示例 2： 输入：X = 3, Y = 3, circles = [[1,1,2]] 输出：false 解释： [https://assets.leetcode.com/uploads/2024/05/18/example1circle.png] 不存在从 (0, 0) 到 (3, 3) 的路径。 示例 3： 输入：X = 3, Y = 3, circles = [[2,1,1],[1,2,1]] 输出：false 解释： [https://assets.leetcode.com/uploads/2024/05/18/example0circle.png] 不存在从 (0, 0) 到 (3, 3) 的路径。 示例 4： 输入：X = 4, Y = 4, circles = [[5,5,1]] 输出：true 解释： [https://assets.leetcode.com/uploads/2024/08/04/rectangles.png] 提示： * 3 <= xCorner, yCorner <= 109 * 1 <= circles.length <= 1000 * circles[i].length == 3 * 1 <= xi, yi, ri <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用几何方法判断路径是否被圆阻挡

算法步骤:
1. 检查每个圆是否阻挡了从 (0, 0) 到 (xCorner, yCorner) 的直线路径。
2. 如果所有圆都不阻挡路径，则返回 True；否则返回 False。

关键点:
- 计算圆心到直线的距离，如果距离小于等于半径，则认为圆阻挡了路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 circles 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def is_rectangle_corner_reachable(xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
    """
    判断矩形的两个角落是否可达
    """
    for circle in circles:
        x, y, r = circle
        # 计算圆心到直线 (0, 0) 到 (xCorner, yCorner) 的距离
        distance = abs(x * yCorner - y * xCorner) / (xCorner ** 2 + yCorner ** 2) ** 0.5
        # 如果距离小于等于半径，则圆阻挡了路径
        if distance <= r:
            return False
    return True

Solution = create_solution(is_rectangle_corner_reachable)