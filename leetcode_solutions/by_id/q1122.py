# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1122
标题: Longest Duplicate Substring
难度: hard
链接: https://leetcode.cn/problems/longest-duplicate-substring/
题目类型: 字符串、二分查找、后缀数组、滑动窗口、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1044. 最长重复子串 - 给你一个字符串 s ，考虑其所有 重复子串 ：即 s 的（连续）子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。 示例 1： 输入：s = "banana" 输出："ana" 示例 2： 输入：s = "abcd" 输出："" 提示： * 2 <= s.length <= 3 * 104 * s 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和滚动哈希来找到最长的重复子串。

算法步骤:
1. 使用二分查找确定最长重复子串的长度。
2. 对于每个长度，使用滚动哈希检查是否存在重复子串。
3. 如果存在，则更新结果并继续查找更长的子串；否则，缩短子串长度。

关键点:
- 使用二分查找来优化查找过程。
- 使用滚动哈希来高效地计算子串的哈希值。
- 处理哈希冲突，确保找到的子串是真正的重复子串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> str:
    """
    函数式接口 - 找到最长的重复子串
    """
    def search(length: int) -> str:
        seen = set()
        hash_val = 0
        base = 26
        mod = 2 ** 32
        
        for i in range(length):
            hash_val = (hash_val * base + ord(s[i])) % mod
        
        seen.add(hash_val)
        
        for i in range(1, len(s) - length + 1):
            hash_val = (hash_val * base - ord(s[i - 1]) * pow(base, length, mod) + ord(s[i + length - 1])) % mod
            if hash_val in seen:
                return s[i:i + length]
            seen.add(hash_val)
        
        return ""
    
    left, right = 1, len(s)
    result = ""
    
    while left <= right:
        mid = (left + right) // 2
        dup = search(mid)
        if dup:
            result = dup
            left = mid + 1
        else:
            right = mid - 1
    
    return result


Solution = create_solution(solution_function_name)