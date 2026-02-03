# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 218
标题: The Skyline Problem
难度: hard
链接: https://leetcode.cn/problems/the-skyline-problem/
题目类型: 树状数组、线段树、数组、分治、有序集合、排序、扫描线、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
218. 天际线问题 - 城市的 天际线 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 由这些建筑物形成的 天际线 。 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示： * lefti 是第 i 座建筑物左边缘的 x 坐标。 * righti 是第 i 座建筑物右边缘的 x 坐标。 * heighti 是第 i 座建筑物的高度。 你可以假设所有的建筑都是完美的长方形，在高度为 0 的绝对平坦的表面上。 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...] 示例 1： [https://assets.leetcode.com/uploads/2020/12/01/merged.jpg] 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]] 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]] 解释： 图 A 显示输入的所有建筑物的位置和高度， 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。 示例 2： 输入：buildings = [[0,2,3],[2,5,3]] 输出：[[0,3],[5,0]] 提示： * 1 <= buildings.length <= 104 * 0 <= lefti < righti <= 231 - 1 * 1 <= heighti <= 231 - 1 * buildings 按 lefti 非递减排序
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 扫描线算法，将建筑物转换为事件点，使用优先队列维护当前最大高度

算法步骤:
1. 将每个建筑物转换为两个事件：(left, height, start)和(right, height, end)
2. 按x坐标排序事件点
3. 使用优先队列（最大堆）维护当前所有建筑物的高度
4. 遍历事件点，当高度变化时，添加关键点

关键点:
- 使用扫描线算法和优先队列
- 时间复杂度O(n log n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序和堆操作
空间复杂度: O(n) - 事件点和堆的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq
from leetcode_solutions.utils.solution import create_solution


def the_skyline_problem(buildings: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 天际线问题
    
    实现思路:
    扫描线算法，将建筑物转换为事件点，使用优先队列维护当前最大高度。
    
    Args:
        buildings: 建筑物列表，每个元素为[left, right, height]
        
    Returns:
        天际线关键点列表
        
    Example:
        >>> the_skyline_problem([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
        [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    """
    events = []
    for left, right, height in buildings:
        events.append((left, height, 'start'))
        events.append((right, height, 'end'))
    
    # 按x坐标排序，相同x坐标时，start事件优先，且高度高的优先
    events.sort(key=lambda x: (x[0], x[2] == 'start', -x[1] if x[2] == 'start' else x[1]))
    
    result = []
    # 使用最大堆存储当前所有建筑物的高度，用负数实现最大堆
    heap = [0]  # 初始高度为0
    removed = {}  # 记录已移除但还在堆中的高度
    
    for x, height, event_type in events:
        if event_type == 'start':
            if height > -heap[0]:
                result.append([x, height])
            heapq.heappush(heap, -height)
        else:  # end
            removed[height] = removed.get(height, 0) + 1
            # 移除堆顶已删除的高度
            while heap and removed.get(-heap[0], 0) > 0:
                removed[-heap[0]] -= 1
                if removed[-heap[0]] == 0:
                    del removed[-heap[0]]
                heapq.heappop(heap)
            
            current_max = -heap[0] if heap else 0
            if not result or result[-1][1] != current_max:
                result.append([x, current_max])
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(the_skyline_problem)
