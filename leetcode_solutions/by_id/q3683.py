# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3683
标题: Find the Lexicographically Largest String From the Box I
难度: medium
链接: https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/
题目类型: 双指针、字符串、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3403. 从盒子中找出字典序最大的字符串 I - 给你一个字符串 word 和一个整数 numFriends。 Alice 正在为她的 numFriends 位朋友组织一个游戏。游戏分为多个回合，在每一回合中： * word 被分割成 numFriends 个 非空 字符串，且该分割方式与之前的任意回合所采用的都 不完全相同 。 * 所有分割出的字符串都会被放入一个盒子中。 在所有回合结束后，找出盒子中 字典序最大的 字符串。 示例 1： 输入: word = "dbca", numFriends = 2 输出: "dbc" 解释: 所有可能的分割方式为： * "d" 和 "bca"。 * "db" 和 "ca"。 * "dbc" 和 "a"。 示例 2： 输入: word = "gggg", numFriends = 4 输出: "g" 解释: 唯一可能的分割方式为："g", "g", "g", 和 "g"。 提示: * 1 <= word.length <= 5 * 103 * word 仅由小写英文字母组成。 * 1 <= numFriends <= word.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法找到字典序最大的字符串。每次选择当前未使用的最大字符作为起始点，尽可能多地扩展该字符串，直到无法再扩展为止。

算法步骤:
1. 初始化一个变量 `max_str` 用于存储当前找到的最大字符串。
2. 遍历字符串 `word`，从右向左查找每个字符，确保每个字符都能成为某个子字符串的起始点。
3. 对于每个起始点，尽可能多地扩展子字符串，直到无法再扩展为止。
4. 更新 `max_str` 为当前找到的最大字符串。
5. 返回 `max_str`。

关键点:
- 从右向左遍历字符串，确保每次选择的都是当前未使用的最大字符。
- 尽可能多地扩展子字符串，确保找到的字符串是字典序最大的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是字符串 `word` 的长度。最坏情况下，需要遍历字符串并进行多次扩展操作。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(word: str, numFriends: int) -> str:
    """
    函数式接口 - 实现
    """
    def find_max_substring(start: int) -> str:
        max_substring = ""
        for i in range(start, len(word)):
            if word[i] >= max_substring[0] if max_substring else True:
                max_substring = word[start:i+1]
        return max_substring

    max_str = ""
    for i in range(len(word) - 1, -1, -1):
        max_substring = find_max_substring(i)
        if max_substring > max_str:
            max_str = max_substring
    return max_str


Solution = create_solution(solution_function_name)