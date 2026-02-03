# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 284
标题: Peeking Iterator
难度: medium
链接: https://leetcode.cn/problems/peeking-iterator/
题目类型: 设计、数组、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
284. 窥视迭代器 - 请你在设计一个迭代器，在集成现有迭代器拥有的 hasNext 和 next 操作的基础上，还额外支持 peek 操作。 实现 PeekingIterator 类： * PeekingIterator(Iterator<int> nums) 使用指定整数迭代器 nums 初始化迭代器。 * int next() 返回数组中的下一个元素，并将指针移动到下个元素处。 * bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。 * int peek() 返回数组中的下一个元素，但 不 移动指针。 注意：每种语言可能有不同的构造函数和迭代器 Iterator，但均支持 int next() 和 boolean hasNext() 函数。 示例 1： 输入： ["PeekingIterator", "next", "peek", "next", "next", "hasNext"] [[[1, 2, 3]], [], [], [], [], []] 输出： [null, 1, 2, 2, 3, false] 解释： PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3] peekingIterator.next(); // 返回 1 ，指针移动到下一个元素 [1,2,3] peekingIterator.peek(); // 返回 2 ，指针未发生移动 [1,2,3] peekingIterator.next(); // 返回 2 ，指针移动到下一个元素 [1,2,3] peekingIterator.next(); // 返回 3 ，指针移动到下一个元素 [1,2,3] peekingIterator.hasNext(); // 返回 False 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 1000 * 对 next 和 peek 的调用均有效 * next、hasNext 和 peek 最多调用 1000 次 进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 缓存下一个元素，peek时返回缓存值

算法步骤:
1. 维护一个next_val缓存下一个元素
2. peek时返回next_val
3. next时返回next_val并更新缓存

关键点:
- 缓存下一个元素
- 时间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作都是O(1)
空间复杂度: O(1) - 只缓存一个元素
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def peeking_iterator_class(iterator):
    """
    函数式接口 - 窥视迭代器
    
    实现思路:
    缓存下一个元素，peek时返回缓存值。
    
    Args:
        iterator: 原始迭代器
        
    Returns:
        PeekingIterator类
        
    Example:
        >>> # 示例用法
    """
    class PeekingIterator:
        def __init__(self, iterator):
            self.iterator = iterator
            self.next_val = None
            if self.iterator.hasNext():
                self.next_val = self.iterator.next()
        
        def peek(self) -> int:
            return self.next_val
        
        def next(self) -> int:
            val = self.next_val
            self.next_val = self.iterator.next() if self.iterator.hasNext() else None
            return val
        
        def hasNext(self) -> bool:
            return self.next_val is not None
    
    return PeekingIterator(iterator)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(peeking_iterator_class)
