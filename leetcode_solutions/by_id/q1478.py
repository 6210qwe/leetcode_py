# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1478
标题: Maximum Number of Events That Can Be Attended
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/
题目类型: 贪心、数组、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1353. 最多可以参加的会议数目 - 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。 你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。在任意一天 d 中只能参加一场会议。 请你返回你可以参加的 最大 会议数目。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/16/e1.png] 输入：events = [[1,2],[2,3],[3,4]] 输出：3 解释：你可以参加所有的三个会议。 安排会议的一种方案如上图。 第 1 天参加第一个会议。 第 2 天参加第二个会议。 第 3 天参加第三个会议。 示例 2： 输入：events= [[1,2],[2,3],[3,4],[1,2]] 输出：4 提示： * 1 <= events.length <= 105 * events[i].length == 2 * 1 <= startDayi <= endDayi <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和最小堆来选择最早结束且当前可参加的会议。

算法步骤:
1. 将所有会议按开始时间排序。
2. 使用一个最小堆来存储当前可参加的会议，并按结束时间排序。
3. 遍历每一天，将当天开始的所有会议加入堆中。
4. 从堆中取出最早结束的会议并参加，然后移除已经结束的会议。
5. 重复上述步骤直到所有天数遍历完毕。

关键点:
- 按开始时间排序确保我们总是处理最早开始的会议。
- 使用最小堆确保我们总是选择最早结束的会议。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 events 的长度。排序操作的时间复杂度为 O(n log n)，而每次插入和删除堆的操作时间复杂度为 O(log n)。
空间复杂度: O(n)，最坏情况下堆中可能包含所有会议。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def maxEvents(events: List[List[int]]) -> int:
    """
    函数式接口 - 返回可以参加的最大会议数目
    """
    # 按开始时间排序
    events.sort()
    
    # 初始化堆和结果计数器
    min_heap = []
    event_index = 0
    attended_events = 0
    current_day = 0
    
    while min_heap or event_index < len(events):
        # 如果当前堆为空，直接跳到下一个会议的开始时间
        if not min_heap:
            current_day = events[event_index][0]
        
        # 将所有开始时间为 current_day 的会议加入堆中
        while event_index < len(events) and events[event_index][0] == current_day:
            heapq.heappush(min_heap, events[event_index][1])
            event_index += 1
        
        # 从堆中取出最早结束的会议
        heapq.heappop(min_heap)
        attended_events += 1
        current_day += 1
        
        # 移除已经结束的会议
        while min_heap and min_heap[0] < current_day:
            heapq.heappop(min_heap)
    
    return attended_events

Solution = create_solution(maxEvents)