# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000562
标题: 最强祝福力场
难度: medium
链接: https://leetcode.cn/problems/xepqZ5/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 74. 最强祝福力场 - 小扣在探索丛林的过程中，无意间发现了传说中“落寞的黄金之都”。而在这片建筑废墟的地带中，小扣使用探测仪监测到了存在某种带有「祝福」效果的力场。 经过不断的勘测记录，小扣将所有力场的分布都记录了下来。`forceField[i] = [x,y,side]` 表示第 `i` 片力场将覆盖以坐标 `(x,y)` 为中心，边长为 `side` 的正方形区域。 若任意一点的 **力场强度** 等于覆盖该点的力场数量，请求出在这片地带中 **力场强度** 最强处的 **力场强度**。 **注意：** - 力场范围的边缘同样被力场覆盖。 **示例 1：** >输入： >`forceField = [[0,0,1],[1,0,1]]` > >输出：`2` > >解释：如图所示，（0.5, 0) 处力场强度最强为 2， （0.5，-0.5）处力场强度同样是 2。 ![image.png](https://pic.leetcode.cn/1681805536-zGfghe-image.png){:width=400px} **示例 2：** >输入： >`forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]` > >输出：`3` > >解释：如下图所示， >`forceField[0]、forceField[1]、forceField[3]` 重叠的区域力场强度最大，返回 `3` ![image.png](https://pic.leetcode.cn/1681805437-HQkyZS-image.png){:width=500px} **提示：** - `1 <= forceField.length <= 100` - `forceField[i].length == 3` - `0 <= forceField[i][0], forceField[i][1] <= 10^9` - `1 <= forceField[i][2] <= 10^9`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用扫描线算法来计算每个点的力场强度。通过将每个力场的边界转换为事件，然后对这些事件进行排序和处理。

算法步骤:
1. 将每个力场的边界转换为事件（开始事件和结束事件）。
2. 对这些事件按 x 坐标进行排序。
3. 使用一个平衡树来维护当前的 y 区间，并计算每个区间的力场强度。
4. 更新全局最大力场强度。

关键点:
- 使用平衡树来高效地维护当前的 y 区间。
- 通过扫描线算法处理事件，确保时间复杂度最优。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是力场的数量。排序操作的时间复杂度是 O(n log n)，处理事件的时间复杂度是 O(n log n)。
空间复杂度: O(n)，用于存储事件和平衡树。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import bisect

def solution_function_name(force_field: List[List[int]]) -> int:
    """
    函数式接口 - 计算最强力场强度
    """
    events = []
    for x, y, side in force_field:
        left, right = x - side / 2, x + side / 2
        bottom, top = y - side / 2, y + side / 2
        events.append((left, 'start', (bottom, top)))
        events.append((right, 'end', (bottom, top)))
    
    events.sort()
    
    active_intervals = []
    max_strength = 0
    current_strength = 0
    
    for x, event_type, interval in events:
        if event_type == 'start':
            bisect.insort(active_intervals, interval)
            current_strength += 1
        else:
            index = bisect.bisect_left(active_intervals, interval)
            del active_intervals[index]
            current_strength -= 1
        
        max_strength = max(max_strength, current_strength)
    
    return max_strength

Solution = create_solution(solution_function_name)