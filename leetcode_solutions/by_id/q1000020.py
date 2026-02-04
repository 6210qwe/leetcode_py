# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000020
标题: Re-Space LCCI
难度: medium
链接: https://leetcode.cn/problems/re-space-lcci/
题目类型: 字典树、数组、哈希表、字符串、动态规划、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.13. 恢复空格 - 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。 注意：本题相对原题稍作改动，只需返回未识别的字符数 示例： 输入： dictionary = ["looked","just","like","her","brother"] sentence = "jesslookedjustliketimherbrother" 输出： 7 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。 提示： * 0 <= len(sentence) <= 1000 * dictionary中总字符数不超过 150000。 * 你可以认为dictionary和sentence中只包含小写字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。定义dp[i]为前i个字符的最小未识别字符数。

算法步骤:
1. 初始化dp数组，长度为n+1，其中n是sentence的长度。dp[0] = 0，因为前0个字符没有未识别字符。
2. 遍历sentence的每个位置i，初始化dp[i+1] = dp[i] + 1，表示当前字符未被识别。
3. 对于每个位置i，检查从0到i的所有子串，如果子串在字典中，则更新dp[i+1] = min(dp[i+1], dp[j])，其中j是子串的起始位置。

关键点:
- 使用动态规划来记录最小未识别字符数。
- 通过遍历所有可能的子串来更新dp数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中n是sentence的长度。最坏情况下，需要检查所有子串。
空间复杂度: O(n)，需要一个长度为n+1的dp数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def respace(dictionary: List[str], sentence: str) -> int:
    """
    函数式接口 - 返回未识别的字符数
    """
    n = len(sentence)
    dp = [0] * (n + 1)

    # 将字典转换为集合，便于快速查找
    dictionary_set = set(dictionary)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1  # 当前字符未被识别
        for j in range(i):
            if sentence[j:i] in dictionary_set:
                dp[i] = min(dp[i], dp[j])
                break  # 找到匹配的子串后，不需要再检查更短的子串

    return dp[n]


Solution = create_solution(respace)