# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 251
标题: Flatten 2D Vector
难度: medium
链接: https://leetcode.cn/problems/flatten-2d-vector/
题目类型: 设计、数组、双指针、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
251. 展开二维向量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个指针，外层指针指向行，内层指针指向列

算法步骤:
1. 维护行索引和列索引
2. 跳过空行
3. 实现next和hasNext方法

关键点:
- 双指针遍历
- 跳过空行
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - next和hasNext都是O(1)
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def vector_2d(vec: List[List[int]]):
    """
    函数式接口 - 展开二维向量
    
    实现思路:
    使用两个指针遍历二维向量。
    
    Args:
        vec: 二维向量
        
    Returns:
        Vector2D类
        
    Example:
        >>> v = vector_2d([[1,2],[3],[4]])
        >>> v.next()
        1
    """
    class Vector2D:
        def __init__(self, vec: List[List[int]]):
            self.vec = vec
            self.row = 0
            self.col = 0
            self._skip_empty_rows()
        
        def _skip_empty_rows(self):
            """跳过空行"""
            while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
                self.row += 1
                self.col = 0
        
        def next(self) -> int:
            """返回下一个元素"""
            if not self.hasNext():
                return None
            val = self.vec[self.row][self.col]
            self.col += 1
            self._skip_empty_rows()
            return val
        
        def hasNext(self) -> bool:
            """判断是否还有下一个元素"""
            return self.row < len(self.vec)
    
    return Vector2D(vec)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(vector_2d)
