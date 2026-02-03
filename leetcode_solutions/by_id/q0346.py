# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 346
标题: Moving Average from Data Stream
难度: easy
链接: https://leetcode.cn/problems/moving-average-from-data-stream/
题目类型: 设计、队列、数组、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
346. 数据流中的移动平均值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用队列维护窗口，维护窗口和

算法步骤:
1. 使用队列存储窗口内的数字
2. 维护窗口和sum
3. 当队列长度>size时，移除队首并更新sum

关键点:
- 队列
- 维护窗口和
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - next操作O(1)
空间复杂度: O(size) - 队列空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def moving_average_class(size: int):
    """
    函数式接口 - 数据流中的移动平均值
    
    实现思路:
    使用队列维护窗口，维护窗口和。
    
    Args:
        size: 窗口大小
        
    Returns:
        MovingAverage类
        
    Example:
        >>> ma = moving_average_class(3)
        >>> ma.next(1)
        1.0
    """
    class MovingAverage:
        def __init__(self, size: int):
            self.size = size
            self.queue = deque()
            self.sum = 0
        
        def next(self, val: int) -> float:
            self.queue.append(val)
            self.sum += val
            
            if len(self.queue) > self.size:
                self.sum -= self.queue.popleft()
            
            return self.sum / len(self.queue)
    
    return MovingAverage(size)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(moving_average_class)
