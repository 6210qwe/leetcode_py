# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 307
标题: Range Sum Query - Mutable
难度: medium
链接: https://leetcode.cn/problems/range-sum-query-mutable/
题目类型: 设计、树状数组、线段树、数组、分治
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
307. 区域和检索 - 数组可修改 - 给你一个数组 nums ，请你完成两类查询。 1. 其中一类查询要求 更新 数组 nums 下标对应的值 2. 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right 实现 NumArray 类： * NumArray(int[] nums) 用整数数组 nums 初始化对象 * void update(int index, int val) 将 nums[index] 的值 更新 为 val * int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]） 示例 1： 输入： ["NumArray", "sumRange", "update", "sumRange"] [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]] 输出： [null, 9, null, 8] 解释： NumArray numArray = new NumArray([1, 3, 5]); numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9 numArray.update(1, 2); // nums = [1,2,5] numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8 提示： * 1 <= nums.length <= 3 * 104 * -100 <= nums[i] <= 100 * 0 <= index < nums.length * -100 <= val <= 100 * 0 <= left <= right < nums.length * 调用 update 和 sumRange 方法次数不大于 3 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组（Binary Indexed Tree）或线段树实现区间和查询和单点更新

算法步骤:
1. 使用树状数组维护前缀和
2. update: 更新树状数组
3. sumRange: 使用前缀和相减计算区间和

关键点:
- 使用树状数组实现O(logn)更新和查询
- 时间复杂度：初始化O(n)，更新和查询O(logn)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 初始化O(n)，更新和查询O(logn)
空间复杂度: O(n) - 树状数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


class NumArray:
    """
    区域和检索 - 数组可修改（使用树状数组）
    """
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (self.n + 1)
        
        # 初始化树状数组
        for i in range(self.n):
            self._update(i, nums[i])
    
    def _lowbit(self, x: int) -> int:
        """返回x的二进制表示中最低位的1所对应的值"""
        return x & -x
    
    def _update(self, index: int, delta: int):
        """更新树状数组"""
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += self._lowbit(i)
    
    def _query(self, index: int) -> int:
        """查询前缀和[0, index]"""
        i = index + 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= self._lowbit(i)
        return total
    
    def update(self, index: int, val: int) -> None:
        """更新数组元素"""
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update(index, delta)
    
    def sumRange(self, left: int, right: int) -> int:
        """返回[left, right]范围内的元素和"""
        return self._query(right) - self._query(left - 1)


def range_sum_query_mutable(nums: List[int]) -> NumArray:
    """
    函数式接口 - 创建区域和检索对象（可修改）
    
    实现思路:
    使用树状数组（Binary Indexed Tree）实现区间和查询和单点更新。
    
    Args:
        nums: 整数数组
        
    Returns:
        NumArray实例
        
    Example:
        >>> numArray = range_sum_query_mutable([1, 3, 5])
        >>> numArray.sumRange(0, 2)
        9
    """
    return NumArray(nums)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(range_sum_query_mutable)
