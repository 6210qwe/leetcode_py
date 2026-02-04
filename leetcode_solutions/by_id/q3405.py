# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3405
标题: Count the Number of Special Characters II
难度: medium
链接: https://leetcode.cn/problems/count-the-number-of-special-characters-ii/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3121. 统计特殊字母的数量 II - 给你一个字符串 word。如果 word 中同时出现某个字母 c 的小写形式和大写形式，并且 每个 小写形式的 c 都出现在第一个大写形式的 c 之前，则称字母 c 是一个 特殊字母 。 返回 word 中 特殊字母 的数量。 示例 1: 输入：word = "aaAbcBC" 输出：3 解释： 特殊字母是 'a'、'b' 和 'c'。 示例 2: 输入：word = "abc" 输出：0 解释： word 中不存在特殊字母。 示例 3: 输入：word = "AbBCab" 输出：0 解释： word 中不存在特殊字母。 提示： * 1 <= word.length <= 2 * 105 * word 仅由小写和大写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个字典分别记录每个字母的小写和大写形式的最早出现位置，然后遍历字典判断是否满足条件。

算法步骤:
1. 初始化两个字典 `lower_case` 和 `upper_case`，分别记录每个字母的小写和大写形式的最早出现位置。
2. 遍历字符串 `word`，更新 `lower_case` 和 `upper_case` 字典。
3. 遍历 `lower_case` 字典，检查每个字母是否在 `upper_case` 字典中存在，并且小写字母的最早出现位置小于大写字母的最早出现位置。
4. 统计满足条件的字母数量。

关键点:
- 使用字典记录字母的最早出现位置，确保时间复杂度为 O(n)。
- 通过比较小写字母和大写字母的最早出现位置来判断是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 `word` 的长度。我们只需要遍历字符串一次，并进行常数时间的操作。
空间复杂度: O(1)，因为字母表的大小是固定的（最多 52 个字母）。
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
    lower_case = {}
    upper_case = {}

    # 记录每个字母的小写和大写形式的最早出现位置
    for i, char in enumerate(word):
        if char.islower():
            if char not in lower_case:
                lower_case[char] = i
        else:
            if char.lower() not in upper_case:
                upper_case[char.lower()] = i

    # 统计满足条件的字母数量
    count = 0
    for char in lower_case:
        if char in upper_case and lower_case[char] < upper_case[char]:
            count += 1

    return count


Solution = create_solution(count_special_characters)