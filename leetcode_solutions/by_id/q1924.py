# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1924
标题: Maximum Number of Groups Getting Fresh Donuts
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-groups-getting-fresh-donuts/
题目类型: 位运算、记忆化搜索、数组、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1815. 得到新鲜甜甜圈的最多组数 - 有一个甜甜圈商店，每批次都烤 batchSize 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 所有 甜甜圈都必须已经全部销售完毕。给你一个整数 batchSize 和一个整数数组 groups ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 groups[i] 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。 当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。 你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多 有多少组人会感到开心。 示例 1： 输入：batchSize = 3, groups = [1,2,3,4,5,6] 输出：4 解释：你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。 示例 2： 输入：batchSize = 4, groups = [1,3,2,5,2,2,1,6] 输出：4 提示： * 1 <= batchSize <= 9 * 1 <= groups.length <= 30 * 1 <= groups[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们使用一个二进制掩码来表示当前哪些组已经被处理过，然后使用记忆化搜索来优化重复计算。

算法步骤:
1. 将每个组的大小对 batchSize 取模，只保留余数。
2. 使用一个二进制掩码来表示当前哪些组已经被处理过。
3. 使用记忆化搜索来计算最大开心组数。

关键点:
- 通过取模操作减少状态空间。
- 使用二进制掩码和记忆化搜索来优化计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * n)，其中 n 是 groups 的长度。因为我们需要遍历所有可能的状态，并且每个状态需要 O(n) 时间来处理。
空间复杂度: O(2^n * n)，记忆化搜索需要存储每个状态的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

def max_happy_groups(batch_size: int, groups: List[int]) -> int:
    """
    函数式接口 - 计算最多有多少组人会感到开心
    """
    # 将每个组的大小对 batchSize 取模
    mod_groups = [g % batch_size for g in groups if g % batch_size != 0]
    
    # 使用记忆化搜索
    @lru_cache(None)
    def dp(mask, remaining):
        if mask == (1 << len(mod_groups)) - 1:
            return 0
        
        max_happy = 0
        for i in range(len(mod_groups)):
            if not (mask & (1 << i)):
                new_remaining = (remaining + mod_groups[i]) % batch_size
                happy = 1 if new_remaining == 0 else 0
                max_happy = max(max_happy, happy + dp(mask | (1 << i), new_remaining))
        
        return max_happy
    
    return dp(0, 0) + groups.count(batch_size)

Solution = create_solution(max_happy_groups)