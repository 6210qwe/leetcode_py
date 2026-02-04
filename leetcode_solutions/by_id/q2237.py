# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2237
标题: Longest Palindrome by Concatenating Two Letter Words
难度: medium
链接: https://leetcode.cn/problems/longest-palindrome-by-concatenating-two-letter-words/
题目类型: 贪心、数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2131. 连接两字母单词得到的最长回文串 - 给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。 请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。 请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。 回文串 指的是从前往后和从后往前读一样的字符串。 示例 1： 输入：words = ["lc","cl","gg"] 输出：6 解释：一个最长的回文串为 "lc" + "gg" + "cl" = "lcggcl" ，长度为 6 。 "clgglc" 是另一个可以得到的最长回文串。 示例 2： 输入：words = ["ab","ty","yt","lc","cl","ab"] 输出：8 解释：最长回文串是 "ty" + "lc" + "cl" + "yt" = "tylcclyt" ，长度为 8 。 "lcyttycl" 是另一个可以得到的最长回文串。 示例 3： 输入：words = ["cc","ll","xx"] 输出：2 解释：最长回文串是 "cc" ，长度为 2 。 "ll" 是另一个可以得到的最长回文串。"xx" 也是。 提示： * 1 <= words.length <= 105 * words[i].length == 2 * words[i] 仅包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每种类型的两字母单词的数量，然后根据回文串的特性进行构造。

算法步骤:
1. 使用哈希表统计每种两字母单词的数量。
2. 分别处理对称和非对称的两字母单词：
   - 对于对称的两字母单词（如 "aa"），可以直接添加到回文串中，最多只能有一个未配对的对称单词。
   - 对于非对称的两字母单词（如 "ab" 和 "ba"），找到它们的最小配对数量，将这些配对添加到回文串中。
3. 计算最终的回文串长度。

关键点:
- 使用哈希表高效统计每种两字母单词的数量。
- 根据回文串的特性，合理处理对称和非对称的两字母单词。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 words 的长度。我们只需要遍历一次 words 数组。
空间复杂度: O(1)，哈希表的大小是固定的，最多有 26*26 种两字母单词。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_palindrome(words: List[str]) -> int:
    """
    函数式接口 - 返回由给定两字母单词组成的最长回文串的长度
    """
    # 哈希表统计每种两字母单词的数量
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # 初始化回文串长度
    length = 0
    # 用于记录是否已经使用了一个未配对的对称单词
    has_center = False
    
    for word, count in word_count.items():
        if word[0] == word[1]:  # 对称的两字母单词
            if count % 2 == 0:
                length += count * 2
            else:
                length += (count - 1) * 2
                has_center = True
        else:  # 非对称的两字母单词
            reverse_word = word[1] + word[0]
            if reverse_word in word_count:
                min_count = min(count, word_count[reverse_word])
                length += min_count * 4
                word_count[reverse_word] -= min_count
                word_count[word] -= min_count
    
    # 如果有未配对的对称单词，可以在回文串中心添加一个
    if has_center:
        length += 2
    
    return length


Solution = create_solution(longest_palindrome)