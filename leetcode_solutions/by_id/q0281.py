# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 281
标题: Zigzag Iterator
难度: medium
链接: https://leetcode.cn/problems/zigzag-iterator/
题目类型: 设计、队列、数组、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
281. 锯齿迭代器 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用队列存储迭代器，轮流取元素

算法步骤:
1. 将两个列表的迭代器加入队列
2. 每次从队列头部取迭代器，取一个元素
3. 如果迭代器还有元素，放回队列尾部

关键点:
- 队列管理迭代器
- 时间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - next和hasNext都是O(1)
空间复杂度: O(k) - k为列表数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def zigzag_iterator_class(v1: List[int], v2: List[int]):
    """
    函数式接口 - 锯齿迭代器
    
    实现思路:
    使用队列存储迭代器，轮流取元素。
    
    Args:
        v1: 第一个列表
        v2: 第二个列表
        
    Returns:
        ZigzagIterator类
        
    Example:
        >>> it = zigzag_iterator_class([1,2], [3,4,5,6])
        >>> it.next()
        1
    """
    class ZigzagIterator:
        def __init__(self, v1: List[int], v2: List[int]):
            self.queue = deque()
            if v1:
                self.queue.append(iter(v1))
            if v2:
                self.queue.append(iter(v2))
        
        def next(self) -> int:
            iterator = self.queue.popleft()
            val = next(iterator)
            # 如果迭代器还有元素，放回队列
            try:
                self.queue.append(iterator)
            except StopIteration:
                pass
            return val
        
        def hasNext(self) -> bool:
            return len(self.queue) > 0
    
    return ZigzagIterator(v1, v2)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(zigzag_iterator_class)
