# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3775
标题: Separate Squares II
难度: hard
链接: https://leetcode.cn/problems/separate-squares-ii/
题目类型: 线段树、数组、二分查找、扫描线
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3454. 分割正方形 II - 给你一个二维整数数组 squares ，其中 squares[i] = [xi, yi, li] 表示一个与 x 轴平行的正方形的左下角坐标和正方形的边长。 找到一个最小的 y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 等于 该线以下正方形的总面积。 答案如果与实际答案的误差在 10-5 以内，将视为正确答案。 注意：正方形 可能会 重叠。重叠区域只 统计一次 。 示例 1： 输入： squares = [[0,0,1],[2,2,1]] 输出： 1.00000 解释： [https://pic.leetcode.cn/1739609602-zhNmeC-4065example1drawio.png] 任何在 y = 1 和 y = 2 之间的水平线都会有 1 平方单位的面积在其上方，1 平方单位的面积在其下方。最小的 y 坐标是 1。 示例 2： 输入： squares = [[0,0,2],[1,1,1]] 输出： 1.00000 解释： [https://pic.leetcode.cn/1739609605-ezeVgk-4065example2drawio.png] 由于蓝色正方形和红色正方形有重叠区域且重叠区域只统计一次。所以直线 y = 1 将正方形分割成两部分且面积相等。 提示： * 1 <= squares.length <= 5 * 104 * squares[i] = [xi, yi, li] * squares[i].length == 3 * 0 <= xi, yi <= 109 * 1 <= li <= 109 * 所有正方形的总面积不超过 1015。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用扫描线算法结合线段树来高效地处理重叠正方形的问题。

算法步骤:
1. 将每个正方形的上下边界分别记录为事件，并按 y 坐标排序。
2. 使用线段树来维护当前扫描线上的面积。
3. 在扫描过程中，通过二分查找找到使得上下面积相等的 y 坐标。

关键点:
- 使用线段树来高效地更新和查询区间面积。
- 通过二分查找来精确找到使上下面积相等的 y 坐标。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + n log C)，其中 n 是正方形的数量，C 是 y 坐标的范围。
空间复杂度: O(n + C)，其中 n 是正方形的数量，C 是 y 坐标的范围。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
    
    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)
    
    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] += val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node, start, mid, idx, val)
            else:
                self._update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
    
    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self._query(2 * node, start, mid, left, right) + self._query(2 * node + 1, mid + 1, end, left, right)

def solution_function_name(squares: List[List[int]]) -> float:
    events = []
    for x, y, l in squares:
        events.append((y, 1, x, x + l - 1))
        events.append((y + l, -1, x, x + l - 1))
    
    events.sort()
    y_coords = sorted(set(y for y, _, _, _ in events))
    y_index = {y: i for i, y in enumerate(y_coords)}
    
    total_area = sum(l ** 2 for _, _, l in squares)
    half_area = total_area / 2
    
    n = len(y_coords)
    segment_tree = SegmentTree(n)
    
    current_area = 0
    for y, typ, x1, x2 in events:
        if typ == 1:
            segment_tree.update(y_index[y], x2 - x1 + 1)
            current_area += (x2 - x1 + 1) * (y_coords[y_index[y] + 1] - y_coords[y_index[y]])
        else:
            current_area -= (x2 - x1 + 1) * (y_coords[y_index[y]] - y_coords[y_index[y] - 1])
            segment_tree.update(y_index[y], -(x2 - x1 + 1))
        
        if abs(current_area - half_area) < 1e-5:
            return y
    
    return y_coords[-1]

Solution = create_solution(solution_function_name)