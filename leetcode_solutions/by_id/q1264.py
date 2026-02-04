# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1264
标题: Maximum Number of Words You Can Type
难度: easy
链接: https://leetcode.cn/problems/maximum-number-of-words-you-can-type/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1935. 可以输入的最大单词数 - 键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。 给你一个由若干单词组成的字符串 text ，单词间由单个空格组成（不含前导和尾随空格）；另有一个字符串 brokenLetters ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 text 中单词的数目。 示例 1： 输入：text = "hello world", brokenLetters = "ad" 输出：1 解释：无法输入 "world" ，因为字母键 'd' 已损坏。 示例 2： 输入：text = "leet code", brokenLetters = "lt" 输出：1 解释：无法输入 "leet" ，因为字母键 'l' 和 't' 已损坏。 示例 3： 输入：text = "leet code", brokenLetters = "e" 输出：0 解释：无法输入任何单词，因为字母键 'e' 已损坏。 提示： * 1 <= text.length <= 104 * 0 <= brokenLetters.length <= 26 * text 由若干用单个空格分隔的单词组成，且不含任何前导和尾随空格 * 每个单词仅由小写英文字母组成 * brokenLetters 由 互不相同 的小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来存储损坏的字母，并遍历每个单词检查是否包含损坏的字母。

算法步骤:
1. 将 brokenLetters 转换为集合，以便快速查找。
2. 将 text 按空格分割成单词列表。
3. 遍历每个单词，检查是否包含任何损坏的字母。
4. 统计可以完全输入的单词数量。

关键点:
- 使用集合来存储损坏的字母，以便 O(1) 时间复杂度进行查找。
- 遍历每个单词并检查是否包含损坏的字母。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 text 的长度，m 是 brokenLetters 的长度。
空间复杂度: O(m)，用于存储损坏的字母集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_type_words(text: str, broken_letters: str) -> int:
    """
    函数式接口 - 返回可以使用此键盘完全输入的 text 中单词的数目。
    """
    # 将 brokenLetters 转换为集合
    broken_set = set(broken_letters)
    
    # 将 text 按空格分割成单词列表
    words = text.split()
    
    # 统计可以完全输入的单词数量
    count = sum(1 for word in words if not any(char in broken_set for char in word))
    
    return count


Solution = create_solution(can_type_words)