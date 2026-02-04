# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2274
标题: Keep Multiplying Found Values by Two
难度: easy
链接: https://leetcode.cn/problems/keep-multiplying-found-values-by-two/
题目类型: 数组、哈希表、排序、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2154. 将找到的值乘以 2 - 给你一个整数数组 nums ，另给你一个整数 original ，这是需要在 nums 中搜索的第一个数字。 接下来，你需要按下述步骤操作： 1. 如果在 nums 中找到 original ，将 original 乘以 2 ，得到新 original（即，令 original = 2 * original）。 2. 否则，停止这一过程。 3. 只要能在数组中找到新 original ，就对新 original 继续 重复 这一过程。 返回 original 的 最终 值。 示例 1： 输入：nums = [5,3,6,1,12], original = 3 输出：24 解释： - 3 能在 nums 中找到。3 * 2 = 6 。 - 6 能在 nums 中找到。6 * 2 = 12 。 - 12 能在 nums 中找到。12 * 2 = 24 。 - 24 不能在 nums 中找到。因此，返回 24 。 示例 2： 输入：nums = [2,7,9], original = 4 输出：4 解释： - 4 不能在 nums 中找到。因此，返回 4 。 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i], original <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来存储数组中的元素，以便快速查找。

算法步骤:
1. 将数组转换为集合，以便 O(1) 时间复杂度的查找。
2. 在集合中查找 original，如果找到则将其乘以 2，继续查找新的 original。
3. 如果找不到 original，则返回当前的 original。

关键点:
- 使用集合来优化查找操作，减少时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 nums 的长度。最坏情况下，我们需要遍历整个数组。
空间复杂度: O(n)，使用集合存储数组中的元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], original: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 将数组转换为集合
    num_set = set(nums)
    
    # 循环查找并更新 original
    while original in num_set:
        original *= 2
    
    return original


Solution = create_solution(solution_function_name)