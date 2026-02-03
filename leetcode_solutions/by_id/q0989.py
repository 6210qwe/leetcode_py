# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 989
标题: Largest Component Size by Common Factor
难度: hard
链接: https://leetcode.cn/problems/largest-component-size-by-common-factor/
题目类型: 并查集、数组、哈希表、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
952. 按公因数计算最大组件大小 - 给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图： * 有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记； * 只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。 返回 图中最大连通组件的大小 。 示例 1： [https://assets.leetcode.com/uploads/2018/12/01/ex1.png] 输入：nums = [4,6,15,35] 输出：4 示例 2： [https://assets.leetcode.com/uploads/2018/12/01/ex2.png] 输入：nums = [20,50,9,63] 输出：2 示例 3： [https://assets.leetcode.com/uploads/2018/12/01/ex3.png] 输入：nums = [2,3,6,7,4,12,21,39] 输出：8 提示： * 1 <= nums.length <= 2 * 104 * 1 <= nums[i] <= 105 * nums 中所有值都 不同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
