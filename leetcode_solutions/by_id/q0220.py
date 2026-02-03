# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 220
标题: Contains Duplicate III
难度: hard
链接: https://leetcode.cn/problems/contains-duplicate-iii/
题目类型: 数组、桶排序、有序集合、排序、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
220. 存在重复元素 III - 给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。 找出满足下述条件的下标对 (i, j)： * i != j, * abs(i - j) <= indexDiff * abs(nums[i] - nums[j]) <= valueDiff 如果存在，返回 true ；否则，返回 false 。 示例 1： 输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0 输出：true 解释：可以找出 (i, j) = (0, 3) 。 满足下述 3 个条件： i != j --> 0 != 3 abs(i - j) <= indexDiff --> abs(0 - 3) <= 3 abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0 示例 2： 输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3 输出：false 解释：尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 。 提示： * 2 <= nums.length <= 105 * -109 <= nums[i] <= 109 * 1 <= indexDiff <= nums.length * 0 <= valueDiff <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用桶排序思想，将元素映射到桶中，每个桶大小为valueDiff+1

算法步骤:
1. 使用滑动窗口维护索引差<=indexDiff的元素
2. 将元素值映射到桶中，桶大小为valueDiff+1
3. 检查当前元素所在桶或相邻桶是否有元素
4. 如果找到满足条件的元素，返回True

关键点:
- 使用桶排序思想
- 时间复杂度O(n)，空间复杂度O(min(n, indexDiff))
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历数组一次
空间复杂度: O(min(n, indexDiff)) - 桶的数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def contains_duplicate_iii(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    """
    函数式接口 - 存在重复元素III
    
    实现思路:
    使用桶排序思想，将元素映射到桶中，每个桶大小为valueDiff+1。
    
    Args:
        nums: 整数数组
        indexDiff: 索引差的最大值
        valueDiff: 值差的最大值
        
    Returns:
        如果存在满足条件的下标对返回True，否则返回False
        
    Example:
        >>> contains_duplicate_iii([1, 2, 3, 1], 3, 0)
        True
    """
    if valueDiff < 0:
        return False
    
    bucket = {}
    bucket_size = valueDiff + 1
    
    for i, num in enumerate(nums):
        bucket_id = num // bucket_size
        
        # 检查当前桶
        if bucket_id in bucket:
            return True
        
        # 检查相邻桶
        if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff:
            return True
        if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff:
            return True
        
        bucket[bucket_id] = num
        
        # 维护滑动窗口
        if i >= indexDiff:
            old_bucket_id = nums[i - indexDiff] // bucket_size
            del bucket[old_bucket_id]
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(contains_duplicate_iii)
