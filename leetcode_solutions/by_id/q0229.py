# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 229
标题: Majority Element II
难度: medium
链接: https://leetcode.cn/problems/majority-element-ii/
题目类型: 数组、哈希表、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
229. 多数元素 II - 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。 示例 1： 输入：nums = [3,2,3] 输出：[3] 示例 2： 输入：nums = [1] 输出：[1] 示例 3： 输入：nums = [1,2] 输出：[1,2] 提示： * 1 <= nums.length <= 5 * 104 * -109 <= nums[i] <= 109 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用Boyer-Moore投票算法，最多有两个候选元素

算法步骤:
1. 使用两个候选元素和两个计数器
2. 遍历数组，更新候选元素和计数器
3. 再次遍历数组，验证候选元素是否满足条件

关键点:
- 使用Boyer-Moore投票算法
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历数组两次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def majority_element_ii(nums: List[int]) -> List[int]:
    """
    函数式接口 - 多数元素II
    
    实现思路:
    使用Boyer-Moore投票算法，最多有两个候选元素。
    
    Args:
        nums: 整数数组
        
    Returns:
        所有出现超过⌊n/3⌋次的元素列表
        
    Example:
        >>> majority_element_ii([3, 2, 3])
        [3]
    """
    if not nums:
        return []
    
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    
    # 第一遍遍历，找出两个候选元素
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    # 第二遍遍历，验证候选元素
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    result = []
    n = len(nums)
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(majority_element_ii)
