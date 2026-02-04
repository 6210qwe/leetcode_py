# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 683
标题: K Empty Slots
难度: hard
链接: https://leetcode.cn/problems/k-empty-slots/
题目类型: 树状数组、线段树、队列、数组、有序集合、滑动窗口、单调队列、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
683. K 个关闭的灯泡 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调队列来维护一个滑动窗口，找到满足条件的天数。

算法步骤:
1. 初始化一个单调队列 `deque` 和一个字典 `day_of_bulb` 来记录每个灯泡点亮的天数。
2. 遍历 `bulbs` 数组，将每个灯泡点亮的天数记录在 `day_of_bulb` 中。
3. 使用单调队列 `deque` 来维护一个滑动窗口，窗口内的灯泡编号是递增的。
4. 对于每个灯泡，检查其与队列中的灯泡是否满足条件：
   - 如果当前灯泡编号与队列头部灯泡编号之差为 `k+1`，且这两个灯泡之间的所有灯泡都比它们晚点亮，则更新答案。
   - 如果当前灯泡编号与队列尾部灯泡编号之差为 `k+1`，且这两个灯泡之间的所有灯泡都比它们晚点亮，则更新答案。
5. 更新单调队列，确保队列中的灯泡编号是递增的，并且满足条件。

关键点:
- 使用单调队列来维护滑动窗口，确保窗口内的灯泡编号是递增的。
- 通过比较灯泡点亮的天数来判断是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def kEmptySlots(bulbs: List[int], k: int) -> int:
    """
    函数式接口 - 找到第一个满足条件的天数
    """
    n = len(bulbs)
    day_of_bulb = [0] * (n + 1)
    for day, bulb in enumerate(bulbs):
        day_of_bulb[bulb] = day
    
    deque = []
    min_day = float('inf')
    
    for i in range(1, n + 1):
        while deque and day_of_bulb[deque[-1]] > day_of_bulb[i]:
            deque.pop()
        
        if deque and i - deque[-1] == k + 1:
            min_day = min(min_day, max(day_of_bulb[deque[-1]], day_of_bulb[i]) + 1)
        
        deque.append(i)
    
    deque.clear()
    
    for i in range(n, 0, -1):
        while deque and day_of_bulb[deque[-1]] > day_of_bulb[i]:
            deque.pop()
        
        if deque and deque[-1] - i == k + 1:
            min_day = min(min_day, max(day_of_bulb[deque[-1]], day_of_bulb[i]) + 1)
        
        deque.append(i)
    
    return min_day if min_day < float('inf') else -1


Solution = create_solution(kEmptySlots)