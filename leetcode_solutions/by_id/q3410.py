# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3410
标题: Find Longest Self-Contained Substring
难度: hard
链接: https://leetcode.cn/problems/find-longest-self-contained-substring/
题目类型: 哈希表、字符串、二分查找、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3104. 查找最长的自包含子串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表和前缀和来记录字符出现的位置，并通过二分查找来找到最长的自包含子串。

算法步骤:
1. 初始化一个哈希表 `char_positions` 来记录每个字符的所有出现位置。
2. 遍历字符串，填充 `char_positions`。
3. 初始化一个数组 `prefix_sum`，用于记录每个字符在当前位置之前的出现次数。
4. 遍历字符串，填充 `prefix_sum`。
5. 使用二分查找来找到最长的自包含子串。对于每个可能的子串长度，检查是否存在一个子串满足条件。

关键点:
- 使用哈希表记录字符位置，便于快速查找。
- 使用前缀和记录字符出现次数，便于快速判断子串是否自包含。
- 使用二分查找优化查找过程，提高效率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。遍历字符串的时间复杂度是 O(n)，二分查找的时间复杂度是 O(log n)。
空间复杂度: O(n)，哈希表和前缀和数组的空间复杂度都是 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_longest_self_contained_substring(s: str) -> int:
    """
    函数式接口 - 查找最长的自包含子串
    """
    def is_valid_substring(start: int, length: int) -> bool:
        """
        检查从 start 开始，长度为 length 的子串是否是自包含的
        """
        for char in set(s[start:start + length]):
            if s[start:start + length].count(char) != prefix_sum[start + length][ord(char) - ord('a')] - prefix_sum[start][ord(char) - ord('a')]:
                return False
        return True

    n = len(s)
    if n == 0:
        return 0

    # 记录每个字符的所有出现位置
    char_positions = [[] for _ in range(26)]
    for i, char in enumerate(s):
        char_positions[ord(char) - ord('a')].append(i)

    # 构建前缀和数组
    prefix_sum = [[0] * 26]
    for i, char in enumerate(s):
        new_row = prefix_sum[-1][:]  # 复制上一行
        new_row[ord(char) - ord('a')] += 1
        prefix_sum.append(new_row)

    # 二分查找最长的自包含子串
    left, right = 1, n
    result = 0
    while left <= right:
        mid = (left + right) // 2
        valid = False
        for start in range(n - mid + 1):
            if is_valid_substring(start, mid):
                valid = True
                break
        if valid:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


Solution = create_solution(find_longest_self_contained_substring)