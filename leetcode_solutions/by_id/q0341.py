# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 341
标题: Flatten Nested List Iterator
难度: medium
链接: https://leetcode.cn/problems/flatten-nested-list-iterator/
题目类型: 栈、树、深度优先搜索、设计、队列、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
341. 扁平化嵌套列表迭代器 - 给你一个嵌套的整数列表 nestedList 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。 实现扁平迭代器类 NestedIterator ： * NestedIterator(List<NestedInteger> nestedList) 用嵌套列表 nestedList 初始化迭代器。 * int next() 返回嵌套列表的下一个整数。 * boolean hasNext() 如果仍然存在待迭代的整数，返回 true ；否则，返回 false 。 你的代码将会用下述伪代码检测： initialize iterator with nestedList res = [] while iterator.hasNext() append iterator.next() to the end of res return res 如果 res 与预期的扁平化列表匹配，那么你的代码将会被判为正确。 示例 1： 输入：nestedList = [[1,1],2,[1,1]] 输出：[1,1,2,1,1] 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。 示例 2： 输入：nestedList = [1,[4,[6]]] 输出：[1,4,6] 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。 提示： * 1 <= nestedList.length <= 500 * 嵌套列表中的整数值在范围 [-106, 106] 内
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈存储迭代器，递归展开嵌套列表

算法步骤:
1. 使用栈存储列表迭代器
2. hasNext时展开嵌套列表
3. next时返回整数

关键点:
- 栈存储迭代器
- 递归展开
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - next和hasNext平均O(1)
空间复杂度: O(d) - d为最大嵌套深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def nested_iterator_class(nested_list: List):
    """
    函数式接口 - 扁平化嵌套列表迭代器
    
    实现思路:
    使用栈存储迭代器，递归展开嵌套列表。
    
    Args:
        nested_list: 嵌套列表
        
    Returns:
        NestedIterator类
        
    Example:
        >>> it = nested_iterator_class([[1,1],2,[1,1]])
        >>> it.next()
        1
    """
    class NestedIterator:
        def __init__(self, nested_list: List):
            self.stack = [iter(nested_list)]
            self.next_val = None
        
        def next(self) -> int:
            return self.next_val
        
        def hasNext(self) -> bool:
            while self.stack:
                try:
                    item = next(self.stack[-1])
                    if isinstance(item, int):
                        self.next_val = item
                        return True
                    else:
                        self.stack.append(iter(item))
                except StopIteration:
                    self.stack.pop()
            return False
    
    return NestedIterator(nested_list)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(nested_iterator_class)
