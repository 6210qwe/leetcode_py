# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 303
标题: Range Sum Query - Immutable
难度: easy
链接: https://leetcode.cn/problems/range-sum-query-immutable/
题目类型: 设计、数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
303. 区域和检索 - 数组不可变 - 给定一个整数数组 nums，处理以下类型的多个查询: 1. 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right 实现 NumArray 类： * NumArray(int[] nums) 使用数组 nums 初始化对象 * int sumRange(int left, int right) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] ) 示例 1： 输入： ["NumArray", "sumRange", "sumRange", "sumRange"] [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]] 输出： [null, 1, -1, -3] 解释： NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]); numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3) numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1)) 提示： * 1 <= nums.length <= 104 * -105 <= nums[i] <= 105 * 0 <= left <= right < nums.length * 最多调用 104 次 sumRange 方法
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和数组，preSum[i]表示前i个元素的和

算法步骤:
1. 初始化时计算前缀和数组
2. sumRange(left, right) = preSum[right+1] - preSum[left]

关键点:
- 使用前缀和实现O(1)查询
- 时间复杂度：初始化O(n)，查询O(1)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 初始化O(n)，查询O(1)
空间复杂度: O(n) - 前缀和数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


class NumArray:
    """
    区域和检索 - 数组不可变
    """
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)
    
    def sumRange(self, left: int, right: int) -> int:
        """返回[left, right]范围内的元素和"""
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


def range_sum_query_immutable(nums: List[int]) -> NumArray:
    """
    函数式接口 - 创建区域和检索对象
    
    实现思路:
    使用前缀和数组，preSum[i]表示前i个元素的和。
    
    Args:
        nums: 整数数组
        
    Returns:
        NumArray实例
        
    Example:
        >>> numArray = range_sum_query_immutable([-2, 0, 3, -5, 2, -1])
        >>> numArray.sumRange(0, 2)
        1
    """
    return NumArray(nums)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(range_sum_query_immutable)
