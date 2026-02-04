# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1003
标题: Minimum Area Rectangle II
难度: medium
链接: https://leetcode.cn/problems/minimum-area-rectangle-ii/
题目类型: 几何、数组、哈希表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
963. 最小面积矩形 II - 给你一个 X-Y 平面上的点数组 points，其中 points[i] = [xi, yi]。 返回由这些点形成的任意矩形的最小面积，矩形的边 不一定 平行于 X 轴和 Y 轴。如果不存在这样的矩形，则返回 0。 答案只需在10-5 的误差范围内即可被视作正确答案。 示例 1： [https://assets.leetcode.com/uploads/2018/12/21/1a.png] 输入： points = [[1,2],[2,1],[1,0],[0,1]] 输出： 2.00000 解释： 最小面积矩形由 [1,2]、[2,1]、[1,0]、[0,1] 组成，其面积为 2。 示例 2： [https://assets.leetcode.com/uploads/2018/12/22/2.png] 输入： points = [[0,1],[2,1],[1,1],[1,0],[2,0]] 输出： 1.00000 解释： 最小面积矩形由 [1,0]、[1,1]、[2,1]、[2,0] 组成，其面积为 1。 示例 3： [https://assets.leetcode.com/uploads/2018/12/22/3.png] 输入： points = [[0,3],[1,2],[3,1],[1,3],[2,1]] 输出： 0 解释： 无法由这些点组成任何矩形。 提示： * 1 <= points.length <= 50 * points[i].length == 2 * 0 <= xi, yi <= 4 * 104 * 所有给定的点都是 唯一 的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个中点到两个端点的映射，通过遍历所有可能的对角线来找到最小面积矩形。

算法步骤:
1. 将所有点转换为复数形式，方便计算中点。
2. 使用哈希表存储每个中点到两个端点的映射。
3. 遍历所有可能的对角线，检查是否存在对应的另一条对角线，计算面积并更新最小面积。

关键点:
- 使用复数表示点，方便计算中点。
- 通过哈希表快速查找中点对应的端点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 points 的长度。
空间复杂度: O(n^2)，哈希表的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_area_free_rect(points: List[List[int]]) -> float:
    """
    函数式接口 - 计算由给定点形成的最小面积矩形
    """
    # 将点转换为复数形式
    points = [complex(*point) for point in points]
    seen = {}
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            center = (p1 + p2) / 2
            radius = abs(center - p1)
            
            if (center, radius) not in seen:
                seen[(center, radius)] = []
            seen[(center, radius)].append((p1, p2))
    
    min_area = float('inf')
    
    for (center, radius), pairs in seen.items():
        for (p1, p2) in pairs:
            for (q1, q2) in pairs:
                if p1 != q1 and p1 != q2 and p2 != q1 and p2 != q2:
                    area = abs((p1 - q1) * (p2 - q1).conjugate())
                    if area > 0:
                        min_area = min(min_area, area)
    
    return min_area if min_area < float('inf') else 0.0


Solution = create_solution(min_area_free_rect)