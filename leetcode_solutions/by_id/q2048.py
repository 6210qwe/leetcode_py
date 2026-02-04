# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2048
标题: Build Array from Permutation
难度: easy
链接: https://leetcode.cn/problems/build-array-from-permutation/
题目类型: 数组、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1920. 基于排列构建数组 - 给你一个 从 0 开始的排列 nums（下标也从 0 开始）。请你构建一个 同样长度 的数组 ans ，其中，对于每个 i（0 <= i < nums.length），都满足 ans[i] = nums[nums[i]] 。返回构建好的数组 ans 。 从 0 开始的排列 nums 是一个由 0 到 nums.length - 1（0 和 nums.length - 1 也包含在内）的不同整数组成的数组。 示例 1： 输入：nums = [0,2,1,5,3,4] 输出：[0,1,2,4,5,3] 解释：数组 ans 构建如下： ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]] = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]] = [0,1,2,4,5,3] 示例 2： 输入：nums = [5,0,1,2,3,4] 输出：[4,5,0,1,2,3] 解释：数组 ans 构建如下： ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]] = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]] = [4,5,0,1,2,3] 提示： * 1 <= nums.length <= 1000 * 0 <= nums[i] < nums.length * nums 中的元素 互不相同 进阶：你能在不使用额外空间的情况下解决此问题吗（即 O(1) 内存）？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 直接遍历输入数组并构建结果数组。

算法步骤:
1. 初始化一个与输入数组等长的结果数组。
2. 遍历输入数组，对于每个索引 i，将 nums[nums[i]] 的值赋给结果数组的第 i 个位置。

关键点:
- 通过直接遍历和赋值，可以在 O(n) 时间复杂度内完成构建。
- 为了达到 O(1) 空间复杂度，我们直接在原数组上进行修改。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def build_array(nums: List[int]) -> List[int]:
    """
    函数式接口 - 构建数组
    """
    n = len(nums)
    for i in range(n):
        # 将 nums[i] 的值编码到 nums[nums[i]] 中
        nums[i] += n * (nums[nums[i]] % n)
    
    for i in range(n):
        # 解码得到最终结果
        nums[i] //= n
    
    return nums


Solution = create_solution(build_array)