# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1733
标题: Maximum Number of Visible Points
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-visible-points/
题目类型: 几何、数组、数学、排序、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1610. 可见点的最大数目 - 给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，其中 location = [posx, posy] 且 points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。 最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，posx 和 posy 不能改变。你的视野范围的角度用 angle 表示， 这决定了你观测任意方向时可以多宽。设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。 对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。 同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。 返回你能看到的点的最大数目。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/04/89a07e9b-00ab-4967-976a-c723b2aa8656.png] 输入：points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1] 输出：3 解释：阴影区域代表你的视野。在你的视野中，所有的点都清晰可见，尽管 [2,2] 和 [3,3]在同一条直线上，你仍然可以看到 [3,3] 。 示例 2： 输入：points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1] 输出：4 解释：在你的视野中，所有的点都清晰可见，包括你所在位置的那个点。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/04/5010bfd3-86e6-465f-ac64-e9df941d2e49.png] 输入：points = [[1,0],[2,1]], angle = 13, location = [1,1] 输出：1 解释：如图所示，你只能看到两点之一。 提示： * 1 <= points.length <= 105 * points[i].length == 2 * location.length == 2 * 0 <= angle < 360 * 0 <= posx, posy, xi, yi <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将所有点相对于位置 location 的极角转换为弧度，并使用滑动窗口来找到最大可见点数。

算法步骤:
1. 计算每个点相对于位置 location 的极角，并将其转换为弧度。
2. 将所有点的弧度值存储在一个列表中，并将列表扩展为原来的两倍，以便处理跨越 360 度的情况。
3. 使用滑动窗口来找到在给定角度范围内的最大点数。

关键点:
- 使用 `math.atan2` 来计算极角。
- 将弧度值列表扩展为原来的两倍，以处理跨越 360 度的情况。
- 使用双指针或滑动窗口来找到最大可见点数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 points 的长度。主要的时间开销在于对弧度值进行排序。
空间复杂度: O(n)，用于存储弧度值和扩展后的弧度值列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import math

def max_visible_points(points: List[List[int]], angle: int, location: List[int]) -> int:
    def to_radians(point):
        dx, dy = point[0] - location[0], point[1] - location[1]
        return (math.atan2(dy, dx) + 2 * math.pi) % (2 * math.pi)

    angles = [to_radians(p) for p in points if p != location]
    same_location_count = len(points) - len(angles)
    
    angles.sort()
    angles += [a + 2 * math.pi for a in angles]
    
    max_count = 0
    left = 0
    for right in range(len(angles)):
        while angles[right] - angles[left] > math.radians(angle):
            left += 1
        max_count = max(max_count, right - left + 1)
    
    return max_count + same_location_count

Solution = create_solution(max_visible_points)