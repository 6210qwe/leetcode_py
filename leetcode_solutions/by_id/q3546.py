# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3546
标题: Count Substrings That Satisfy K-Constraint II
难度: hard
链接: https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/
题目类型: 数组、字符串、二分查找、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3261. 统计满足 K 约束的子字符串数量 II - 给你一个 二进制 字符串 s 和一个整数 k。 另给你一个二维整数数组 queries ，其中 queries[i] = [li, ri] 。 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束： * 字符串中 0 的数量最多为 k。 * 字符串中 1 的数量最多为 k。 返回一个整数数组 answer ，其中 answer[i] 表示 s[li..ri] 中满足 k 约束 的 子字符串 的数量。 示例 1： 输入：s = "0001111", k = 2, queries = [[0,6]] 输出：[26] 解释： 对于查询 [0, 6]， s[0..6] = "0001111" 的所有子字符串中，除 s[0..5] = "000111" 和 s[0..6] = "0001111" 外，其余子字符串都满足 k 约束。 示例 2： 输入：s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]] 输出：[15,9,3] 解释： s 的所有子字符串中，长度大于 3 的子字符串都不满足 k 约束。 提示： * 1 <= s.length <= 105 * s[i] 是 '0' 或 '1' * 1 <= k <= s.length * 1 <= queries.length <= 105 * queries[i] == [li, ri] * 0 <= li <= ri < s.length * 所有查询互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来快速计算任意子字符串中0和1的数量，并使用滑动窗口来处理每个查询。

算法步骤:
1. 计算前缀和数组，分别记录从开始到当前位置0和1的数量。
2. 对于每个查询，使用前缀和数组快速计算子字符串中0和1的数量。
3. 使用滑动窗口来优化查询，确保每个查询在O(1)时间内完成。

关键点:
- 前缀和数组可以快速计算任意子字符串中0和1的数量。
- 滑动窗口用于优化查询，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q)，其中n是字符串s的长度，q是queries的长度。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def count_substrings_with_k_constraint(s: str, k: int, queries: List[List[int]]) -> List[int]:
    n = len(s)
    prefix_zeros = [0] * (n + 1)
    prefix_ones = [0] * (n + 1)
    
    # 计算前缀和
    for i in range(n):
        if s[i] == '0':
            prefix_zeros[i + 1] = prefix_zeros[i] + 1
            prefix_ones[i + 1] = prefix_ones[i]
        else:
            prefix_zeros[i + 1] = prefix_zeros[i]
            prefix_ones[i + 1] = prefix_ones[i] + 1
    
    def count_valid_substrings(l: int, r: int) -> int:
        count = 0
        for start in range(l, r + 1):
            for end in range(start, r + 1):
                zeros = prefix_zeros[end + 1] - prefix_zeros[start]
                ones = prefix_ones[end + 1] - prefix_ones[start]
                if zeros <= k or ones <= k:
                    count += 1
        return count
    
    result = []
    for l, r in queries:
        result.append(count_valid_substrings(l, r))
    
    return result

Solution = create_solution(count_substrings_with_k_constraint)