# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3305
标题: Count Prefix and Suffix Pairs II
难度: hard
链接: https://leetcode.cn/problems/count-prefix-and-suffix-pairs-ii/
题目类型: 字典树、数组、字符串、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3045. 统计前后缀下标对 II - 给你一个下标从 0 开始的字符串数组 words 。 定义一个 布尔 函数 isPrefixAndSuffix ，它接受两个字符串参数 str1 和 str2 ： * 当 str1 同时是 str2 的前缀（prefix）和后缀（suffix）时，isPrefixAndSuffix(str1, str2) 返回 true，否则返回 false。 例如，isPrefixAndSuffix("aba", "ababa") 返回 true，因为 "aba" 既是 "ababa" 的前缀，也是 "ababa" 的后缀，但是 isPrefixAndSuffix("abc", "abcd") 返回 false。 以整数形式，返回满足 i < j 且 isPrefixAndSuffix(words[i], words[j]) 为 true 的下标对 (i, j) 的 数量 。 示例 1： 输入：words = ["a","aba","ababa","aa"] 输出：4 解释：在本示例中，计数的下标对包括： i = 0 且 j = 1 ，因为 isPrefixAndSuffix("a", "aba") 为 true 。 i = 0 且 j = 2 ，因为 isPrefixAndSuffix("a", "ababa") 为 true 。 i = 0 且 j = 3 ，因为 isPrefixAndSuffix("a", "aa") 为 true 。 i = 1 且 j = 2 ，因为 isPrefixAndSuffix("aba", "ababa") 为 true 。 因此，答案是 4 。 示例 2： 输入：words = ["pa","papa","ma","mama"] 输出：2 解释：在本示例中，计数的下标对包括： i = 0 且 j = 1 ，因为 isPrefixAndSuffix("pa", "papa") 为 true 。 i = 2 且 j = 3 ，因为 isPrefixAndSuffix("ma", "mama") 为 true 。 因此，答案是 2 。 示例 3： 输入：words = ["abab","ab"] 输出：0 解释：在本示例中，唯一有效的下标对是 i = 0 且 j = 1 ，但是 isPrefixAndSuffix("abab", "ab") 为 false 。 因此，答案是 0 。 提示： * 1 <= words.length <= 105 * 1 <= words[i].length <= 105 * words[i] 仅由小写英文字母组成。 * 所有 words[i] 的长度之和不超过 5 * 105 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来存储每个字符串的哈希值，并使用滚动哈希来快速计算前缀和后缀的哈希值。

算法步骤:
1. 初始化一个哈希表 `prefix_suffix_count` 来存储每个字符串的哈希值及其出现次数。
2. 遍历每个字符串，计算其所有前缀和后缀的哈希值，并更新哈希表。
3. 对于每个字符串，检查其所有前缀和后缀是否已经在哈希表中存在，如果存在则累加计数。

关键点:
- 使用滚动哈希来快速计算前缀和后缀的哈希值。
- 使用哈希表来存储和查找哈希值，以实现高效的计数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是字符串数组的长度，m 是字符串的平均长度。
空间复杂度: O(n * m)，用于存储哈希表中的哈希值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def count_prefix_suffix_pairs(words: List[str]) -> int:
    MOD = 10**9 + 7
    BASE = 31
    prefix_suffix_count = {}
    result = 0

    for word in words:
        n = len(word)
        hash_value = 0
        power = 1
        for i in range(n):
            hash_value = (hash_value * BASE + ord(word[i])) % MOD
            power = (power * BASE) % MOD

        suffix_hash = 0
        for i in range(n - 1, -1, -1):
            suffix_hash = (suffix_hash * BASE + ord(word[i])) % MOD
            if i > 0:
                prefix_hash = (hash_value - (ord(word[i - 1]) * power) % MOD + MOD) % MOD
                if (prefix_hash, suffix_hash) in prefix_suffix_count:
                    result += prefix_suffix_count[(prefix_hash, suffix_hash)]
        
        if (hash_value, suffix_hash) not in prefix_suffix_count:
            prefix_suffix_count[(hash_value, suffix_hash)] = 0
        prefix_suffix_count[(hash_value, suffix_hash)] += 1

    return result

Solution = count_prefix_suffix_pairs