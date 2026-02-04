# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2715
标题: K Items With the Maximum Sum
难度: easy
链接: https://leetcode.cn/problems/k-items-with-the-maximum-sum/
题目类型: 贪心、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2600. K 件物品的最大和 - 袋子中装有一些物品，每个物品上都标记着数字 1 、0 或 -1 。 给你四个非负整数 numOnes 、numZeros 、numNegOnes 和 k 。 袋子最初包含： * numOnes 件标记为 1 的物品。 * numZeros 件标记为 0 的物品。 * numNegOnes 件标记为 -1 的物品。 现计划从这些物品中恰好选出 k 件物品。返回所有可行方案中，物品上所标记数字之和的最大值。 示例 1： 输入：numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2 输出：2 解释：袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 2 件标记为 1 的物品，得到的数字之和为 2 。 可以证明 2 是所有可行方案中的最大值。 示例 2： 输入：numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4 输出：3 解释：袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 3 件标记为 1 的物品，1 件标记为 0 的物品，得到的数字之和为 3 。 可以证明 3 是所有可行方案中的最大值。 提示： * 0 <= numOnes, numZeros, numNegOnes <= 50 * 0 <= k <= numOnes + numZeros + numNegOnes
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 优先选择标记为 1 的物品，其次是标记为 0 的物品，最后是标记为 -1 的物品。

算法步骤:
1. 尽可能多地选择标记为 1 的物品。
2. 如果还需要更多物品，则选择标记为 0 的物品。
3. 如果仍然需要更多物品，则选择标记为 -1 的物品。

关键点:
- 通过贪心策略，确保每次选择的物品都是当前最优的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def k_items_with_maximum_sum(num_ones: int, num_zeros: int, num_neg_ones: int, k: int) -> int:
    """
    函数式接口 - 返回选择 k 件物品后，物品上所标记数字之和的最大值。
    """
    # 尽可能多地选择标记为 1 的物品
    ones_selected = min(num_ones, k)
    k -= ones_selected
    
    # 如果还需要更多物品，则选择标记为 0 的物品
    zeros_selected = min(num_zeros, k)
    k -= zeros_selected
    
    # 如果仍然需要更多物品，则选择标记为 -1 的物品
    neg_ones_selected = k
    
    # 计算总和
    total_sum = ones_selected * 1 + zeros_selected * 0 + neg_ones_selected * (-1)
    
    return total_sum


Solution = create_solution(k_items_with_maximum_sum)