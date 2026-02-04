```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1713
标题: Dot Product of Two Sparse Vectors
难度: medium
链接: https://leetcode.cn/problems/dot-product-of-two-sparse-vectors/
题目类型: 设计、数组、哈希表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1570. 两个稀疏向量的点积 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储非零元素的索引和值，然后通过双指针计算点积。

算法步骤:
1. 初始化时，使用哈希表存储非零元素的索引和值。
2. 计算点积时，使用双指针遍历两个哈希表，找到相同的索引并计算乘积。

关键点:
- 使用哈希表存储非零元素可以减少空间复杂度。
- 双指针可以高效地计算点积。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是两个稀疏向量的非零元素个数。
空间复杂度: O(n + m)，用于存储非零元素的哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzeros[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i, j = 0, 0
        keys1, keys2 = list(self.nonzeros.keys()), list(vec.nonzeros.keys())
        
        while i < len(keys1) and j < len(keys2):
            if keys1[i] == keys2[j]:
                result += self.nonzeros[keys1[i]] * vec.nonzeros[keys2[j]]
                i += 1
                j += 1
            elif keys1[i] < keys2[j]:
                i += 1
            else:
                j += 1
        
        return result


# 示例用法
if __name__ == "__main__":
    # 创建两个稀疏向量
    v1 = SparseVector([1, 0, 0, 2, 3])
    v2 = SparseVector([0, 3, 0, 4, 0])
    
    # 计算点积
    print(v1.dotProduct(v2))  # 输出: 8
```

这个实现中，`SparseVector` 类使用哈希表存储非零元素的索引和值，并通过双指针方法计算两个稀疏向量的点积。这样可以确保时间和空间复杂度最优。