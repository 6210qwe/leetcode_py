# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1273
标题: Compare Strings by Frequency of the Smallest Character
难度: medium
链接: https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/
题目类型: 数组、哈希表、字符串、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1170. 比较字符串最小字母出现频次 - 定义一个函数 f(s)，统计 s 中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。 示例 1： 输入：queries = ["cbd"], words = ["zaaaz"] 输出：[1] 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。 示例 2： 输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"] 输出：[1,2] 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。 提示： * 1 <= queries.length <= 2000 * 1 <= words.length <= 2000 * 1 <= queries[i].length, words[i].length <= 10 * queries[i][j]、words[i][j] 都由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用预处理和二分查找来优化查询效率。

算法步骤:
1. 定义一个辅助函数 `f(s)` 来计算字符串 s 中最小字母的出现频次。
2. 对 `words` 中的每个字符串应用 `f(s)` 并存储结果。
3. 对 `words` 的频次结果进行排序。
4. 对于每个 `queries` 中的字符串，使用二分查找来计算满足条件的 `words` 数量。

关键点:
- 预处理 `words` 的频次并排序，以便后续快速查找。
- 使用二分查找来高效地找到满足条件的 `words` 数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m log n)，其中 n 是 `words` 的长度，m 是 `queries` 的长度。
空间复杂度: O(n)，用于存储 `words` 的频次结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def f(s: str) -> int:
    """计算字符串 s 中最小字母的出现频次"""
    min_char = min(s)
    return s.count(min_char)

def num_smaller_by_frequency(queries: List[str], words: List[str]) -> List[int]:
    """
    计算每个查询中满足 f(queries[i]) < f(words[j]) 的 words 数量
    """
    # 预处理 words 的频次
    word_freqs = [f(word) for word in words]
    word_freqs.sort()
    
    # 查询结果
    result = []
    
    for query in queries:
        query_freq = f(query)
        # 使用二分查找找到第一个大于等于 query_freq 的位置
        index = bisect.bisect_right(word_freqs, query_freq)
        result.append(len(words) - index)
    
    return result

Solution = create_solution(num_smaller_by_frequency)