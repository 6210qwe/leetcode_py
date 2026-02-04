# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2140
标题: Longest Subsequence Repeated k Times
难度: hard
链接: https://leetcode.cn/problems/longest-subsequence-repeated-k-times/
题目类型: 贪心、字符串、回溯、计数、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2014. 重复 K 次的最长子序列 - 给你一个长度为 n 的字符串 s ，和一个整数 k 。请你找出字符串 s 中 重复 k 次的 最长子序列 。 子序列 是由其他字符串删除某些（或不删除）字符派生而来的一个字符串。 如果 seq * k 是 s 的一个子序列，其中 seq * k 表示一个由 seq 串联 k 次构造的字符串，那么就称 seq 是字符串 s 中一个 重复 k 次 的子序列。 * 举个例子，"bba" 是字符串 "bababcba" 中的一个重复 2 次的子序列，因为字符串 "bbabba" 是由 "bba" 串联 2 次构造的，而 "bbabba" 是字符串 "bababcba" 的一个子序列。 返回字符串 s 中 重复 k 次的最长子序列 。如果存在多个满足的子序列，则返回 字典序最大 的那个。如果不存在这样的子序列，返回一个 空 字符串。 示例 1： example 1 [https://assets.leetcode.com/uploads/2021/08/30/longest-subsequence-repeat-k-times.png] 输入：s = "letsleetcode", k = 2 输出："let" 解释：存在两个最长子序列重复 2 次：let" 和 "ete" 。 "let" 是其中字典序最大的一个。 示例 2： 输入：s = "bb", k = 2 输出："b" 解释：重复 2 次的最长子序列是 "b" 。 示例 3： 输入：s = "ab", k = 2 输出："" 解释：不存在重复 2 次的最长子序列。返回空字符串。 提示： * n == s.length * 2 <= k <= 2000 * 2 <= n < min(2001, k * 8) * s 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和回溯法来找到最长的重复 k 次的子序列。

算法步骤:
1. 计算每个字符在字符串 s 中出现的次数。
2. 构建一个可能的候选字符列表，这些字符在 s 中出现的次数至少为 k。
3. 使用回溯法生成所有可能的子序列，并检查它们是否可以在 s 中重复 k 次。
4. 选择最长且字典序最大的子序列。

关键点:
- 通过贪心算法优先选择出现次数最多的字符。
- 使用回溯法生成所有可能的子序列。
- 检查生成的子序列是否可以在 s 中重复 k 次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(26^m)，其中 m 是 s 中不同字符的数量。
空间复杂度: O(m)，用于存储候选字符列表和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_subsequence(s: str, sub: str, k: int) -> bool:
    """
    检查 sub 是否可以重复 k 次作为 s 的子序列。
    """
    it = iter(s)
    return all(char in it for char in sub * k)


def backtrack(s: str, k: int, path: List[str], result: List[str]):
    if len(path) > len(result):
        if is_subsequence(s, ''.join(path), k):
            result[:] = path[:]
    
    for i in range(len(path) + 1):
        new_path = path[:i] + [path[-1]] + path[i:]
        if is_subsequence(s, ''.join(new_path), k):
            backtrack(s, k, new_path, result)


def solution_function_name(s: str, k: int) -> str:
    """
    函数式接口 - 找到字符串 s 中重复 k 次的最长子序列。
    """
    from collections import Counter
    
    # 计算每个字符的出现次数
    char_count = Counter(s)
    
    # 构建候选字符列表
    candidates = [char for char, count in char_count.items() if count >= k]
    
    # 初始化结果
    result = []
    
    # 回溯法生成所有可能的子序列
    for char in candidates:
        backtrack(s, k, [char], result)
    
    # 返回最长且字典序最大的子序列
    return ''.join(sorted(result, reverse=True))


Solution = create_solution(solution_function_name)