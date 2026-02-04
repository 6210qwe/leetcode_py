# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3510
标题: Maximize the Total Height of Unique Towers
难度: medium
链接: https://leetcode.cn/problems/maximize-the-total-height-of-unique-towers/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3301. 高度互不相同的最大塔高和 - 给你一个数组 maximumHeight ，其中 maximumHeight[i] 表示第 i 座塔可以达到的 最大 高度。 你的任务是给每一座塔分别设置一个高度，使得： 1. 第 i 座塔的高度是一个正整数，且不超过 maximumHeight[i] 。 2. 所有塔的高度互不相同。 请你返回设置完所有塔的高度后，可以达到的 最大 总高度。如果没有合法的设置，返回 -1 。 示例 1： 输入：maximumHeight = [2,3,4,3] 输出：10 解释： 我们可以将塔的高度设置为：[1, 2, 4, 3] 。 示例 2： 输入：maximumHeight = [15,10] 输出：25 解释： 我们可以将塔的高度设置为：[15, 10] 。 示例 3： 输入：maximumHeight = [2,2,1] 输出：-1 解释： 无法设置塔的高度为正整数且高度互不相同。 提示： * 1 <= maximumHeight.length <= 105 * 1 <= maximumHeight[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，通过排序和分配最小可用高度来确保所有塔的高度互不相同。

算法步骤:
1. 对 maximumHeight 数组进行降序排序。
2. 初始化一个集合 used_heights 来记录已经使用过的高度。
3. 初始化一个变量 total_height 来记录总高度。
4. 遍历排序后的 maximumHeight 数组，对于每个高度：
   - 从 1 开始尝试分配最小未使用的高度。
   - 如果当前高度大于等于待分配的高度，则将其分配给当前塔，并更新 total_height 和 used_heights。
   - 如果遍历完所有可能的高度都无法分配，则返回 -1。
5. 返回 total_height。

关键点:
- 通过降序排序确保优先处理较高的塔。
- 使用集合记录已使用的高度，确保高度互不相同。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 maximumHeight 的长度，主要由排序操作决定。
空间复杂度: O(n)，用于存储已使用的高度集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximize_total_height(maximumHeight: List[int]) -> int:
    """
    函数式接口 - 计算高度互不相同的最大塔高和
    """
    # 降序排序
    maximumHeight.sort(reverse=True)
    
    used_heights = set()
    total_height = 0
    
    for max_h in maximumHeight:
        for h in range(1, max_h + 1):
            if h not in used_heights:
                used_heights.add(h)
                total_height += h
                break
        else:
            return -1  # 无法找到合适的高度
    
    return total_height


Solution = create_solution(maximize_total_height)