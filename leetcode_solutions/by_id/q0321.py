# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 321
标题: Create Maximum Number
难度: hard
链接: https://leetcode.cn/problems/create-maximum-number/
题目类型: 栈、贪心、数组、双指针、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
321. 拼接最大数 - 给你两个整数数组 nums1 和 nums2，它们的长度分别为 m 和 n。数组 nums1 和 nums2 分别代表两个数各位上的数字。同时你也会得到一个整数 k。 请你利用这两个数组中的数字创建一个长度为 k <= m + n 的最大数。同一数组中数字的相对顺序必须保持不变。 返回代表答案的长度为 k 的数组。 示例 1： 输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5 输出：[9,8,6,5,3] 示例 2： 输入：nums1 = [6,7], nums2 = [6,0,4], k = 5 输出：[6,7,6,0,4] 示例 3： 输入：nums1 = [3,9], nums2 = [8,9], k = 3 输出：[9,8,9] 提示： * m == nums1.length * n == nums2.length * 1 <= m, n <= 500 * 0 <= nums1[i], nums2[i] <= 9 * 1 <= k <= m + n * nums1 和 nums2 没有前导 0。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 枚举从两个数组中选择的数量，分别找最大子序列，然后合并

算法步骤:
1. 枚举从nums1选i个，从nums2选k-i个
2. 分别用单调栈找最大子序列
3. 合并两个子序列
4. 比较所有合并结果，找最大值

关键点:
- 单调栈
- 合并两个数组
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k*(m+n)) - m和n为数组长度
空间复杂度: O(k) - 结果数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_number(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    """
    函数式接口 - 拼接最大数
    
    实现思路:
    枚举从两个数组中选择的数量，分别找最大子序列，然后合并。
    
    Args:
        nums1: 第一个数组
        nums2: 第二个数组
        k: 目标长度
        
    Returns:
        最大数数组
        
    Example:
        >>> max_number([3,4,6,5], [9,1,2,5,8,3], 5)
        [9, 8, 6, 5, 3]
    """
    def get_max_subsequence(nums: List[int], k: int) -> List[int]:
        """使用单调栈获取长度为k的最大子序列"""
        drop = len(nums) - k
        stack = []
        for num in nums:
            while drop > 0 and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k]
    
    def merge(nums1: List[int], nums2: List[int]) -> List[int]:
        """合并两个数组，保持字典序最大"""
        result = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                result.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                result.append(nums1[i])
                i += 1
            elif nums1[i:] > nums2[j:]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        return result
    
    result = []
    for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
        sub1 = get_max_subsequence(nums1, i)
        sub2 = get_max_subsequence(nums2, k - i)
        merged = merge(sub1, sub2)
        if merged > result:
            result = merged
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(max_number)
