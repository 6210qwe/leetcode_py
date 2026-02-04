# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3408
标题: Count the Number of Special Characters I
难度: easy
链接: https://leetcode.cn/problems/count-the-number-of-special-characters-i/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3120. 统计特殊字母的数量 I - 给你一个字符串 word。如果 word 中同时存在某个字母的小写形式和大写形式，则称这个字母为 特殊字母 。 返回 word 中 特殊字母 的数量。 示例 1: 输入：word = "aaAbcBC" 输出：3 解释： word 中的特殊字母是 'a'、'b' 和 'c'。 示例 2: 输入：word = "abc" 输出：0 解释： word 中不存在大小写形式同时出现的字母。 示例 3: 输入：word = "abBCab" 输出：1 解释： word 中唯一的特殊字母是 'b'。 提示： * 1 <= word.length <= 50 * word 仅由小写和大写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来记录出现过的小写字母和大写字母，然后检查每个字母是否同时存在于两个集合中。

算法步骤:
1. 初始化两个集合，分别用于存储小写字母和大写字母。
2. 遍历字符串，将每个字符添加到相应的集合中。
3. 遍历所有字母（从 'a' 到 'z'），检查其小写和大写形式是否同时存在于两个集合中。
4. 统计满足条件的字母数量。

关键点:
- 使用集合进行快速查找。
- 只需要遍历一次字符串和一次字母表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + 26) = O(n)，其中 n 是字符串的长度。
空间复杂度: O(1)，因为集合的大小最多为 26 个字母。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_special_characters(word: str) -> int:
    """
    函数式接口 - 统计特殊字母的数量
    """
    # 初始化两个集合
    lower_set = set()
    upper_set = set()

    # 遍历字符串，将每个字符添加到相应的集合中
    for char in word:
        if char.islower():
            lower_set.add(char)
        else:
            upper_set.add(char)

    # 统计满足条件的字母数量
    special_count = 0
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in lower_set and char.upper() in upper_set:
            special_count += 1

    return special_count


Solution = create_solution(count_special_characters)