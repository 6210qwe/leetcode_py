# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1423
标题: Maximum Number of Occurrences of a Substring
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1297. 子串的最大出现次数 - 给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数： * 子串中不同字母的数目必须小于等于 maxLetters 。 * 子串的长度必须大于等于 minSize 且小于等于 maxSize 。 示例 1： 输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4 输出：2 解释：子串 "aab" 在原字符串中出现了 2 次。 它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。 示例 2： 输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3 输出：2 解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。 示例 3： 输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3 输出：3 示例 4： 输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3 输出：0 提示： * 1 <= s.length <= 10^5 * 1 <= maxLetters <= 26 * 1 <= minSize <= maxSize <= min(26, s.length) * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来统计满足条件的子串出现次数。

算法步骤:
1. 初始化一个哈希表来记录每个子串的出现次数。
2. 使用滑动窗口遍历字符串，窗口大小为 minSize。
3. 对于每个窗口内的子串，检查其不同字符数是否小于等于 maxLetters。
4. 如果满足条件，将该子串的出现次数加一。
5. 最后返回哈希表中出现次数最多的子串的出现次数。

关键点:
- 使用滑动窗口可以高效地遍历所有可能的子串。
- 使用哈希表记录子串的出现次数，便于快速查找和更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * minSize)，其中 n 是字符串 s 的长度，minSize 是子串的最小长度。
空间复杂度: O(n * minSize)，最坏情况下，哈希表中存储了所有可能的子串。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    """
    函数式接口 - 返回满足条件且出现次数最大的子串的出现次数
    """
    from collections import Counter
    
    # 初始化计数器
    counter = Counter()
    
    # 使用滑动窗口遍历字符串
    for i in range(len(s) - minSize + 1):
        substring = s[i:i + minSize]
        if len(set(substring)) <= maxLetters:
            counter[substring] += 1
    
    # 返回出现次数最多的子串的出现次数
    return max(counter.values()) if counter else 0


Solution = create_solution(solution_function_name)